import tkinter as tk
from dataclasses import dataclass
from organizer import *

window = tk.Tk()
window.configure(background="#FFFFFF")

static_dynamic_values = {"static": 0, "dynamic": 1, 0: "static", 1: "dynamic"}


class Preset:
    def __init__(self, *, pos="static", color="static", size="static", font="static"):
        self.pos = static_dynamic_values[pos]
        self.color = static_dynamic_values[color]
        self.size = static_dynamic_values[size]
        self.font = static_dynamic_values[font]

    def __str__(self):
        return str(vars(self))


class Text:
    def __init__(self, *, text="Hello world", preset=None, pos=Vector2(), colorPreset=ColorPreset(), size=Vector2(), fontsize=18):
        if not (isinstance(preset, Preset) or isinstance(pos, Vector2) or
                isinstance(colorPreset, ColorPreset) or isinstance(size, Vector2) or isinstance(text, str) or isinstance(fontsize, int)):
            raise Exception("Invalid Parameters")

        self.preset = preset
        self.pos = pos
        self.colorPreset = colorPreset
        self.size = size
        self.text = text
        self.fontsize = fontsize
        self.textWidget = tk.Label(text=text, bg=colorPreset.bg_color, fg=colorPreset.fg_color, width=size.x, height=size.y, font=("Arial", self.fontsize))
        self.textWidget.place(x=pos.x, y=pos.y)






paragraph_text = Preset()
print(paragraph_text)

message = "Hello my name is Kevin"
text = Text(text=message, preset=paragraph_text, pos=Vector2(100, 2), colorPreset=ColorPreset(bg_color="#327355", fg_color="#FFFFFF"), size=Vector2(10, 5))
text2 = Text(text=message, preset=paragraph_text, pos=Vector2(100, 100), colorPreset=ColorPreset(bg_color="#327355", fg_color="#FFFFFF"), size=Vector2(10, 5))

window.mainloop()