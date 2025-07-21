from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import math
import time
import sys
import readchar
import random

def ping_pong():
    console = Console()
    i = 0
    direction = -1
    lim = 10
    ball_height = 5
    while 1:
        if i == lim or i == 0:
            if i == lim:
                timestamp = time.time()
                console.print("press button:\n")
                move = readchar.readchar()
                if move != chr(97+ball_height) or time.time() - timestamp > 5:
                    break
            ball_height += random.randint(-1, 1)
            if ball_height > 9:
                ball_height = 9
            if ball_height < 0:
                ball_height = 0
            direction *= -1
        i += direction
        console.clear()
        console.print("Testing Console")
        for j in range(10):
            if j == ball_height:
                console.print("|", " "*i, "*", " "*(lim-i-3), "|", chr(97+j))
            else:
                console.print("|", " "*lim, "|", chr(97+j))
        
        time.sleep(.05)
