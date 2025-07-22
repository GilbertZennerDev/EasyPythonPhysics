# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    stage2.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gzenner <gzenner@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/07/16 16:50:39 by gzenner           #+#    #+#              #
#    Updated: 2025/07/21 14:36:01 by gzenner          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Stage 2: Variables and User Interaction
# Learning: variables, input(), string formatting, basic data types

# Getting user information
name = input("What is your name? ")
age = input("How old are you? ")
favorite_color = input("What's your favorite color? ")

# Displaying personalized information
print(f"Hello, {name}!")
print(f"You are {age} years ageold.")
print("Your favorite color is", favorite_color, ".")

# Simple calculations
try:
    birth_year = 2025 - int(age)
    print(f"You were born in approximately {birth_year}.")
except Exception as e:
    print(e)
# Let's be creative
print("🎉 Nice to meet you, " + name + "!")
