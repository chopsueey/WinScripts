class ScriptError(Exception):
    """Custom exception for errors raised by PowerShell scripts."""
    def __init__(self, message, stderr=None):
        super().__init__(message)
        self.stderr = stderr

    def __str__(self):
        if self.stderr:
            return f"{super().__str__()}\n\n[PowerShell Error Output]:\n{self.stderr}"
        return super().__str__()
