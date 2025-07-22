import subprocess as sp
import time

#THE BASIC of PYTHON
#Printing
"""
str1 = "Hello"
str2 = "World"
print(str1, str2)
"""

"""
count = 0
direction = -1
while 1:
    if count == 0 or count == 10:
        direction *= -1
    sp.run(["clear"])
    print("="*count)
    count += direction
    time.sleep(.1)
    """
"""
#easy while loop
t = 0
while t < 10:
    print(t)
    t += 1
    time.sleep(.2)
    """
"""
arr = []
arr.append(input("enter something"))
print(arr)
"""

open("newfile", "w").write("Random Text")