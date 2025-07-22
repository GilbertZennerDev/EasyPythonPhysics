"""
print("Hello World")

######################

print("Hello", "World")

######################

print("="*30)

######################

i = 1
while(i <= 10):
    print("="*i)
    i += 1
    
######################

while(i >= 1):
    print("="*i)
    i -= 1

######################

#Taking user input and printing it

print(input("Enter sth\n"))

######################

#Taking Several Inputs, then printing them

inputs = []
i = 0
while i < 3:
    inputs.append(input("Enter sth:"))
    i += 1
print(inputs)   

# Formatting string

str1 = "hello world"
print(str1, "bla", str1, "bla")

# data types

i = 0
print("i = ", i)
i = 0.3
print("i = ", i)
i = 'c'
print("i = ", i)
i = "hello world"
print("i = ", i)
try:
    test = int(i)
except Exception as e:
    print(e)


i = 100
print(i)


str = open("hw.txt", "r").read().splitlines()
print(str)

str = "word1;word2;word3;"
str = str.rsplit(";",1)
print(str)

import random

usrinput = -1
guesses = 0
secretnumber = random.randint(1, 10)
while usrinput != secretnumber:
    usrinput = int(input("Guess number 1 to 10: "))
    if usrinput > secretnumber:
        print("Too high")
    elif usrinput < secretnumber:
        print("Too low")
    guesses += 1
print("Correct Guess. You needed", guesses, "Guesses")


age = int(input("Enter your age:\n"))

if age < 18:
    print("Child")
elif age < 30:
    print("Sous 30")
elif age < 40:
    print("Sous 30")
elif age < 50:
    print("Sous 40")
elif age < 60:
    print("Sous 60")
elif age < 70:
    print("Retired")
else:
    print("Still alive")

#define functions
from ft_strlen import ft_strlen

print(ft_strlen("123"))


# caesar encryption
str = "XYZZZZ"

def caesar_enc(str, diff):
    newstr = ""
    for c in str:
        newstr += chr(ord(c) + diff)
    return newstr

def caesar_dec(str, diff):
    return caesar_enc(str, -diff)

diff = 2
str_enc = caesar_enc(str, diff)
str_dec = caesar_dec(str_enc, diff)
print(str, str_enc, str_dec)
"""

#rock paper scissors
import random

usrinput = input("rock paper scissors: ")
options = "rock paper scissors".split()
cpu = "paper"#options[random.randint(0, 2)]

if usrinput == "rock":
    if cpu == "paper":
        print("CPU WINS")