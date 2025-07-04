import tkinter as tk
import subprocess, json


def increment(var: tk.IntVar):
    var.set(var.get() + 1)


def decrement(var: tk.IntVar):
    var.set(var.get() - 1)


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    window.geometry(f"{width}x{height}+{int(x)}+{int(y)}")


def run_ps1_cmd(cmd: str) -> str:
    result = subprocess.run(
        ["powershell", "-Command", cmd],
        capture_output=True,
        text=True,
        check=True,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )

    if result.returncode == 0:
        return result.stdout
    else:
        return result.stderr


def run_ps1_script_elevated(
    script_path: str, window=False, ps_args: list = None
) -> None:
    if ps_args is None:
        ps_args = []

    script_argument_list = [
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        script_path,
    ]

    script_argument_list.extend(ps_args)

    # Build a single string: each argument quoted and joined with spaces (NOT commas)
    argument_list_string = " ".join(
        [
            f'"{arg}"' if " " in arg or "(" in arg or ")" in arg else arg
            for arg in script_argument_list
        ]
    )

    command_to_execute = (
        f"Start-Process powershell.exe "
        f"-ArgumentList '{argument_list_string}' "
        f"-Wait "  # remove for non-blocking
        f"-Verb RunAs "
        f"{'-WindowStyle Hidden' if not window else ''}"
    )

    # changed to .run to block python execution, as it takes a while to create the json file
    # in CreateVMTab.py (see self.get_windows_image_editions). Was subprocess.Popen before.
    subprocess.run(
        ["powershell.exe", "-NoProfile", "-Command", command_to_execute],
        shell=True,
        capture_output=True,
        text=True,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )


def run_ps1_script_2(script_path: str, ps_args: list = None) -> None:
    if ps_args is None:
        ps_args = []

    cmd = [
        "powershell.exe",
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        script_path,
    ] + ps_args

    result = subprocess.Popen(
        cmd,
        # shell=True,
        # capture_output=True,
        # text=True,
        # creationflags=subprocess.CREATE_NO_WINDOW,
    )

    # print("STDOUT:", result.stdout)
    # print("STDERR:", result.stderr)
    # result.check_returncode()


def run_ps1_script(script_path: str, window: bool = False, ps_args: list = None) -> list:
    if ps_args is None:
        ps_args = []

    powershell_command_args = [
        "powershell.exe",
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        script_path,
    ]
    powershell_command_args.extend(ps_args)

    creationflags = subprocess.CREATE_NO_WINDOW if not window else 0

    try:
        result = subprocess.run(
            powershell_command_args,
            capture_output=True,  # Capture stdout and stderr
            text=True,  # Decode stdout/stderr as text
            check=True,  # Raise CalledProcessError for non-zero exit codes
            creationflags=creationflags,  # Control window visibility
        )

        json_output = result.stdout.strip()

        if not json_output:
            print(
                f"Warning: PowerShell script '{script_path}' returned no output to stdout."
            )
            # Even if no output, check stderr in case there was a non-fatal warning
            if result.stderr:
                print(f"PowerShell STDERR: {result.stderr.strip()}")
            return []  # Return an empty list if no output, assuming no error

        return json.loads(json_output)

    except subprocess.CalledProcessError as e:
        print(f"Error executing PowerShell script '{script_path}':")
        print(f"Return code: {e.returncode}")
        print(
            f"STDOUT (if any): {e.stdout.strip()}"
        )  # Show any partial output before error
        print(f"STDERR: {e.stderr.strip()}")
        return None
    except json.JSONDecodeError as e:
        print(
            f"Error decoding JSON from PowerShell output for script '{script_path}': {e}"
        )
        print(f"Raw PowerShell output (STDOUT): '{json_output}'")
        # Include stderr if available, as it might explain malformed JSON
        if "result" in locals() and result.stderr:  # Check if result is defined
            print(f"PowerShell STDERR: {result.stderr.strip()}")
        return None
    except FileNotFoundError:
        print(
            f"Error: 'powershell.exe' or script '{script_path}' not found. Make sure PowerShell is in your PATH."
        )
        return None
