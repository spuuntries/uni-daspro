# V2, with recursion
import re

_ = input()


def why(init, curr=None):  # Once again, why.
    if not curr:
        curr = init[0]
    if len(curr) <= 1:
        return init  # We've reached final value
    new = []
    for i in range(len(curr) - 1):
        new.append(sum(curr[i : i + 2]))
    return why(init + [new], new)


res = why([[int(e) for e in re.split(" +", input())]])
res.reverse()
[print(" ".join(map(str, e))) for e in res]
