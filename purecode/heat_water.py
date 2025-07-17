# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gzenner <gzenner@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/07/08 13:55:26 by gzenner           #+#    #+#              #
#    Updated: 2025/07/08 14:09:20 by gzenner          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#some simple first tasks

#heating water up

import sys
import time as t

if len(sys.argv) != 4:
    print("Bad Input")
    exit()

def color_text(text, rgb, water_temp):
    r, g, b = rgb
    return (f"\033[38;2;{int(water_temp * 255 / 150)};{g};{b}m{text}\033[0m")

water_temp = 0
while water_temp < int(sys.argv[1]):
    print("Water Temp: ", end='')
    print(color_text(water_temp, (255, 0, 0), water_temp))
    water_temp += float(sys.argv[3])
    t.sleep(float(sys.argv[2]))