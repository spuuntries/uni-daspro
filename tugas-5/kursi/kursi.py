# I hate DP istg.
# Tried to do this via pure recursion tho, true hell.
_ = input()
sessions = list(map(int, input().split()))


def ways(n, track={0: 1}):
    if n < 0:
        return 0
    elif n in track:
        return track[n]
    else:
        result = ways(n - 1) + ways(n - 3) + ways(n - 5)
        track[n] = result
        return result


[print(f"SESI {s+1}: {w}") for s, w in enumerate(map(ways, sessions))]
