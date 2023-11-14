# Got the base algorithm from Kevin,
# modified to return the resulting array of combinations.
# Pure recursive.
import sys

sys.setrecursionlimit(10000)
p, t = map(int, input().split())


def rprepend(i, ways):
    if not ways:
        return []
    else:
        return [[i] + ways[0]] + rprepend(i, ways[1:])


def count_ways(p, t, i=1, target=100):
    if p == target:
        return [[]] if i == 1 else []
    elif p > target or p == t or i > 6:
        return []
    else:
        ways = rprepend(i, count_ways(p + i, t, 1)) + count_ways(p, t, i + 1)
        return ways


res = count_ways(p, t)
# print(res)
print(f"Ada {len(res)} cara nih!")
