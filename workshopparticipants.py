

#first workshop had 6 people
#second has 20 people

import time
"""
firstAmount = 6
secondAmount = 20
ratio = 20/6

amount = int(secondAmount * ratio)
while amount < 8e9:
    print(amount)
    amount = int(ratio*amount)
    time.sleep(.2)
"""
#Write a simple python function that 
#checks whether the input is odd or even
try:
    nbr = int(input("Enter a number"))
    if nbr % 2 == 0:
        print(nbr, "is even")
    else:
        print(nbr, "is odd")
except Exception as e:
    print(e)
#do your checks