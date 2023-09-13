# Bruteforce, slow.

from math import factorial

inp = list(str(factorial(int(input()))))
sum = 0

inp.reverse()

for e in inp:
    if e == "0":
        sum += 1
    else:
        break

print(sum)
if sum % 4 == 0:
    print("Tuker dulu Rink!")
else:
    print("Gas pol rem blong, Rink!")
