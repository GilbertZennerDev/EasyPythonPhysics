from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import math
import time
import sys

print("Build Your Own Nuclear Reactor! --- In Your garden")
print("="*30)

"""
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
"""

"""
console = Console()
i = 0
direction = -1
lim = int(sys.argv[1])
height = 10
ball_height = 5
while 1:
    if i == lim or i == 0:
        direction *= -1
    i += direction
    console.clear()
    console.print("Testing Console")
    console.print("[red]CPU[/red]", " "*lim, "[green]PLAYER[/green]")

    for r in range(height):
        if r == ball_height:
            console.print("|", " "*i, "[yellow]*[/yellow]", " "*(lim-i-3), "|")
        else:
            console.print("|", " "*(lim), "|")
    
    time.sleep(.04)
    """

"""
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


    #█ ■

"""

#QR Code
import random

size = 10

console = Console()

console.clear()

value = 64
bin_value = bin(value)
console.print("Bin Value of ", value, " = ", bin_value, value & 0b1000000)

arr = []
for i in range(size):
    arr1 = []
    for j in range(size):
        arr1.append(random.randint(0,1))
    arr.append(arr1)

for i in range(size):
    line = ""
    for j in range(size):
        if arr[i][j]:
            line += '[green]■[/green] '
        else:
            line += '[blue]■[/blue] '
    console.print(line)