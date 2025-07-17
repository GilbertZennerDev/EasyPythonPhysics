import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import math
import time
import sys

def ping_pong():
    console = Console()
    i = 0
    direction = -1
    lim = int(sys.argv[1])
    while 1:
        if i == lim or i == 0:
            direction *= -1
        i += direction
        console.clear()
        console.print("Testing Console")
        console.print("|", " "*i, "*", " "*(lim-i), "|")
        
        time.sleep(.04)
