def ft_strlen(str):
    length = 0
    for c in str:
        if c == 0:
            break
        length += 1
    return length