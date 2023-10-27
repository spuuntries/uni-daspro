# V2, with recursion
n = int(input())


def why(init, n, i=1):  # YES.
    if n <= len(init):  # See antonbut.py
        return init
    return why(init + [sum(init[i - 1 : i + 2])], n, i + 1)


print(why([0, 1, 2], n)[n - 1])
# The sequence is a tribonacci sequence, so at least 3 samples is necessary to construct it
