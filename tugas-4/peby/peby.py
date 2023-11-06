n = int(input())


def why(base_case, n):  # Indeed.
    for i in range(1, n):
        if n <= len(base_case):
            break  # See anton.py
        base_case.append(
            sum(base_case[i - 1 : i + 1]) + (2 - i)
        )  # Credit to ReverentFox (or whatever other pseudonyms) on Discord for helping me find the pattern
    return base_case


print(why([9, 10], n)[n - 1])
