import subprocess as sp

nbstr = ""
for i in range(5):
    nbstr += str(i) + ' '
#print(nbstr)

sp.run(["python", "simple_push_swap.py", nbstr])