import re

_ = input()


def why(init):  # Once again, why.
    seq = [init]
    curr = init

    while len(curr) > 1:
        new = []
        for i in range(len(curr) - 1):
            new.append(sum(curr[i : i + 2]))
        seq.append(new)
        curr = new

    seq.reverse()
    return seq


res = why([int(e) for e in re.split(" +", input())])
[print(" ".join(map(str, e))) for e in res]
