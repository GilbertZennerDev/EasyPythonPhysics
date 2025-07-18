from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import math
import time
import sys
import readchar
import random

def cave_diving():
    console = Console()
    console.clear()
    for i in range(15):
        console.print('.'*80)
        console.print(' '*80)