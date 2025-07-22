from ping_pong import ping_pong
from moving_line import moving_line
from qr import QR
from boiler import boiler
from mix import mix
from arc import arc
from cave_diving import cave_diving
from rubbing_heat import rubbing_heat

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import math
import time
import sys

print("Build Your Own Nuclear Reactor! --- In Your garden")
print("="*30)

if len(sys.argv) !=2 :
    print("Usage:", sys.argv[0], "ping_pong/moving_line/QR/boiler/mix/arc/cave_diving")
    exit()

arg = sys.argv[1]

if arg == "ping_pong":
    ping_pong()

if arg == "moving_line":
    moving_line()

if arg == "QR":
    QR(5)

if arg == "boiler":
    boiler(12)

if arg == "mix":
    mix(6, 20)

if arg == "arc":
    arc()

if arg == "cave_diving":
    cave_diving()
    
if arg == "rubbingheat":
    rubbing_heat()

#QR(10)

#boiler(int(sys.argv[1]))

#mix(6, 20)

#arc()

#QR(5)

#cave_diving()