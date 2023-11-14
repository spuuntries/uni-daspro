import sys

sys.setrecursionlimit(10000)
# Bruteforce every possible combination.
# This is pure recursive, so technically it fulfills the requirements here,
# if anything, *better* than other submissions lmao.
# Note that this is very naive, and could lead to exponential growth in the call stack size.

# Why was this my first approach? See `uni-daspro\island` for an even worse solution.
p, t = map(int, input().split())


def ways(p, t, memo={}, i=1, c=[], res=[], adj=False):
    if p == t:
        return []
    # Check if value is already in memo
    if str((p, t, i, tuple(c), tuple(res), adj)) in memo:
        return memo[str((p, t, i, tuple(c), tuple(res), adj))]

    c = c.copy()
    res = res.copy()
    # To initialize, we'll basically recurse +i until we hit t
    if t > 0:
        if p + sum(c) != t and not adj and p + sum(c) != 100:
            return ways(p, t, memo, i, c + [i], res, adj)
        elif adj:
            if p + sum(c + [i]) == 100:
                last = c.pop()
                res.append(c + [last, i])
                new_last = last + 1
                if not c and p + sum(c + [new_last]) != 100:
                    memo[str((p, t, i, tuple(c), tuple(res), adj))] = res
                    return res
                return ways(p, t, memo, i, c + [new_last], res, adj)
            elif p + sum(c) == 100:
                last = c.pop()
                res.append(c + [last])
                if not c:
                    memo[str((p, t, i, tuple(c), tuple(res), adj))] = res
                    return res
                new_last = c.pop() + 1
                return ways(p, t, memo, i, c + [new_last], res, adj)
            return ways(p, t, memo, i, c + [i], res, adj)
        else:
            last = c.pop()
            if t - p == 1 and not adj:
                adj = True
                return ways(p, t, memo, i, c + [last + 1], res, adj)
            if p + sum(c + [last + 1]) == 100:
                res.append(c + [last + 1])
                if not c:
                    memo[str((p, t, i, tuple(c), tuple(res), adj))] = res
                    return res
                new_last = c.pop() + 1
                return ways(p, t, memo, i, c + [new_last], res, adj)
            elif p + sum(c + [last]) == 100:
                res.append(c + [last])
                if not c:
                    memo[str((p, t, i, tuple(c), tuple(res), adj))] = res
                    return res
                new_last = c.pop() + 1
                return ways(p, t, memo, i, c + [new_last], res, adj)
            if not c and p + sum(c + [last + 1, i]) != 100:
                return res
            return ways(p, t, memo, i, c + [last + 1], res, adj)
    else:
        if p + sum(c) != 100:
            return ways(p, t, memo, i, c + [i], res)
        else:
            res.append(c.copy())
            last = c.pop()
            if not c:
                memo[str((p, t, i, tuple(c), tuple(res), adj))] = res
                return res
            new_last = c.pop()
            return ways(p, t, memo, i, c + [new_last + 1], res)


res = list(filter(lambda x: all(map(lambda y: y < 7, x)), ways(p, t)))

# print(res)
print(f"Ada {len(res)} cara nih!")
