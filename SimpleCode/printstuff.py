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