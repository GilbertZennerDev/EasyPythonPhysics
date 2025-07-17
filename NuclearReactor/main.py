from ping_pong import ping_pong
from moving_line import moving_line
from qr import QR
from boiler import boiler

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import math
import time
import sys

print("Build Your Own Nuclear Reactor! --- In Your garden")
print("="*30)

#ping_pong()

#moving_line()

#QR(10)

boiler(int(sys.argv[1]))