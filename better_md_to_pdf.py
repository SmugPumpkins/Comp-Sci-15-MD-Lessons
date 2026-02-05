"""
Requirements:
    pip install markdown playwright
    playwright install chromium
"""

from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import markdown
from playwright.sync_api import sync_playwright

# =======================
# Config
# =======================

HIGHLIGHTJS_THEME = "github-dark"

PDF_WIDTH_INCHES = 8.5
LEFT_RIGHT_MARGIN_INCHES = 0.5
CSS_DPI = 96
SAFETY_PADDING_INCHES = 0.5
PDF_SCALE = 1.0

# =======================
# HTML Template
# =======================

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>

<link rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/{theme}.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
<script>hljs.highlightAll();</script>

<style>
* {{
    box-sizing: border-box;
}}

body {{
    max-width: 900px;
    margin: 40px auto;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    line-height: 1.6;
    background-color: #14012b;
    color: white;
}}

pre {{
    margin: 1em 0;
    padding: 12px;
    overflow-x: auto;
}}

pre code {{
    padding: 0;
    background: transparent;
    border: 2px solid white;
    border-radius: 5px;
}}

p code {{
    padding: 3px;
    background: #413a4a;
    border-radius: 3px;
}}

/* ---------- PDF / print fixes ---------- */
@media print {{
    pre, code {{
        user-select: text !important;
        -webkit-user-select: text !important;
        pointer-events: auto !important;
    }}

    pre {{
        white-space: pre-wrap;
        word-break: normal;
        overflow: visible;

        /* REMOVE borders (they break selection rendering in Chromium PDFs) */
        border: none !important;

        /* PDF-safe visual replacement for border */
        box-shadow: inset 0 0 0 2px white;
        border-radius: 5px;
    }}

    pre code {{
        background: transparent !important;
    }}

    pre code span {{
        display: inline;
    }}

    body {{
        user-select: text;
    }}
}}

</style>
</head>
<body>
{content}
</body>
</html>
"""

# =======================
# Initial dialog
# =======================

def choose_options(root: tk.Tk):
    result = {
        "mode": None,
        "html": tk.BooleanVar(value=True),
        "pdf": tk.BooleanVar(value=True),
        "overwrite": tk.BooleanVar(value=True),
    }

    def set_mode(value):
        result["mode"] = value
        dialog.destroy()

    dialog = tk.Toplevel(root)
    dialog.title("Markdown Export Options")
    dialog.resizable(False, False)
    dialog.grab_set()

    tk.Label(dialog, text="Select export options", padx=20, pady=10).pack(anchor="w")

    tk.Checkbutton(dialog, text="Export HTML", variable=result["html"]).pack(anchor="w", padx=20)
    tk.Checkbutton(dialog, text="Export PDF", variable=result["pdf"]).pack(anchor="w", padx=20)
    tk.Checkbutton(dialog, text="Overwrite existing files", variable=result["overwrite"]).pack(anchor="w", padx=20)

    tk.Label(dialog, text="Select Markdown input", pady=10).pack()

    tk.Button(dialog, text="Select Folder (all .md files)", width=30,
              command=lambda: set_mode("folder")).pack(pady=5)
    tk.Button(dialog, text="Select Markdown Files", width=30,
              command=lambda: set_mode("files")).pack(pady=5)
    tk.Button(dialog, text="Cancel", width=30,
              command=dialog.destroy).pack(pady=5)

    root.wait_window(dialog)
    return result

# =======================
# Collect Markdown files
# =======================

def collect_md_files(root: tk.Tk, mode: str) -> list[Path]:
    if mode == "folder":
        folder = filedialog.askdirectory(
            parent=root,
            title="Select Folder Containing Markdown Files"
        )
        return list(Path(folder).glob("*.md")) if folder else []

    files = filedialog.askopenfilenames(
        parent=root,
        title="Select Markdown Files",
        filetypes=[("Markdown files", "*.md")]
    )
    return [Path(f) for f in files]

# =======================
# Markdown → HTML
# =======================

def md_to_html(md_path: Path, html_dir: Path, overwrite: bool) -> Path:
    html_dir.mkdir(exist_ok=True)
    html_path = html_dir / (md_path.stem + ".html")

    if html_path.exists() and not overwrite:
        return html_path

    md_text = md_path.read_text(encoding="utf-8")
    html_body = markdown.markdown(md_text, extensions=["fenced_code"])

    html = HTML_TEMPLATE.format(
        title=md_path.stem,
        content=html_body,
        theme=HIGHLIGHTJS_THEME
    )

    html_path.write_text(html, encoding="utf-8")
    return html_path

# =======================
# Progress window (PDF)
# =======================

class ProgressWindow:
    def __init__(self, root: tk.Tk, total: int):
        self.win = tk.Toplevel(root)
        self.win.title("Processing PDFs")
        self.win.resizable(False, False)
        self.win.grab_set()

        tk.Label(self.win, text="Converting HTML to PDF…", padx=20, pady=10).pack()
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

# =======================
# HTML → PDF (single long page)
# =======================

def convert_html_to_pdf(root: tk.Tk, html_files: list[Path], overwrite: bool):
    progress_ui = ProgressWindow(root, len(html_files))

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        for i, html_file in enumerate(html_files, start=1):
            base_dir = html_file.parent.parent
            pdf_dir = base_dir / "PDF"
            pdf_dir.mkdir(exist_ok=True)

            pdf_path = pdf_dir / (html_file.stem + ".pdf")
            if pdf_path.exists() and not overwrite:
                progress_ui.step(i, len(html_files))
                continue

            page.goto(html_file.resolve().as_uri(), wait_until="networkidle")
            page.emulate_media(media="print")

            # Flatten Highlight.js spans for perfect copy/paste in PDF
            page.evaluate("""
                () => {
                    document.querySelectorAll('pre code').forEach(code => {
                        code.classList.remove('hljs');
                        code.querySelectorAll('span').forEach(span => {
                            span.replaceWith(span.textContent);
                        });
                    });
                }
            """)

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

            progress_ui.step(i, len(html_files))

        browser.close()

    progress_ui.close()

# =======================
# Main
# =======================

def main():
    root = tk.Tk()
    root.withdraw()

    options = choose_options(root)
    if options["mode"] is None:
        root.destroy()
        return

    if not options["html"].get() and not options["pdf"].get():
        messagebox.showwarning(
            parent=root,
            title="No Output Selected",
            message="Select at least HTML or PDF output."
        )
        root.destroy()
        return

    md_files = collect_md_files(root, options["mode"])
    if not md_files:
        root.destroy()
        return

    generated_html = []

    for md in md_files:
        base_dir = md.parent
        html_dir = base_dir / "HTML"

        if options["html"].get() or options["pdf"].get():
            html_path = md_to_html(md, html_dir, options["overwrite"].get())
            generated_html.append(html_path)

    if options["pdf"].get():
        convert_html_to_pdf(root, generated_html, options["overwrite"].get())

    root.destroy()

if __name__ == "__main__":
    main()
