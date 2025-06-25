import tkinter as tk
from tkinter import ttk
from lib.functions import run_ps1_cmd

class QuickShell(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Command input
        self.input_frame = ttk.Frame(self)
        self.input_frame.pack(fill="x", pady=4)
        self.input_frame.grid_rowconfigure(0, weight=1)
        self.input_frame.grid_columnconfigure(0, weight=1)
        self.input_frame.grid_columnconfigure(1, weight=0)
        self.script_input = ttk.Entry(self.input_frame, font="18")
        self.script_input.grid(row=0, column=0, sticky="ew", padx=4)

        # Run Button
        self.run_script_button = ttk.Button(
            self.input_frame, text="Run", command=self.run_script_and_display_output
        )
        self.run_script_button.grid(row=0, column=1, padx=4)

        self.script_input.bind(
            "<Return>", lambda e: self.run_script_and_display_output()
        )

        # Output Text Widget with Scrollbar
        output_frame = ttk.Frame(self)
        output_frame.pack(expand=True, fill="both", padx=4)

        self.script_output_text = tk.Text(output_frame, wrap="word")
        self.script_output_text.pack(side="left", expand=True, fill="both")

        scrollbar = ttk.Scrollbar(
            output_frame, orient="vertical", command=self.script_output_text.yview
        )
        scrollbar.pack(side="right", fill="y")

        self.script_output_text.config(yscrollcommand=scrollbar.set)


    def run_script_and_display_output(self):
        output = run_ps1_cmd(self.script_input.get())
        self.script_output_text.delete("1.0", tk.END)
        self.script_output_text.insert(tk.END, output)