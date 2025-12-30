# Overview

This lesson explains how screen updates work in Tkinter and why changing a widget in code does not redraw the screen instantly.

# Important Information

## Screen Updates Only Happen in the Event Loop

A key detail about Tkinter is that **drawing is not done immediately** when you change a widget. Instead, the widget tells Tkinter, “I need to be redrawn.” The actual drawing happens later when the event loop gets time to do it.

This happens so quickly that it usually looks instant, but the timing matters when your code blocks the event loop.

## Example: Changing Text Doesn’t Redraw Until the Loop Can Run
### Blocked Event Loop
In this example, the label’s text is changed, but the window may not show the change right away if the event loop is busy.

```python
from tkinter import *
from tkinter import ttk
import time

root = Tk()

label = ttk.Label(root, text="Waiting...")
label.grid(row=0, column=0, padx=10, pady=10)

def run_task():
    label["text"] = "Working..."
    time.sleep(2)  # blocks the event loop
    label["text"] = "Done!"

button = ttk.Button(root, text="Start", command=run_task)
button.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()
```

Even though the code changes the label text to `"Working..."` before the sleep, the screen may not redraw until after the sleep finishes, because the event loop is blocked.

### Fixing Updates by Not Blocking the Event Loop

Instead of `sleep`, you can schedule the next step with `after`. This allows the event loop to process redraws in between steps.

```python
from tkinter import *
from tkinter import ttk

root = Tk()

label = ttk.Label(root, text="Waiting...")
label.grid(row=0, column=0, padx=10, pady=10)

def start_task():
    label["text"] = "Working..."
    root.after(2000, finish_task)  # schedule finish in 2 seconds

def finish_task():
    label["text"] = "Done!"

button = ttk.Button(root, text="Start", command=start_task)
button.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()
```

Now the label updates to `"Working..."` immediately because control returns to the event loop, which can redraw the screen.

If the event loop cannot run, screen updates cannot happen. This is why freezing feels like “the window won’t repaint.” It is not that the label or button stopped existing. It is that the event loop is not getting a chance to process redraw events.

