p, t = map(int, input().split())


def ways(p, t, i=1, c=[], res=[]):
    # To initialize, we'll basically recurse +i until we hit t
    if t > 0:
        if p + sum(c) != t:
            return ways(p, t, i, c + [i], res)
        else:
            last = c.pop()
            if p + sum(c + [last + 1]) == 100:
                res.append(c + [last + 1])
                if not c:
                    return res
                new_last = c.pop() + 1
                return ways(p, t, i, c + [new_last], res)
            if not c:
                return res
            return ways(p, t, i, c + [last + 1], res)
    else:
        if p + sum(c) != 100:
            return ways(p, t, i, c + [i], res)
        else:
            res.append(c.copy())
            last = c.pop()
            if not c:
                return res
            new_last = c.pop()
            return ways(p, t, i, c + [new_last + 1], res)


print(f"Ada {len(ways(p, t))} cara nih!")
