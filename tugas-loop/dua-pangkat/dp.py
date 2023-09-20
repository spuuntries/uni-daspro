inp = int(input())
b = False

while inp > 1:
    if inp % 2 == 1:
        b = True
        break
    inp /= 2

if b:
    print("bukan")
else:
    print("ya")
