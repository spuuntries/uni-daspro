n = int(input())
base_case = [0, 1, 2]
# The sequence is a tribonacci sequence, so at least 3 samples is necessary to construct it


def why(x):  # YES.
    for i in range(1, x):
        if x <= len(base_case):
            break  # See anton.py
        base_case.append(sum(base_case[i - 1 : i + 2]))
    return base_case


print(why(n)[n - 1])
