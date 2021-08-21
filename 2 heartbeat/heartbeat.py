import serial
from serial.tools import list_ports
import numpy as np

PICO_HWID = "2E8A:0005"


def get_pico_port():
    return next(list_ports.grep(PICO_HWID)).name


def serial_lines(port, timeout, message, ending):
    """
    Send the given message on the port specified, and yield lines until
    one of them matches ending. If the serial buffer is empty, yield an empty string.
    """
    with serial.Serial(port, timeout=timeout) as s:
        s.write(str.encode(message + "\r"))
        s.readline()  # first line is always our message
        line = s.readline().decode("UTF8").strip()
        while line != ending:
            yield line
            line = s.readline().decode("UTF8").strip()


def acquire(rate, y, line, fig):
    """
    Take in heartbeat data, meanwhile updating the line and figure
    so that you can see the data as it arrives in real time.
    """
    i = 0
    for entry in serial_lines(
        get_pico_port(),
        timeout=0.1 / rate,
        message=f"{rate},{len(y)}",
        ending="done",
    ):
        if entry:
            y[i] = int(entry)
            i += 1
            line.set_ydata(y)
        else:
            # the buffer is empty, so we have time to draw.
            fig.canvas.draw()


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
