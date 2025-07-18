import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import math
import time
import sys
import readchar

def print_bit_chain(usr_chr):
    console = Console()
    ord_usr_chr = ord(usr_chr)
    upper_lim = int(math.log2(ord_usr_chr))
    bit = 1
    bit = bit << upper_lim;
    while bit > 0:
        if ord_usr_chr & bit:
            console.print('[green]■[/green] ', end='')
        else:
            console.print('[blue]■[/blue] ', end='')
        bit = bit >> 1;
    console.print()

def QR(size):
    console = Console()
    usr_input = ""
    while usr_input != ';':
        #console.clear()
        usr_input = readchar.readchar()
        print_bit_chain(usr_input)