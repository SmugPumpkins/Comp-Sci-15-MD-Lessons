# Overview
A `radiobutton` widget lets you choose between one of several mutually exclusive choices. Unlike a checkbutton, they are not limited to just two options. Radiobuttons are always used together in a set, where multiple radiobutton widgets are tied to a single choice or preference. They are appropriate to use when the number of options is relatively small, e.g., 3-5.

# Important Information
## Creating Radiobuttons
Radiobuttons are created using the `ttk.Radiobutton` class. Typically, you'll create and initialize several of them at once:
```python
# Create the variable that the radiobutton is connected to
phone = StringVar()
# Create the first radiobutton option
home = ttk.Radiobutton(parent, text='Home', variable=phone, value='home')
# Create the second radiobutton option
office = ttk.Radiobutton(parent, text='Office', variable=phone, value='office')
# Create the third radiobutton option
cell = ttk.Radiobutton(parent, text='Mobile', variable=phone, value='cell')
```

Radiobuttons share most of the same configuration options as checkbuttons. One exception is that the `onvalue` and `offvalue` options are replaced with a single `value` option. 

Each radiobutton in the set will have the same linked variable but a different value. When the variable holds the matching value, that radiobutton will visually indicate it is selected. If it doesn't match, the radiobutton will be unselected. 

If the linked variable doesn't exist, or you don't specify one with the variable option, radiobuttons also display as "tristate" or indeterminate. This can be checked via the `alternate` state flag.

# Copy, Change, Challenge

## Copy

```python
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Radiobutton Copy Example")

# Variable shared by all radiobuttons
choice = StringVar(value="home")

# Create radiobuttons
home = ttk.Radiobutton(root, text="Home", variable=choice, value="home")
office = ttk.Radiobutton(root, text="Office", variable=choice, value="office")
mobile = ttk.Radiobutton(root, text="Mobile", variable=choice, value="mobile")

# Add radiobuttons to the window
home.grid()
office.grid()
mobile.grid()

root.mainloop()
```

## Change

Modify the program so that:

* The default selected option is **"Office"**
* The text of the third radiobutton is changed to **"Cell Phone"**

## Challenge

Create a program that uses radiobuttons to select a **theme preference**:

* Create **at least four** radiobutton options (for example: `"Light"`, `"Dark"`, `"System"`, `"High Contrast"`)
* All radiobuttons must:
  * Share the same variable
  * Use meaningful string values
* Add a **label** that displays the currently selected option
* When a different radiobutton is selected, the label should automatically update to show the new choice
