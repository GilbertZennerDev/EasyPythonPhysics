import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import math
import time
import sys

def QR(size):
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