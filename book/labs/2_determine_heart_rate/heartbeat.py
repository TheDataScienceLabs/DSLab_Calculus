import serial
from serial.tools import list_ports
import numpy as np
import time

PICO_HWID = "2E8A:0005"


def get_pico_port():
    pico_ports = list(list_ports.grep(PICO_HWID))
    if len(pico_ports) == 0:
        raise Exception(
            "No Raspberry Pi Pico was detected. Check to make sure it is plugged in, and that no other programs are accessing it"
        )
    return pico_ports[0].device


def serial_lines(port, timeout, message, ending):
    """
    Send the given message on the port specified, and yield lines until
    one of them matches ending. If the serial buffer is empty, yield an empty string.
    """
    with serial.Serial(port, timeout=timeout) as s:
        call = str.encode(message + "\r")
        s.write(call)
        response = s.readline()  # first line is always our message
        if response != call + b"\n":
            raise Exception(
                f"""The microcontroller did not receive the command correctly.
                We sent the message {call}, but we received the response {response}.
                Is there something else reading from this serial port?"""
            )
        line = s.readline().decode("UTF8").strip()
        while line != ending:
            yield line
            line = s.readline().decode("UTF8").strip()


def acquire(rate, y, line, fig, min_frame_time=0.1):
    """
    Take in heartbeat data, meanwhile updating the line and figure
    so that you can see the data as it arrives in real time.
    """
    i = 0
    most_recent_draw = time.monotonic()
    for entry in serial_lines(
        get_pico_port(),
        timeout=0.005,
        message=f"{rate},{len(y)}",
        ending="done",
    ):
        if entry:
            y[i] = int(entry)
            i += 1
            line.set_ydata(y)
        if time.monotonic() - most_recent_draw > min_frame_time or not entry:
            # the buffer is empty, so we have time to draw.
            fig.canvas.draw()
            most_recent_draw = time.monotonic()


def rolling_centered_average(x, n):
    """
    Compute a rolling average of n samples, centered. This fills the outside terms
    where there are not enough neighbors with NaN, to preserve the shape.

    arguments
    ---------
    x: array - the points to be averaged.
    n: int - the number to include in each average.

    returns
    -------
    out: array - the centered rolling averages, with NaN at either end filling our to the
    same shape as x.
    """
    out = np.full_like(x, np.nan)
    out[(n - 1) // 2 : -(n // 2)] = np.convolve(x, np.ones(n), mode="valid") / n
    return out
