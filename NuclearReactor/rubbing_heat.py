import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import readchar
import math
import time
import sys

def rubbing_heat():
    console = Console()
    block = '\u2588'
    rubbing = False
    heat = 0
    while 1:
        if rubbing:
            heat += 10
            heat = min(100, heat)
        else:
            heat -= 10
            heat = max(0, heat)
        r_value = int((heat*255)/100)
        console.clear()
        console.print("[rgb(255,255,255)]" + '='*30 + "[/rgb(255,255,255)]")
        for i in range(20):
            console.print("[rgb(255,255,255)]" + '||' + "[/rgb(255,255,255)]" + f"[rgb({r_value},0,0)]" + block*26 + f"[/rgb({r_value},0,0)]" + "[rgb(255,255,255)]" + '||' + "[/rgb(255,255,255)]")
        console.print("[rgb(255,255,255)]" + '='*30 + "[/rgb(255,255,255)]")
        print('r for rubbing, c for cooling down, x for exit')
        usr_input = readchar.readchar()
        if usr_input == 'x':
            break
        elif usr_input == 'r':
            rubbing = True
        elif usr_input == 'c':
            rubbing = False