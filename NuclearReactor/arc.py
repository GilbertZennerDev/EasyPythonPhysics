import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import math
import time
import sys

def arc():
    block = '\u2588'
    block2 = '\u25A0'
    console = Console()
    arc_height = 8
    while 1:
        console.clear()

        r_value = random.randint(200, 255)
        g_value = random.randint(200, 255)
        
        top_height = 10
        bottom_height = 5
        
        for i in range(3):
            console.print(' '*(30))
        for i in range(5):
            console.print(' '*(10+i), block, ' '*(16-2*i), block, ' '*(10+i))
            console.print(' '*(10+i), block, ' '*(16-2*i), block, ' '*(10+i))
        
        console.print(' '*14, f'[rgb({r_value},{g_value},0)]'+block2*12+f'[/rgb({r_value},{g_value},0)]', ' '*16)
        
        for i in range(5):
            console.print(' '*15, block, ' '*6, block, ' '*15)
        
        console.print(block*45)
        time.sleep(.1)