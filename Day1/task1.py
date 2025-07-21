"""
Your job:

First Workshop had 6 participants
Second Workshop has 20 participants

Write a loop which uses that ratio to calculate the next numbers for the next Workshops.
Stop when Participants has reached 8 billion people
"""

import time

ratio = 20/6
number = 6
ws = 1
while ratio * number < 8e9:
    number = int(ratio * number)
    print(ws, number)
    ws += 1
    time.sleep(.1)
