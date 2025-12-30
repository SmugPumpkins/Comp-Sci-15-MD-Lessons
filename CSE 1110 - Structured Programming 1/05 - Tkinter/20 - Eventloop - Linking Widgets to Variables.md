# Overview

This lesson explains how Tkinter widgets can be linked to special variable objects so that changes in your program and changes in the user interface stay in sync automatically.

# Important Information

## Why Widgets Use Special Variables

In regular Python programs, variables are simple names that store values. In Tkinter, many widgets need a way to communicate changes back and forth between the user interface and your code. To make this work, Tkinter provides special variable classes that can be linked directly to widgets.

When a widget is linked to one of these variables, changing the variable updates the widget, and user actions that change the widget update the variable.

## The Four Main Tkinter Variable Types

Tkinter provides four main variable classes that you will use most often.

### StringVar

`StringVar` stores text data. It is commonly used with labels, entry widgets, and comboboxes.

```python
name_var = StringVar()
```

### BooleanVar

`BooleanVar` stores either `True` or `False`. It is often used with checkbuttons or to track on/off states.

```python
enabled_var = BooleanVar()
```

### IntVar

`IntVar` stores whole numbers. It is commonly used with radiobuttons or numeric settings.

```python
choice_var = IntVar()
```

### DoubleVar

`DoubleVar` stores decimal numbers. Even though Python usually calls decimal numbers `float`, Tkinter uses the name `DoubleVar`. This comes from other programming languages where decimal numbers are often called “doubles,” and Tkinter was designed to work with multiple languages, not just Python.

```python
volume_var = DoubleVar()
```

## Initializing Variables with Starting Values

Each of these variable classes can be created with an initial value. If you do not provide one, Tkinter will use a default value.

```python
name_var = StringVar(value="Guest")
enabled_var = BooleanVar(value=True)
choice_var = IntVar(value=2)
volume_var = DoubleVar(value=0.75)
```

Using an initial value is helpful when you want widgets to start in a specific state when the program opens.

## Linking Variables to Widgets

Widgets are linked to variables using specific configuration options. Which option you use depends on the widget.

Labels, entries, and comboboxes typically use `textvariable`.

```python
name_label = ttk.Label(root, textvariable=name_var)
name_entry = ttk.Entry(root, textvariable=name_var)
```

Checkbuttons and radiobuttons use the `variable` option.

```python
check = ttk.Checkbutton(root, text="Enable", variable=enabled_var)

radio1 = ttk.Radiobutton(root, text="Option 1", variable=choice_var, value=1)
radio2 = ttk.Radiobutton(root, text="Option 2", variable=choice_var, value=2)
```

When the user interacts with these widgets, the linked variable automatically updates.

## Getting and Setting Variable Values in the Program

Each Tkinter variable class provides `get()` and `set()` methods.

```python
current_name = name_var.get()
name_var.set("Alex")
```

You do not assign to these variables using `=`. Instead, you always use `get()` and `set()` so Tkinter can keep the widget and variable synchronized.

## Using Linked Variables Inside Functions

Linked variables work the same way inside functions, including callbacks. As long as the variable exists in scope, you can read or change its value. 

```python
def submit():
    if enabled_var.get():
        print("Enabled for", name_var.get())
    else:
        print("Disabled")
```

Changing a variable inside a function automatically updates any widgets linked to it.

```python
def reset_name():
    name_var.set("Guest")
```

This is one of the most powerful features of Tkinter’s variable system.

Because linked variables are represented using *objects* instead of *regular python variables*, the `global` keyword is not necessary. You aren't *reassigning* the variable, you are *setting the value of an object*.

## Accessing Values Through Widgets Directly

Some widgets provide methods to get or set their values without accessing the linked variable directly. For example, entry widgets have a `get()` method.

```python
typed_text = name_entry.get()
```

You can also insert or delete text directly in an entry widget.

```python
name_entry.delete(0, "end")
name_entry.insert(0, "New Name")
```

While these widget methods are useful in some cases, using linked variables is usually preferred because it keeps all parts of the program synchronized. Widgets like labels do not provide direct `get()` methods, which makes variable linking especially important for consistent data handling.

Understanding how to link widgets to variables is a key step in writing clean, responsive Tkinter programs that react smoothly to user input.
