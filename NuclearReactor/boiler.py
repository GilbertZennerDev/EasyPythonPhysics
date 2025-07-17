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
    heat = 20
    while heat < 101:
        console.clear()
        console.print("Heat: ", heat)
        for i in range(5):
            console.print(' '*4, '[yellow]'+block+'[/yellow]', '[black]'+block+'[/black]', '[yellow]'+block+'[/yellow]', ' '*5)
        console.print('[yellow]' + block*6 + '[/yellow]' + ' '*3 + '[yellow]' + block*5 + '[/yellow]')
        r_value = int(heat*255/100)
        for i in range(height+3):
            if i < 3:
                console.print('[yellow]'+block+'[/yellow]', f'[rgb(0,0,255)]' + block*10 + f'[/rgb(0,0,255)]', '[yellow]'+block+'[/yellow]')
            else:
                console.print('[yellow]'+block+'[/yellow]', f'[rgb({r_value},0,0)]' + block*10 + f'[/rgb({r_value},0,0)]', '[yellow]'+block+'[/yellow]')
        heat += 1
        console.print('[yellow]'+block*14+'[/yellow]')
        time.sleep(.01)