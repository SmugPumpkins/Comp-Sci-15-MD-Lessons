"""
Requirements:
    pip install markdown
"""

from pathlib import Path
import tkinter as tk
from tkinter import filedialog
import markdown


# ---------- Config ----------

HIGHLIGHTJS_THEME = "github-dark"


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

    tk.Label(dialog, text="How would you like to select Markdown files?", padx=20, pady=10).pack()
    tk.Button(dialog, text="Select Folder (all .md files)", width=30,
              command=lambda: set_choice("folder")).pack(pady=5)
    tk.Button(dialog, text="Select Markdown Files", width=30,
              command=lambda: set_choice("files")).pack(pady=5)
    tk.Button(dialog, text="Cancel", width=30,
              command=dialog.destroy).pack(pady=5)

    root.wait_window(dialog)
    return choice


def collect_md_files(root: tk.Tk) -> list[Path]:
    mode = choose_input_mode(root)
    if mode is None:
        return []

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


# ---------- Markdown → HTML ----------

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>

<!-- Highlight.js -->
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
</style>
</head>
<body>
{content}
</body>
</html>
"""


def md_to_html(md_path: Path) -> None:
    md_text = md_path.read_text(encoding="utf-8")

    html_body = markdown.markdown(
        md_text,
        extensions=["fenced_code"]
    )

    html = HTML_TEMPLATE.format(
        title=md_path.stem,
        content=html_body,
        theme=HIGHLIGHTJS_THEME
    )

    html_path = md_path.with_suffix(".html")
    html_path.write_text(html, encoding="utf-8")


# ---------- Main ----------

def main() -> None:
    root = tk.Tk()
    root.withdraw()

    md_files = collect_md_files(root)

    for md_file in md_files:
        md_to_html(md_file)

    root.destroy()


if __name__ == "__main__":
    main()
