import tkinter as tk
from html_parser import TkHTMLParser


htmlstring = '''
<html>
    <head>
       <title>TesTWEt</title>
    </head>
    <body>
       <h1>Parse me!</h1>
    </body>
</html>
'''
parser = TkHTMLParser()
parser.feed(htmlstring)

window = tk.Tk()

html_keywords = {
    "title": lambda title: set_title(title)
}


def set_title(title):
    window.title(title)


window.mainloop()

