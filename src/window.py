from customtkinter import CTk
from customtkinter import set_appearance_mode
from pathlib import Path

class Window(CTk):
    def __init__(self, width, height, title, resizable):
        super().__init__()
        self.title(title)
        self.minsize(width, height)
        self.resizable(resizable, resizable)
        self.iconbitmap(Path(__file__).parent / "assets/icon.ico")
        set_appearance_mode("Light")
        self.configure(fg_color="white")
        
        self.rowconfigure(7, weight=7)
        self.columnconfigure(3, weight=3)