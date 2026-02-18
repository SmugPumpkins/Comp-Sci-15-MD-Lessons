"""
Requirements:
    pip install markdown playwright
    playwright install chromium
"""

from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import markdown
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

# =======================
# Config
# =======================

HIGHLIGHTJS_THEME = "github-dark"

PDF_WIDTH_INCHES = 8.5
LEFT_RIGHT_MARGIN_INCHES = 1
CSS_DPI = 96
SAFETY_PADDING_INCHES = 0.5
PDF_SCALE = 1.0
RUBRIC_MARGIN = -0.5
RUBRIC_WIDTH_EXTRA = abs(RUBRIC_MARGIN) * 2

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
      <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Google+Sans+Code:ital,wght@0,600;1,600&display=swap"
        rel="stylesheet">
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
        background-color: #100120;
        color: rgb(238, 238, 238);
    }}

    h1 {{
        font-size: 2.25rem;
    }}

    h1::after {{
        content: "";
        display: block;
        height: 4px;
        background: rgb(238, 238, 238);
        width: 100%;
        margin-top: 0.5rem;
    }}

    h2 {{
        font-size: 2rem;
        color: rgb(252, 204, 141);
        margin: 1.5rem 0.25rem;
    }}

    h2::after {{
        content: "";
        display: block;
        height: 2px;
        background: rgb(252, 204, 141);
        width: 100%;
        margin-top: 0.1rem;
    }}

    h3 {{
        font-weight: 300;
        font-size: 1.75rem;
        color: rgb(250, 249, 202);
        margin: 1.25rem 0.75rem;
    }}

    h3::after {{
        content: "";
        display: block;
        height: 1px;
        background: rgb(250, 249, 202);
        width: 100%;
        margin-top: 0.5rem;
    }}

    h4 {{
        font-weight: 300;
        font-size: 1.5rem;
        color: rgb(201, 245, 248);
        margin: 1rem 1.25rem;
    }}

    h4::after {{
        content: "";
        display: block;
        height: 1px;
        background: rgb(201, 245, 248);
        width: 100%;
        margin-top: 0.5rem;
    }}

    h5 {{
        font-weight: 600;
        font-size: 1.25rem;
        color: rgb(239, 201, 248);
        margin: 1rem 1.5rem;
    }}

    h5::after {{
        content: "";
        display: block;
        height: 1px;
        background: rgb(239, 201, 248);
        width: 100%;
        margin-top: 0.5rem;
    }}

    h6 {{
        font-weight: 300;
        font-size: 1rem;
        color: rgb(248, 210, 201);
        margin: 1rem 1.75rem;
    }}

    h6::after {{
        content: "";
        display: block;
        height: 1px;
        background: rgb(248, 210, 201);
        width: 100%;
        margin-top: 0.5rem;
    }}

    a,
    a:visited {{
        color: rgb(233, 157, 157);
        text-decoration: underline;
        font-weight: 400;
    }}

    a:hover {{
        font-weight: 600;
    }}

    body>p,
    body>ul,
    body>ol {{
        margin: 1rem 2rem;
    }}

    p,
    ul,
    ol {{
        margin-bottom: 1rem;
        text-align: justify;
        text-align-last: left;
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

    code {{
        padding: 3px;
        background: #413a4a;
        border-radius: 3px;
    }}

    table {{
        width: 100%;
        border-collapse: collapse;
        margin: 1.5em 0;
    }}

    th,
    td {{
        border: 1px solid white;
        padding: 8px 10px;
        text-align: left;
        vertical-align: top;
    }}

    thead {{
        background-color: #2b1a4a;
    }}

    tbody tr:nth-child(even) {{
        background-color: #1d1235;
    }}

    #end-message {{
        text-align: center;
        text-align-last: center;
        font-size: 1rem;
        font-weight: 300;
        margin: 0;
        color: rgb(250, 249, 202);
    }}

    footer {{
        margin-top: 7rem;
    }}

    #spacer {{
        height: 1rem;
        background: transparent;
    }}

    #copy {{
        text-align: center;
        text-align-last: center;
        color: #100120;
        color: #403150;
    }}

    .flourish::before {{
        content: "——";
        margin: 0 0.5rem;
    }}

    .flourish::after {{
        content: "——";
        margin: 0 0.5rem;
    }}

    #ducky {{
        line-height: 2.65rem;
        font-family: "Google Sans Code", monospace;
        font-weight: 600;
        font-size: 2.5rem;
        width: fit-content;
        margin: 0 auto;
    }}

    .yellow {{
        color: #f7ec52;
    }}

    .orange {{
        color: #fcac00;
    }}

    .eye {{
        color: #BCFAF2;
    }}

    .water {{
        color: #008dd5;
    }}

    .grass {{
        color: #96f58e;
    }}

    #rubric {{
        margin-left: {rubric_margin}in;
        margin-right: {rubric_margin}in;
        width: calc(100% + {rubric_extra}in);
        font-size: 0.6rem;
    }}
    #rubric th{{
    font-size: 0.8rem;
    }}
</style>
</head>
<body>
{content}
<footer>
<pre id="ducky">
    <span class="yellow">_</span>
 <span class="yellow">__(</span><span class="eye">o</span><span class="yellow">)</span><span class="orange">=</span>
 <span class="yellow">\___)</span>
<span class="grass">&gt;</span><span class="water">~~~~~</span><span class="grass">&lt;</span></pre>
<p id="end-message" class="flourish"><em>Make something worth making.</em></p>
<div id="spacer"></div>
<p id="copy">© Nathan Forsyth</p>
</footer>
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

    # Enable tables + fenced code + sane defaults
    html_body = markdown.markdown(
        md_text,
        extensions=[
            "fenced_code",
            "tables",
            "sane_lists",
            "smarty",
        ]
    )

    soup = BeautifulSoup(html_body, "html.parser")

    header = soup.find("h2", string=lambda s: s and "Mastery Rubric" in s)
    if header:
        table = header.find_next("table")
        if table:
            table["id"] = "rubric"

    html = HTML_TEMPLATE.format(
        title=md_path.stem,
        content=str(soup),
        theme=HIGHLIGHTJS_THEME,
        rubric_margin= RUBRIC_MARGIN,
        rubric_extra = RUBRIC_WIDTH_EXTRA
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

            printable_width_in = PDF_WIDTH_INCHES - (LEFT_RIGHT_MARGIN_INCHES * 2)

            page.evaluate(f"""
                () => {{
                    const wrapper = document.createElement('div');
                    const rubric = document.querySelector('#rubric');
                    if (rubric){{
                        rubric.style.marginLeft = 'calc({(-LEFT_RIGHT_MARGIN_INCHES) - RUBRIC_MARGIN}in)';
                        rubric.style.marginRight = 'calc({(-LEFT_RIGHT_MARGIN_INCHES) - RUBRIC_MARGIN}in)';
                        rubric.style.width = 'calc(100% + {RUBRIC_WIDTH_EXTRA}in)';
                    }}
                    
                    // Full page width wrapper, centered
                    wrapper.style.width = '{PDF_WIDTH_INCHES}in';
                    wrapper.style.margin = '0 auto';

                    // Use padding as the "margins" for normal content
                    wrapper.style.paddingLeft = '{LEFT_RIGHT_MARGIN_INCHES}in';
                    wrapper.style.paddingRight = '{LEFT_RIGHT_MARGIN_INCHES}in';
                    wrapper.style.boxSizing = 'border-box';

                    // Allow content to extend into padding without clipping
                    wrapper.style.overflow = 'visible';

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
                table {
                    page-break-inside: avoid !important;
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
                    "left": "0in",
                    "right": "0in",
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

        html_path = md_to_html(md, html_dir, options["overwrite"].get())
        generated_html.append(html_path)

    if options["pdf"].get():
        convert_html_to_pdf(root, generated_html, options["overwrite"].get())

    root.destroy()

if __name__ == "__main__":
    main()
