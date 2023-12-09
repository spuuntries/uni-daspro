import math

inputs = list(map(int, input().split()))

gcd = math.gcd(*inputs)
if len(str(gcd)) % 2 == 0:
    print("Yey brankas berhasil dibuka :D")
else:
    print("Yah gagal :(")
