import tkinter as tk


class Menubar(tk.Menu):
    def __init__(self, master):
        super().__init__(master)

        file_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="File", menu=file_menu)
