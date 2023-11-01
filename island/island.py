n, _ = list(map(int, input().split()))
mat = [list(map(int, e)) for e in [input().split() for _ in range(n)]]
track = {}

for r, h in enumerate(mat):
    for c, e in enumerate(h):
        if e == 1:
            tracklist = list(
                filter(
                    lambda k: any(
                        map(
                            lambda x: (
                                r + 1 == list(map(int, x.split("|")))[0]
                                and c == list(map(int, x.split("|")))[1]
                            )
                            or (
                                r - 1 == list(map(int, x.split("|")))[0]
                                and c == list(map(int, x.split("|")))[1]
                            )
                            or (
                                c + 1 == list(map(int, x.split("|")))[1]
                                and r == list(map(int, x.split("|")))[0]
                            )
                            or (
                                c - 1 == list(map(int, x.split("|")))[1]
                                and r == list(map(int, x.split("|")))[0]
                            ),
                            k[0].split(","),
                        )
                    ),
                    list(track.items()),
                )
            )

            if not len(tracklist):
                track[f"{r}|{c}"] = [e]
            else:
                key = (
                    tracklist[-1][0] + f",{r}|{c}"
                    if f"{r}|{c}" != tracklist[-1][0]
                    else f"{r}|{c}"
                )
                track[key] = track[tracklist[-1][0]] + [e]
                del track[tracklist[-1][0]]

print(len(track.values()))
print(max([len(e) for e in track.values()]))
print(min([len(e) for e in track.values()]))
