import ipaddress

def is_not_empty(value: str) -> bool:
    """Checks if a string is not empty or just whitespace."""
    return bool(value and not value.isspace())

def is_integer(value: str) -> bool:
    """Checks if a string can be converted to an integer."""
    try:
        int(value)
        return True
    except (ValueError, TypeError):
        return False

def is_ip_address(value: str) -> bool:
    """Checks if a string is a valid IPv4 or IPv6 address."""
    if not value:
        return False
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False

def is_cidr(value: str) -> bool:
    """Checks if a string represents a valid CIDR prefix length (0-32)."""
    if not is_integer(value):
        return False
    prefix = int(value)
    return 0 <= prefix <= 32

def is_path_like(value: str, must_exist: bool = False) -> bool:
    """
    Checks if a string is a valid path-like string.
    A simple check for now, can be expanded.
    """
    if not isinstance(value, str) or not value:
        return False
    # For this application, we are mostly concerned with ISO files
    if ".iso" in value.lower():
        # A very basic check to see if it ends with .iso and isn't just ".iso"
        return len(value) > 4
    # A simple check for "No ISO chosen yet."
    if "No ISO chosen yet" in value:
        return False
    return True
