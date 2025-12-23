# Overview

In this lesson, you will learn why **Python versions matter**, how having multiple versions of Python on one computer works, and how to control which version your system uses. This is important because some **external libraries only work with specific Python versions**, which will become especially relevant later in the course when working with computer vision.

# Important Information

Python is updated regularly. Each update is called a **version**, such as:

* Python 3.9
* Python 3.10
* Python 3.11

While newer versions often add features and improvements, **not all libraries support every version**.

This means:

* A program can work perfectly in one Python version
* The same program may fail in another version
* External libraries may refuse to install or run

## Why Libraries Care About Python Versions

External libraries are written by other programmers. They:

* Choose which Python versions to support
* May not update immediately when Python changes
* Sometimes stop supporting older versions

Later in the course, when working with **computer vision libraries**, you may need to:

* Install a specific Python version
* Switch between Python versions depending on the project

## Checking Installed Python Versions

Many computers have **more than one Python version installed**.

You can check which versions are available by using the command line.

Common commands:

* `python --version`
* `python3 --version`
* `py --list`

On Windows, `py --list` is especially useful because it shows:

* All installed Python versions
* The exact version numbers available

## Python and the PATH

Your computer uses something called the **PATH** to decide which Python version runs when you type `python`.

The PATH:

* Is a list of folders the system searches
* Determines which executable is used first
* Can change depending on installation order

This means:

* Typing `python` may not run the version you expect
* Installing a new version does not always replace the old one

Because of this, **explicitly controlling Python versions is important**.

## Installing Multiple Python Versions

You can safely install multiple Python versions on the same computer.

Good practices:

* Install versions side-by-side
* Do not uninstall older versions unless you are sure they are unused
* Let the Python launcher manage versions when possible

On Windows, the **Python Launcher (`py`)** is designed specifically for this purpose.

## Using `py.ini` to Control Python Versions

On Windows, you can control the default Python version using a configuration file called `py.ini`.

This file is usually placed in your user AppData directory, such as:

* `C:\Users\<your_username>\AppData\Local\Programs\Python`
* or directly in `C:\Users\<your_username>\AppData\Local`

### What `py.ini` Does

The `py.ini` file tells the Python launcher:

* Which Python version to use by default
* Which version to use when running scripts from the command prompt

Without this file, Python chooses a default automatically.
With this file, **you explicitly control the version**.

### Example `py.ini` Configuration

Below is a simple example that sets the default Python version to **Python 3.10** when using the command prompt:

```ini
[defaults]
python=3.10
```

What this means:

* Typing `python` in the command prompt will use Python 3.10
* The Python launcher (`py`) will prefer Python 3.10 unless told otherwise

You can change `3.10` to any version you have installed, such as `3.9` or `3.11`.

This is especially useful when:

* A library only works with a specific Python version
* You want consistent behavior across different projects
* You want to avoid accidentally using the wrong version

You will practice creating and editing `py.ini` later in the course.

## Common Problems and Causes

### Library Will Not Install

**Cause**: Python version is unsupported
**Fix**: Check library documentation for required versions

### Code Works for One Student but Not Another

**Cause**: Different Python versions
**Fix**: Verify installed versions and PATH behavior

### Wrong Python Version Runs

**Cause**: PATH order or default launcher behavior
**Fix**: Use the Python launcher or configure `py.ini`

## Key Takeaways

* Python versions matter
* External libraries often depend on specific versions
* Multiple Python versions can exist on one system
* PATH determines which version runs
* The Python launcher and `py.ini` give you control

Later in the course, you will apply these ideas directly when installing and using advanced libraries.
