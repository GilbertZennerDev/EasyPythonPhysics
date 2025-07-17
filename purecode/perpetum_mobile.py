# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    perpetum_mobile.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gzenner <gzenner@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/07/10 11:53:27 by gzenner           #+#    #+#              #
#    Updated: 2025/07/16 13:56:02 by gzenner          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time as t

charge = 100

while charge > 0:
    charge -= 1
    charge += 0.1
    print(f"Eternal Charge: {charge}")
    t.sleep(0.1)
    