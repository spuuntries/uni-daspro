# V2, recursive.

n, _ = list(map(int, input().split()))
mat = [list(map(int, e)) for e in [input().split() for _ in range(n)]]
track = {}


def island(track, mat, r, c):
    if r >= len(mat) - 1 and c >= len(mat[0]) - 1:
        return track
    h = mat[r]
    e = h[c]
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

    if c < len(mat[0]) - 1:
        c += 1
    else:
        r += 1
        c = 0
    return island(track, mat, r, c)


print(len(island({}, mat, 0, 0).values()))
print(max([len(e) for e in island({}, mat, 0, 0).values()]))
print(min([len(e) for e in island({}, mat, 0, 0).values()]))
