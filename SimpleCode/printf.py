def ft_printf(strarg, *args):
    #printf("%s", str)
    #example ft_printf("%s", "hello world")
    j = 0
    for i, c in enumerate(args):
        if c == '%':
            if strarg[i + 1] == 's':
                print(args[j], end='')
                j += 1
            elif strarg[i + 1] == 'x':
                print(hex(args[j]), end='')
                j += 1
            elif strarg[i + 1] == 'X':
                print(hex(args[j]).upper(), end='')
                j += 1
            i += 2
        else:
            print(c, end=' ')
    print()

ft_printf("%s %s %X", "hello world", "second text", 255)
print(hex(255))