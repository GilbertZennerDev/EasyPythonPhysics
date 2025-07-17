import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import math
import time
import sys

def mix(height, width):
    console = Console()
    console.clear()
    block = '\u2588'
    obj1_pos = {'x': 2, 'y': int(height / 2)}
    obj2_pos = {'x': width-2, 'y': int(height / 2)}

    while obj1_pos['x'] != obj2_pos['x']:
        for i in range(1, height):
            for j in range(1, width):
                if i == obj1_pos['y'] and j == obj1_pos['x']:
                    console.print('[rgb(255,0,0)]' + block + '[/rgb(255,0,0)]', end = '')
                elif i == obj2_pos['y'] and j == obj2_pos['x']:
                    console.print('[rgb(0,255,0)]' + block + '[/rgb(0,255,0)]', end = '')
                else:
                    console.print('[rgb(0,0,0)]' + block + '[/rgb(0,0,0)]', end = '')
            console.print()
        
        if input("a for approaching, d for distancing:\n") == "a":
            obj1_pos['x'] += 1
            obj2_pos['x'] -= 1
        #time.sleep(.1)
    if obj1_pos['x'] == obj2_pos['x']:
        for i in range(1, height):
            for j in range(1, width):
                if i == obj1_pos['y'] and j == obj1_pos['x']:
                    console.print('[rgb(255,255,255)]' + block + '[/rgb(255,255,255)]', end = '')
                else:
                    console.print('[rgb(0,0,0)]' + block + '[/rgb(0,0,0)]', end = '')
            console.print()