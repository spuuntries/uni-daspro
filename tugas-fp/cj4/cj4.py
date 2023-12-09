import sys

op = int(input())
inputs = sys.stdin.read()
# This is stupid, input() will end on the existence of newline,
# but here, this'll only end at EOF: this way, we can encode the newlines as well.
res = ""

if op == 1:
    for c in inputs:
        encoded = str(bin("".join(chr(i) for i in range(128)).find(c)))[2:]
        padding = "0" * (8 - len(encoded)) if len(encoded) < 8 else ""
        res += padding + encoded
elif op == -1:
    slices = []
    for i in range(0, len(inputs), 8):
        slices.append(inputs[i : i + 8])
    for i, s in enumerate(slices):
        sarr = list(s)
        while True:
            head = sarr.pop(0)
            if head != "0":
                sarr.insert(0, head)
                break
        slices[i] = "".join(sarr)
    res = "".join(
        list(
            map(
                lambda c: dict([(str(bin(i))[2:], chr(i)) for i in range(128)])[c],
                slices,
            )
        )
    )


print(res, end="")
