# Take Numbers as arguments and store them inside an array
import sys
import time

def checkDouble(arr):
    return len(arr) == len(set(arr))

def getMin(arr):
    minimum = arr[0]
    min_index = 0
    for i, nb in enumerate(arr):
        if nb < minimum:
            minimum = nb
            min_index = i
    return (min_index, minimum)

def collectArgs(args):
    a = []
    for i, number in enumerate(args):
        if i != 0:
            a.append(int(number))
    return (a)

def getNbsFromArgv(argv):
    return argv.split()

def checkAscending(arr):
    """sortedArr = arr.sort()
    for i, nb in enumerate(sortedArr):
        if nb != arr[i]:
            return False"""
    for i, nb in enumerate(arr):
        if i < len(arr) - 1:
            if nb > int(arr[i + 1]):
                return False
    return True

def DoPushSwap():
    a = []
    b = []
    a = getNbsFromArgv(sys.argv[1])
    if not checkDouble(a):
        print("Error: Duplicates")
        exit()
    #print("Start a:",a)
    timestamp = time.time()
    while len(a) > 0:
        i, minimum = getMin(a)
        #print(i, minimum)
        b.insert(0, minimum)
        a.pop(i)
    #print(a)
    #print(b)
    while len(b) > 0:
        a.insert(0, b[0])
        b.pop(0)
    #print("Final: ",a)
    #print(b)
    print("Time Passed: ", time.time() - timestamp)
    #a.insert(0, 1000)
    if not checkAscending(a):
        print("Error: A not ascending")
        exit()

if __name__ == "__main__":
    DoPushSwap()