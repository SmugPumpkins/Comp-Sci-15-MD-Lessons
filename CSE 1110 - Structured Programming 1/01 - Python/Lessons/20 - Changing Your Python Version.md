# Overview

In this lesson, you will learn why **Python versions matter**, how having multiple versions of Python on one computer works, and how to control which version your system uses. This is important because some **external libraries only work with specific Python versions**, which will become especially relevant later in the course when working with computer vision.

# Important Information

Python is updated regularly. Each update is called a **version**, such as:

* Python 3.9
* Python 3.10
* Python 3.11

While newer versions often add features and improvements, **not all libraries support every version**. If a library is not updated to the most recent version of python, you can end up with a program that can run perfectly in one Python version, but the same program may fail in another version. You may also have external libraries refuse to install or run.

## Why Libraries Care About Python Versions

External libraries are written by other programmers. They choose which Python versions to support, and may not update their library immediately when Python changes. Sometimes they will also stop supporting older versions of python.

Later in the course, when working with **computer vision libraries**, you may need to install a specific Python version and switch between Python versions depending on the project.

## Checking Installed Python Versions

Many computers have **more than one Python version installed**.

You can check which version your device defaults to by using this command in the command line. _(Depending on your computer's specific configuration, different prefixes may or may not work, so try all 3 of them)._
```bash
python --version
```
```bash
python3 --version
```
```bash
py --version
```

To see all versions of python that your computer has installed and knows about, you can use the following command. There will be an asterix `*` next to the version your device defaults to when running programs or installing libraries:
```bash
python -0
```
```bash
python3 -0
```
```bash
py -0
```

Your computer uses something called the **PATH** to decide which Python version runs when you type `python`.

The PATH is a list of folders the system searches and determines which executable is used first. This can change depending on the installation order. Typing `python` may not run the version you expect. Installing a new version does not always replace the old one. The version that shows up with the `python --version` command is the version that your PATH is currently using.

**Explicitly controlling Python which python version you use is important**.

## Installing Multiple Python Versions

You can safely install multiple Python versions on the same computer.

Good practices:

* Install versions side-by-side
* Do not uninstall older versions unless you are sure they are unused
* Let the Python launcher manage versions when possible

On Windows, the **Python Launcher (`py`)** is designed specifically for this purpose.
# Using Different Python Versions
## Using `py.ini` to Control Python Versions

On Windows, you can control the default Python version using a configuration file called `py.ini`.

This file is usually placed in your user AppData directory, such as:

* `C:\Users\<your_username>\AppData\Local\Programs\Python`
* or directly in `C:\Users\<your_username>\AppData\Local`

The `py.ini` file tells the Python launcher which Python version to use by default and which version to use when running scripts from the command prompt.

Without this file, Python chooses a default automatically. With this file, **you explicitly control the version**.

Below is a simple example that sets the default Python version to **Python 3.10**:

```ini
[defaults]
python=3.10
```
With this content in your `py.ini` file, typing `python` in the command prompt will use Python 3.10 and the Python launcher (`py`) will prefer Python 3.10 unless told otherwise.

You can change `3.10` to any version you have installed, such as `3.9` or `3.11`. This is especially useful when a library only works with a specific Python version. You may also want consistent behavior across different projects, or you may want to avoid accidentally using the wrong version.

You will practice creating and editing `py.ini` throughout this course.

### Common Problems and Causes

#### Library Will Not Install

* **Cause**: Python version is unsupported
* **Fix**: Check library documentation for required versions

#### Code Works on One Computer, But Not Another

* **Cause**: Different Python versions
* **Fix**: Verify installed versions and PATH behavior

#### Wrong Python Version Runs

* **Cause**: PATH order or default launcher behavior
* **Fix**: Use the Python launcher or configure `py.ini`

## Using Shorthand to Access Different Python Versions

Sometimes you may want to run a python program in a specific version or install a library for a specific version _without_ changing the default python version for your whole computer. You can do this directly in the command prompt by prefacing your commands with the version.

For example:
```bash
py -3.12 my_program.py
```

By adding the `-3.12`, the computer knows to run the program using the `3.12` version of python.

### Installing Libraries with Shorthand

This also works for installing libraries.

For example, this would install the `opencv-python` library for python `3.12`:
```bash
py -3.12 -m pip install opencv-python
```

Whereas using this code would try to install the library for your default python version:
```bash
pip install opencv-python
```
When installing a library for your default python version, if you don't have a compatible version of python selected, the library installation will fail. To fix this, visit the library's documentation to see what versions of python are compatible and use those.

# If You Have Been Working Ahead
Hello! Mr. Forsyth here. The next sections of these lessons will start covering some libraries that we will use for projects. For Structured Programming 1, these first 20 lessons have covered most of the important things you need to understand in terms of general programming. If you understand these concepts well, you __do not__ need any additional general python knowledge...

...however...

...you have been working ahead...

...which probably means that you find this course at least *somewhat* interesting. 

*Again, what we have covered so far is enough to get you full marks for Structured Programming 1.* But you have shown yourself to be someone who has taken an interest in computer science. If you are still ahead, you may find it interesting to cover the Structured Programming 2 Python Lessons starting with [Lesson 01 - Selection - If Statements](/CSE%201120%20-%20Structured%20Programming%202/01%20-%20Python/Lessons/01%20-%20Selection%20-%20If%20Statements.md) and continuing through until [15 - Iteration - Nesting Loops](/CSE%201120%20-%20Structured%20Programming%202/01%20-%20Python/Lessons/15%20-%20Iteration%20-%20Nesting%20Loops.md). 

So far in this course we have covered general python syntax and __sequence__ control structures (the concept that code runs in order). The Structured Programming 2 Lessons cover __selection__ (being able to run code based on conditions) and __iteration__ (looping over code to have it repeat).

These control structures __are not necessary__ for Structured Programming 1, *but* they will let you write code that can do more. A lot more. So much more that you can pretty much do whatever you want with code.

If you are interested in creating projects that go above and beyond, my recommendation is that you skip ahead to those lessons, and then come back after to make your projects. Hopefully, *hopefully*, you'll thank me later.

