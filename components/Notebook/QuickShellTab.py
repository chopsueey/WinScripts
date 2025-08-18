import customtkinter
from lib.functions import run_ps1_cmd
from lib.exceptions import ScriptError


class QuickShellTab(customtkinter.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.pack(expand=True, fill="both")

        # Command input
        self.input_frame = customtkinter.CTkFrame(self)
        self.input_frame.pack(fill="x", padx=5, pady=5)
        self.input_frame.grid_rowconfigure(0, weight=1)
        self.input_frame.grid_columnconfigure(0, weight=1)
        self.input_frame.grid_columnconfigure(1, weight=0)

        self.script_input = customtkinter.CTkEntry(self.input_frame)
        self.script_input.grid(row=0, column=0, sticky="ew", padx=(0, 5))
        self.script_input.bind(
            "<Return>", lambda e: self.run_script_and_display_output()
        )

        # Run Button
        self.run_script_button = customtkinter.CTkButton(
            self.input_frame, text="Run", command=self.run_script_and_display_output
        )
        self.run_script_button.grid(row=0, column=1)

        # Output Text Widget with Scrollbar
        self.output_frame = customtkinter.CTkFrame(self)
        self.output_frame.pack(expand=True, fill="both", padx=5, pady=(0, 5))

        self.script_output_text = customtkinter.CTkTextbox(self.output_frame, wrap="word")
        self.script_output_text.pack(side="left", expand=True, fill="both")

    def run_script_and_display_output(self):
        self.script_output_text.delete("1.0", "end")
        try:
            output = run_ps1_cmd(self.script_input.get())
            self.script_output_text.insert("end", output)
        except ScriptError as e:
            self.script_output_text.insert("end", f"ERROR: {e}")
