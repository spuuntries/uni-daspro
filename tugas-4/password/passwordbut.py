# V2, recursive
n = int(input())


def why(n, res=[]):  # mhm
    if len(res) < 1:
        res = [n]
    if n % 4 != 0 and n == 1:
        return res  # Break the recursion because we've reached the end condition.
    if n % 4 == 0:
        n //= 4
        res += [n]
    else:
        n += 1
        res += [n]
    return why(n, res)


print(" ".join(map(str, why(n))))
