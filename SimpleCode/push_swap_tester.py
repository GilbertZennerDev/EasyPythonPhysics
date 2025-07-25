import subprocess as sp

nbstr = ""
for i in range(11):
        nbstr += str(i) + ' '
nbstr = nbstr[:len(nbstr)-1]
print(nbstr,".")

sp.run(["python", "simple_push_swap.py", nbstr])