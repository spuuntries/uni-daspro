n, m = list(map(int, input().split()))
mat = [list(map(int, e)) for e in [input().split() for _ in range(n)]]


def island(track: list, mat, r, c):
    if r > len(mat) - 1:
        return [e.split(",") for e in track]
    h = mat[r]
    e = h[c]
    if e == 1:
        check_list = list(
            filter(
                lambda x: f"{r-1}|{c}" in x
                or f"{r+1}|{c}" in x
                or f"{r}|{c-1}" in x
                or f"{r}|{c+1}" in x,
                track,
            )
        )

        if not check_list:
            track.append(f"{r}|{c}")
        else:
            latest = check_list[-1]
            track.remove(latest)
            larray = latest.split(",")
            larray.append(f"{r}|{c}")
            track.append(",".join(larray))

    if c < len(mat[0]) - 1:
        c += 1
    else:
        r += 1
        c = 0
    return island(track, mat, r, c)


if not mat or not mat[0]:
    res = []
else:
    res = island([], mat, 0, 0)
print(f"Banyak Pulau: {len(res)}")
print(f"Luas Pulau: {' '.join([str(len(e)) for e in res]) if res else '0'}")
