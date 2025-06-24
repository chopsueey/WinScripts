import tkinter as tk
from tkinter import ttk
from lib.functions import increment, decrement


class State(ttk.Frame):
    def __init__(self, master=None, app_instance=None, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.increase = ttk.Button(
            master=self, text="+", command=lambda: increment(var=app_instance.value)
        )
        self.increase.grid(row=0, column=1)
        self.decrease = ttk.Button(
            master=self, text="-", command=lambda: decrement(var=app_instance.value)
        )
        self.decrease.grid(row=1, column=1)

        self.show_state = ttk.Label(
            master=self,
            style="Heading.TLabel",
            textvariable=app_instance.value,
            padding=20,
        )
        self.show_state.grid(row=0, column=0, rowspan=2)
