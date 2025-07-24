def isEven(nb):
    return ((nb%2) == 0)

def ft_atoi(nb):
    #nb = 1234
    power = len(nb) - 1
    inbr = 0
    for c in nb:
        inbr += int(c)*pow(10, power)
        power -= 1
    print(inbr)

def ft_itoa(nb):
    output = ""
    while nb:
        output = str(nb % 10) + output
        nb = int(nb / 10)
    print(output)
    print(type(output))

def ft_putnbr(nb):
    print(nb)
    print(type(nb))

#ft_atoi("1234")
#ft_itoa(1234)
ft_putnbr(1234)