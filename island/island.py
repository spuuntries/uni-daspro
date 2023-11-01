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
                if f"{r}|{c}" not in tracklist[-1][0].split(","):
                    key = (
                        ",".join(map(lambda x: x[0], tracklist)) + f",{r}|{c}"
                        if f"{r}|{c}" != tracklist[-1][0]
                        else f"{r}|{c}"
                    )

                    def flatten(l):
                        return [item for sublist in l for item in sublist]

                    temp = flatten([e[1] for e in tracklist])
                    for k in tracklist:
                        del track[k[0]]
                    track[key] = temp + [e]

print(len(track.values()))
print(max([len(e) for e in track.values()]))
print(min([len(e) for e in track.values()]))
