# V2, w/ recursion
n = int(input())


def why(base_case, n, i=1):  # Indeed.
    if n <= len(base_case):
        return base_case  # See antonbut.py
    # Credit to ReverentFox (or inst, or whatever other pseudonyms) on Discord for helping me find the pattern
    return why(base_case + [sum(base_case[i - 1 : i + 1]) + (2 - i)], n, i + 1)


print(why([9, 10], n, 1)[n - 1])
