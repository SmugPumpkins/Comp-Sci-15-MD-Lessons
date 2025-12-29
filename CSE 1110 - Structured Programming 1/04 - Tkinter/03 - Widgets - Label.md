# Overview
A `label` is a widget that displays text or images, typically that users will just view but not otherwise interact with. Labels are used to identify controls or other parts of the user interface, provide textual feedback or results, etc.

# Important Information
## Creating a Label
Labels are created using the `ttk.Label` class. Often, the text or image the label will display are specified via configuration options at the same time:
```python
label = ttk.Label(root, text='Full name:')
```
Like frames, labels can take several different configuration options, which can alter how they are displayed.

## Displaying Text
The `text` configuration option (shown above when creating the label) is the most commonly used, particularly when the label is purely decorative or explanatory. You can change what text is displayed by modifying this configuration option. This can be done at any time, not only when first creating the label.

```python
label['text'] = "Hello World!"
```
### Setting Text to a Variable that Changes
You can also have the widget monitor a variable in your script. Whenever the variable changes, the label will automatically update to display the new value of the variable. This is done with the `textvariable` configuration option:
```python
resultsContents = StringVar()
label['textvariable'] = resultsContents
resultsContents.set('Initial value to display')
```
Tkinter only allows you to attach widgets to an instance of the `StringVar` class but not arbitrary Python variables. This class contains all the logic to watch for changes and communicate them back and forth between the variable and Tk. Use the get and set methods to read or write the current value of the variable.
```python
current = resultsContents.get()
resultsContents.set('New value to display')
```

## Displaying Images
Labels can also display an image instead of text. If you just want a static image displayed in your user interface, this is normally the way to do it. We'll go into images in more detail in a later chapter, but for now, let's assume you want to display a PNG stored in a file on disk. This is a two-step process. First, create an image "object." Then, tell the label to display that object via its image configuration option:
```python
image = PhotoImage(file='myimage.png')
label['image'] = image
```
### Text and Images
Labels can also display both an image and text at the same time. You'll often see this in toolbar buttons. To do so, use the `compound` configuration option, which accepts the following values:
|Configuration Option|Result|
|--|--|
|`none` (default)|display only the image if present; if there is no image, display the text specified by the `text` or `textvariable` options|
|`text`|text only (ignore any image provided)|
|`image`|image only (ignore any text provided)|
|`center`|text in the center of the image|
|`top`|image above text|
|`bottom`|image below text|
|`left`|image to left of text|
|`right`|image to right of text|