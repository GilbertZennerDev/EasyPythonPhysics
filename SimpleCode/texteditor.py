print("Welcome to Text Editor")

usrinput = input("")
print(usrinput)
open("testfile_python.txt", "a").write(usrinput)