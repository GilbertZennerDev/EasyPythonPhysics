# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    fork.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gzenner <gzenner@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/07/08 14:09:55 by gzenner           #+#    #+#              #
#    Updated: 2025/07/16 13:43:47 by gzenner          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
A sound fork is ringing at 128 HZ, emitting its sound.
Task1: Write a function that simulates its sound every second at the right frequency
We assume the fork goes mute after 60 seconds and the decrease is linear.
Take note that the frequency never changes.
Task2: Fork1 rings again at 100% but this time we place an identical not-ringing fork next to it.
We let the Fork2 rest there. Will it also start ringing? At a different frequency?
This time we mute Fork1 after 30s. Will Fork2 keep ringing?
Write a function that describes what Fork2 does. If it does ring, be sure to write down its volume descend to 0 in the code as before
"""

import sys
import time as t

def task1():
    frequency = 128
    volume1 = 100
    while volume1 > 0:
        volume1 -= 100/60
        print(f"Fork1 Volume:{volume1:.2f}")
        t.sleep(0.05)

def task2():
    frequency = 128
    volume1 = 100
    volume2 = 80
    passed_time = 0
    while volume1 > 0 or volume2 > 0:
        volume1 -= 100/60
        if volume1 > 0:
            print(f"Fork1 Volume:{volume1:.2f}")
        if volume1 <= 50:
            volume1 = 0
            volume2 -= 80/60
            print(f"Fork2 Volume:{volume2:.2f}")
        t.sleep(0.05)

task2()