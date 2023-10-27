n = int(input())


def why(base_case, x):  # YES.
    for i in range(1, x):
        if x <= len(base_case):
            break  # See anton.py
        base_case.append(sum(base_case[i - 1 : i + 2]))
    return base_case


print(why([0, 1, 2], n)[n - 1])
# The sequence is a tribonacci sequence, so at least 3 samples is necessary to construct it
