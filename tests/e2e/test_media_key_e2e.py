"""E2E tests for media key input with Input Capture API."""

import ch9329py
from e2e_utils import InputCaptureSessionManager


def test_media_key_mute(
    input_capture_session_manager: InputCaptureSessionManager,
) -> None:
    """Test that mute media key event is captured."""
    capture_session = input_capture_session_manager.start_session(name="media_key_mute")
    with capture_session, ch9329py.SerialAdapter(port="/dev/ttyUSB0") as serial_adapter:
        driver = ch9329py.CH9329Driver(serial_adapter)
        input_data = ch9329py.MediaKeyInput(keys=[ch9329py.MediaKey.KEY_MUTE])
        driver.send_media_key_input(input_data)
        driver.send_media_key_input(ch9329py.MediaKeyInput(keys=[]))

    # Media keys send press (value=1) and CH9329 doesn't send release automatically
    # so we expect only the press event
    expected_codes_and_values = [
        ("('KEY_MIN_INTERESTING', 'KEY_MUTE')", 1),
        ("('KEY_MIN_INTERESTING', 'KEY_MUTE')", 0),
    ]
    actual_codes_and_values = [
        (event.code_name, event.value) for event in capture_session.events
    ]
    assert actual_codes_and_values == expected_codes_and_values


def test_media_key_volume_up(
    input_capture_session_manager: InputCaptureSessionManager,
) -> None:
    """Test that volume up media key event is captured."""
    capture_session = input_capture_session_manager.start_session(
        name="media_key_volume_up"
    )
    with capture_session, ch9329py.SerialAdapter(port="/dev/ttyUSB0") as serial_adapter:
        driver = ch9329py.CH9329Driver(serial_adapter)
        input_data = ch9329py.MediaKeyInput(keys=[ch9329py.MediaKey.KEY_VOLUMEUP])
        driver.send_media_key_input(input_data)
        driver.send_media_key_input(ch9329py.MediaKeyInput(keys=[]))

    expected_codes_and_values = [
        ("KEY_VOLUMEUP", 1),
        ("KEY_VOLUMEUP", 0),
    ]
    actual_codes_and_values = [
        (event.code_name, event.value) for event in capture_session.events
    ]
    assert actual_codes_and_values == expected_codes_and_values


def test_media_key_volume_down(
    input_capture_session_manager: InputCaptureSessionManager,
) -> None:
    """Test that volume down media key event is captured."""
    capture_session = input_capture_session_manager.start_session(
        name="media_key_volume_down"
    )
    with capture_session, ch9329py.SerialAdapter(port="/dev/ttyUSB0") as serial_adapter:
        driver = ch9329py.CH9329Driver(serial_adapter)
        input_data = ch9329py.MediaKeyInput(keys=[ch9329py.MediaKey.KEY_VOLUMEDOWN])
        driver.send_media_key_input(input_data)
        driver.send_media_key_input(ch9329py.MediaKeyInput(keys=[]))

    expected_codes_and_values = [
        ("KEY_VOLUMEDOWN", 1),
        ("KEY_VOLUMEDOWN", 0),
    ]
    actual_codes_and_values = [
        (event.code_name, event.value) for event in capture_session.events
    ]
    assert actual_codes_and_values == expected_codes_and_values


def test_media_key_play_pause(
    input_capture_session_manager: InputCaptureSessionManager,
) -> None:
    """Test that play/pause media key event is captured."""
    capture_session = input_capture_session_manager.start_session(
        name="media_key_play_pause"
    )
    with capture_session, ch9329py.SerialAdapter(port="/dev/ttyUSB0") as serial_adapter:
        driver = ch9329py.CH9329Driver(serial_adapter)
        input_data = ch9329py.MediaKeyInput(keys=[ch9329py.MediaKey.KEY_PLAYPAUSE])
        driver.send_media_key_input(input_data)
        driver.send_media_key_input(ch9329py.MediaKeyInput(keys=[]))

    expected_codes_and_values = [
        ("KEY_PLAYPAUSE", 1),
        ("KEY_PLAYPAUSE", 0),
    ]
    actual_codes_and_values = [
        (event.code_name, event.value) for event in capture_session.events
    ]
    assert actual_codes_and_values == expected_codes_and_values


def test_media_key_next_track(
    input_capture_session_manager: InputCaptureSessionManager,
) -> None:
    """Test that next track media key event is captured."""
    capture_session = input_capture_session_manager.start_session(
        name="media_key_next_track"
    )
    with capture_session, ch9329py.SerialAdapter(port="/dev/ttyUSB0") as serial_adapter:
        driver = ch9329py.CH9329Driver(serial_adapter)
        input_data = ch9329py.MediaKeyInput(keys=[ch9329py.MediaKey.KEY_NEXTSONG])
        driver.send_media_key_input(input_data)
        driver.send_media_key_input(ch9329py.MediaKeyInput(keys=[]))

    expected_codes_and_values = [
        ("KEY_NEXTSONG", 1),
        ("KEY_NEXTSONG", 0),
    ]
    actual_codes_and_values = [
        (event.code_name, event.value) for event in capture_session.events
    ]
    assert actual_codes_and_values == expected_codes_and_values


def test_media_key_prev_track(
    input_capture_session_manager: InputCaptureSessionManager,
) -> None:
    """Test that previous track media key event is captured."""
    capture_session = input_capture_session_manager.start_session(
        name="media_key_prev_track"
    )
    with capture_session, ch9329py.SerialAdapter(port="/dev/ttyUSB0") as serial_adapter:
        driver = ch9329py.CH9329Driver(serial_adapter)
        input_data = ch9329py.MediaKeyInput(keys=[ch9329py.MediaKey.KEY_PREVIOUSSONG])
        driver.send_media_key_input(input_data)
        driver.send_media_key_input(ch9329py.MediaKeyInput(keys=[]))

    expected_codes_and_values = [
        ("KEY_PREVIOUSSONG", 1),
        ("KEY_PREVIOUSSONG", 0),
    ]
    actual_codes_and_values = [
        (event.code_name, event.value) for event in capture_session.events
    ]
    assert actual_codes_and_values == expected_codes_and_values


def test_media_key_all_keys(
    input_capture_session_manager: InputCaptureSessionManager,
) -> None:
    """Test that all media key events are captured."""
    capture_session = input_capture_session_manager.start_session(
        name="media_key_all_keys"
    )
    with capture_session, ch9329py.SerialAdapter(port="/dev/ttyUSB0") as serial_adapter:
        driver = ch9329py.CH9329Driver(serial_adapter)
        for media_key in ch9329py.MediaKey:
            input_data = ch9329py.MediaKeyInput(keys=[media_key])
            driver.send_media_key_input(input_data)
            driver.send_media_key_input(ch9329py.MediaKeyInput(keys=[]))

    # Map MediaKey enum to expected evdev key names
    media_key_to_evdev_name = {
        ch9329py.MediaKey.KEY_EJECTCD: "KEY_EJECTCD",
        ch9329py.MediaKey.KEY_STOPCD: "KEY_STOPCD",
        ch9329py.MediaKey.KEY_PREVIOUSSONG: "KEY_PREVIOUSSONG",
        ch9329py.MediaKey.KEY_NEXTSONG: "KEY_NEXTSONG",
        ch9329py.MediaKey.KEY_PLAYPAUSE: "KEY_PLAYPAUSE",
        ch9329py.MediaKey.KEY_MUTE: "('KEY_MIN_INTERESTING', 'KEY_MUTE')",
        ch9329py.MediaKey.KEY_VOLUMEDOWN: "KEY_VOLUMEDOWN",
        ch9329py.MediaKey.KEY_VOLUMEUP: "KEY_VOLUMEUP",
    }

    expected_codes_and_values: list[tuple[str, int]] = []
    for media_key in ch9329py.MediaKey:
        evdev_name = media_key_to_evdev_name[media_key]
        expected_codes_and_values.append((evdev_name, 1))
        expected_codes_and_values.append((evdev_name, 0))

    actual_codes_and_values = [
        (event.code_name, event.value) for event in capture_session.events
    ]
    assert actual_codes_and_values == expected_codes_and_values
