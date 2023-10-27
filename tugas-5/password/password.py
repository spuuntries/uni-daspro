n = int(input())


def why(n):  # mhm
    res = []
    while n % 4 == 0 or n != 1:
        res.append(n)
        if n % 4 == 0:
            n //= 4
        else:
            n += 1
    res.append(n)
    return res


print(" ".join(map(str, why(n))))
