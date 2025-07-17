import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import math
import time
import sys

def boiler(height):
    block = '\u2588'
    console = Console()
    heat = 0
    while heat < 100:
        console.clear()
        console.print("Heat: ", heat)
        console.print('[yellow]' + block*14 + '[/yellow]')
        r_value = int(heat*255/100)
        for i in range(height):
            console.print('[yellow]|[/yellow]', f'[rgb({r_value},0,0)]' + block*10 + f'[/rgb({r_value},0,0)]', '[yellow]|[/yellow]')
        heat += 1
        console.print('[yellow]=[/yellow]'*14)
        time.sleep(.2)