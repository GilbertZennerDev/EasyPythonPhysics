import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import math
import time
import sys

def moving_line():
    console = Console()

    direction = -1
    lim = 0
    while 1:
        console.clear()
        for j in range(10, 0, -1):
            if j == lim:
                console.print('[green]■[/green] '*5)
            else:
                console.print('[black]■[/black] '*5)
        if lim == 10 or lim == 0:
            direction *= -1
        lim += direction
        time.sleep(0.2)