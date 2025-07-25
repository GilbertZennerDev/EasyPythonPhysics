import sys

def savetext(total_input):
    for line in total_input:
            open("testfile_python.txt", "a").write(line + '\n')

print("Welcome to Text Editor")
total_input = []
while 1:
    usrinput = input("")
    if usrinput == "exit":
        savetext(total_input)
        exit()
    elif usrinput == "save":
        savetext(total_input)
    else:
        total_input.append(usrinput)
        print(total_input)