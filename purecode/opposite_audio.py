# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    opposite_audio.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gzenner <gzenner@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/07/08 14:38:02 by gzenner           #+#    #+#              #
#    Updated: 2025/07/08 15:47:38 by gzenner          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time as t
import math


while 1:
    sound1 = math.sin(t.time())
    sound2 = -sound1
    print(f"sound1: {sound1:.2f}")
    print(f"\033[38;2;255;0;0m sound2: {sound2:.2f}\033[0m")
    print(f"\033[38;2;0;255;0m sound3: {(sound2 + sound1):.2f}\033[0m")
    t.sleep(0.1)

#Task: print what you hear if playing both at the same time?