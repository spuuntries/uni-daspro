n = int(input())
base_case = [0, 1]


def why(x):  # We really don't need this istg
    for i in range(1, x):
        if x <= len(
            base_case
        ):  # Since this is within base case range, it'd be redundant to recalculate
            break
        base_case.append(
            sum(base_case[i - 1 : i + 1])
        )  # Recursion to form a fibonacci sequence
    return base_case


print(sum(why(n)[0:n]) * 125)
