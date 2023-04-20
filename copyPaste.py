import win32clipboard

# returns whatever data is stored in the clipboard
def paste():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return(data)

# replaces a piece of text with whatever was on the clipboard
def copy(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text,win32clipboard.CF_TEXT)
    win32clipboard.CloseClipboard()