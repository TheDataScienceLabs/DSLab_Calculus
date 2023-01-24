"Heartbeat connection module"

import serial
from serial.tools import list_ports
import time

PICO_HWID = "2E8A:0005"  # Vendor Product ID for Raspberry Pi Pico

def get_pico_port():
    pico_ports = list(list_ports.grep(PICO_HWID))
    if len(pico_ports) == 0:
        raise Exception(
            "No Raspberry Pi Pico was detected. Check to make sure it is plugged in, and that no other programs are accessing it"
        )
    return pico_ports[0].device # Full device name/path4


def serial_lines(port, num_samp, message, timeout):
    """
    Listen to the port of the connected device and yield lines. If the serial buffer is empty, yield an empty string.
    """
    with serial.Serial(port, timeout=timeout) as s:
        # Add EOL control character (\n (LF), \r (CR), \r\n (CRLF)) to indicate that what is before will be sent.
        # Then make an utf-8 encoded version of the string
        call = str.encode(message + "\r")
        s.write(call)
        response = s.readline()
        line = s.readline().decode("UTF8").strip()
        for k in range(num_samp):
            yield line
            line = s.readline().decode("UTF8").strip()
            
            
def acquire(rate, y, line, fig, num_samp, min_frame_time=0.1):
    """
    Take in heartbeat data, meanwhile updating the line and figure
    so that you can see the data as it arrives in real time.
    """
    i = 0
    most_recent_draw = time.monotonic()
    for entry in serial_lines(
        get_pico_port(),
        num_samp,
        message = str(rate),
        timeout = 0.5
    ):
        if entry:
            #y[i] = int(entry)
            y[i] = int(''.join(c for c in entry if (c in "0123456789"))
            i += 1
            line.set_ydata(y)
        if time.monotonic() - most_recent_draw > min_frame_time or not entry:
            # the buffer is empty, so we have time to draw.
            fig.canvas.draw()
            most_recent_draw = time.monotonic()