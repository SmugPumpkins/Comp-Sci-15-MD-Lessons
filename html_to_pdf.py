"""
Requirements:
    pip install playwright
    playwright install chromium
"""


from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from playwright.sync_api import sync_playwright

PDF_WIDTH_INCHES = 8.5
LEFT_RIGHT_MARGIN_INCHES = 0.5
CSS_DPI = 96
SAFETY_PADDING_INCHES = 0.5
PDF_SCALE = 1.0


# ---------- Input mode dialog ----------

def choose_input_mode(root: tk.Tk) -> str | None:
    choice = None

    def set_choice(value):
        nonlocal choice
        choice = value
        dialog.destroy()

    dialog = tk.Toplevel(root)
    dialog.title("Choose Input Type")
    dialog.resizable(False, False)
    dialog.grab_set()

    tk.Label(dialog, text="How would you like to select HTML files?", padx=20, pady=10).pack()
    tk.Button(dialog, text="Select Folder", width=25, command=lambda: set_choice("folder")).pack(pady=5)
    tk.Button(dialog, text="Select HTML Files", width=25, command=lambda: set_choice("files")).pack(pady=5)
    tk.Button(dialog, text="Cancel", width=25, command=dialog.destroy).pack(pady=5)

    root.wait_window(dialog)
    return choice


def collect_html_files(root: tk.Tk) -> list[Path]:
    mode = choose_input_mode(root)
    if mode is None:
        return []

    if mode == "folder":
        folder = filedialog.askdirectory(parent=root, title="Select Folder Containing HTML Files")
        return list(Path(folder).glob("*.html")) if folder else []

    files = filedialog.askopenfilenames(
        parent=root,
        title="Select HTML Files",
        filetypes=[("HTML files", "*.html")]
    )
    return [Path(f) for f in files]


# ---------- Progress window ----------

class ProgressWindow:
    def __init__(self, root: tk.Tk, total: int):
        self.win = tk.Toplevel(root)
        self.win.title("Processing PDFs")
        self.win.resizable(False, False)
        self.win.grab_set()

        tk.Label(self.win, text="Converting HTML files to PDF…", padx=20, pady=10).pack()
        self.progress = ttk.Progressbar(self.win, length=300, mode="determinate", maximum=total)
        self.progress.pack(padx=20, pady=10)
        self.status = tk.Label(self.win, text=f"0 / {total}")
        self.status.pack(pady=(0, 10))
        self.win.update()

    def step(self, current: int, total: int):
        self.progress["value"] = current
        self.status.config(text=f"{current} / {total}")
        self.win.update()

    def close(self):
        self.win.destroy()


# ---------- Conversion ----------

def convert_html_to_pdf(root: tk.Tk, html_files: list[Path]) -> None:
    progress_ui = ProgressWindow(root, len(html_files))

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        for i, html_file in enumerate(html_files, start=1):
            base_dir = html_file.parent

            html_dir = base_dir / "HTML"
            pdf_dir = base_dir / "PDF"
            html_dir.mkdir(exist_ok=True)
            pdf_dir.mkdir(exist_ok=True)

            page.goto(html_file.resolve().as_uri(), wait_until="networkidle")
            page.emulate_media(media="print")

            printable_width_in = PDF_WIDTH_INCHES - (LEFT_RIGHT_MARGIN_INCHES * 2)

            page.evaluate(f"""
                () => {{
                    const wrapper = document.createElement('div');
                    wrapper.style.width = '{printable_width_in}in';
                    wrapper.style.margin = '0 auto';
                    while (document.body.firstChild) {{
                        wrapper.appendChild(document.body.firstChild);
                    }}
                    document.body.appendChild(wrapper);
                }}
            """)

            page.add_style_tag(content="""
                @page { margin: 0 !important; }
                html, body {
                    margin: 0 !important;
                    padding: 0 !important;
                    overflow: visible !important;
                }
                * {
                    page-break-before: avoid !important;
                    page-break-after: avoid !important;
                    page-break-inside: avoid !important;
                }
            """)

            height_px = page.evaluate("() => Math.ceil(document.body.scrollHeight)")
            height_in = (height_px / CSS_DPI) + SAFETY_PADDING_INCHES

            pdf_path = pdf_dir / html_file.with_suffix(".pdf").name

            page.pdf(
                path=str(pdf_path),
                width=f"{PDF_WIDTH_INCHES}in",
                height=f"{height_in}in",
                scale=PDF_SCALE,
                print_background=True,
                margin={
                    "top": "0in",
                    "bottom": "0in",
                    "left": f"{LEFT_RIGHT_MARGIN_INCHES}in",
                    "right": f"{LEFT_RIGHT_MARGIN_INCHES}in",
                },
                prefer_css_page_size=False,
            )

            html_file.rename(html_dir / html_file.name)

            progress_ui.step(i, len(html_files))

        browser.close()

    progress_ui.close()


# ---------- Main ----------

def main() -> None:
    root = tk.Tk()
    root.withdraw()

    html_files = collect_html_files(root)

    if not html_files:
        messagebox.showwarning(
            parent=root,
            title="No HTML Files Detected",
            message="No HTML files were selected or found."
        )
        root.destroy()
        return

    convert_html_to_pdf(root, html_files)

    messagebox.showinfo(
        parent=root,
        title="Process Complete",
        message=f"Successfully created {len(html_files)} PDF file(s)."
    )

    root.destroy()


if __name__ == "__main__":
    main()
