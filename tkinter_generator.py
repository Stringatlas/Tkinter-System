import tkinter as tk

window = tk.Tk()

html_keywords = {
    "title": lambda title: set_title(title)
}

def set_title(title):
    window.title(title)

window.mainloop()