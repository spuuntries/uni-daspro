# v2, pake algo.

inp = int(input())
sum = 0
i = 1

while True:
    r = inp // (5**i)
    if r < 1:
        break
    sum += r
    i += 1

print(sum)
if sum % 4 == 0:
    print("Tuker dulu Rink!")
else:
    print("Gas pol rem blong, Rink!")
