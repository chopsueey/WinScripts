import tkinter as tk
from tkinter import ttk
from lib.functions import run_ps1_cmd
from lib.ui_helpers import StyledFrame, StyledEntry, StyledButton


class QuickShellTab(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master)

        # Command input
        self.input_frame = StyledFrame(self)
        self.input_frame.pack(fill="x", padx=5, pady=5)
        self.input_frame.grid_rowconfigure(0, weight=1)
        self.input_frame.grid_columnconfigure(0, weight=1)
        self.input_frame.grid_columnconfigure(1, weight=0)

        self.script_input = StyledEntry(self.input_frame)
        self.script_input.grid(row=0, column=0, sticky="ew", padx=(0, 5))
        self.script_input.bind(
            "<Return>", lambda e: self.run_script_and_display_output()
        )

        # Run Button
        self.run_script_button = StyledButton(
            self.input_frame, text="Run", command=self.run_script_and_display_output
        )
        self.run_script_button.grid(row=0, column=1)

        # Output Text Widget with Scrollbar
        self.output_frame = StyledFrame(self)
        self.output_frame.pack(expand=True, fill="both", padx=5, pady=(0, 5))

        # tk.Text and ttk.Scrollbar do not have styled helpers, so they are used directly.
        # Their appearance is generally governed by the OS or a base Tcl/Tk theme.
        self.script_output_text = tk.Text(self.output_frame, wrap="word", relief="flat", borderwidth=1)
        self.script_output_text.pack(side="left", expand=True, fill="both")

        self.scrollbar = ttk.Scrollbar(
            self.output_frame, orient="vertical", command=self.script_output_text.yview
        )
        self.scrollbar.pack(side="right", fill="y")

        self.script_output_text.config(yscrollcommand=self.scrollbar.set)

    def run_script_and_display_output(self):
        output = run_ps1_cmd(self.script_input.get())
        self.script_output_text.delete("1.0", tk.END)
        self.script_output_text.insert(tk.END, output)
