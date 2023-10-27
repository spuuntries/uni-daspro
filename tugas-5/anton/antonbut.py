# V2, fulfilling requirement, i.e. use of recursion
n = int(input())


def why(init, n, i=1):  # We really don't need this istg
    if n <= len(init):  # Since this result has reached desired range, we end recursion
        return init
    return why(
        init + [sum(init[i - 1 : i + 1])], n, i + 1
    )  # Recurse to form a fibonacci sequence


print(sum(why([0, 1], n, 1)[0:n]) * 125)
