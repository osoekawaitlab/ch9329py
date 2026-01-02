"""Python driver for CH9329 USB HID device.

This package provides a low-level state-based API for controlling CH9329
USB HID devices. The CH9329 chip allows simulation of keyboard, mouse, and
media key inputs through serial communication.

Basic usage:
    >>> from ch9329py import CH9329Driver, SerialAdapter, KeyboardInput, KeyCode
    >>> adapter = SerialAdapter("/dev/ttyUSB0", 9600)
    >>> driver = CH9329Driver(adapter)
    >>> input_data = KeyboardInput(keys=[KeyCode.KEY_A])
    >>> driver.send_keyboard_input(input_data)
    >>> driver.close()

Context manager usage:
    >>> with SerialAdapter("/dev/ttyUSB0", 9600) as adapter:
    ...     with CH9329Driver(adapter) as driver:
    ...         input_data = KeyboardInput(keys=[KeyCode.KEY_H, KeyCode.KEY_I])
    ...         driver.send_keyboard_input(input_data)
"""

from ch9329py.adapter import CommunicationAdapter, SerialAdapter
from ch9329py.driver import CH9329Driver
from ch9329py.exceptions import CH9329PyError, UnsupportedEvdevCodeError
from ch9329py.models import (
    KeyboardInput,
    KeyCode,
    MediaKey,
    MediaKeyInput,
    ModifierKey,
    MouseButton,
    MouseInput,
)

__version__ = "0.2.1"

__all__ = [
    "CH9329Driver",
    "CH9329PyError",
    "CommunicationAdapter",
    "KeyCode",
    "KeyboardInput",
    "MediaKey",
    "MediaKeyInput",
    "ModifierKey",
    "MouseButton",
    "MouseInput",
    "SerialAdapter",
    "UnsupportedEvdevCodeError",
    "__version__",
]
