"""Exceptions for ch9329py library."""


class CH9329PyError(Exception):
    """Base exception for ch9329py library."""


class UnsupportedEvdevCodeError(CH9329PyError):
    """Raised when an evdev code is not supported by CH9329.

    Args:
        code: The unsupported evdev code.
        message: Optional custom error message.

    Examples:
        >>> raise UnsupportedEvdevCodeError(999)
        UnsupportedEvdevCodeError: Evdev code 999 is not supported by CH9329
    """

    def __init__(self, code: int, message: str | None = None) -> None:
        """Initialize the exception.

        Args:
            code: The unsupported evdev code.
            message: Optional custom error message.
        """
        self.code = code
        if message is None:
            message = f"Evdev code {code} is not supported by CH9329"
        super().__init__(message)
