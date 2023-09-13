import re

ans = int(input())
time = [int(e) for e in re.split(r" +", input())]
lmt = 35700  # 9.55
converted = 0

for i, t in enumerate(time):
    match i:
        case 0:
            converted += (t * 60) * 60
        case 1:
            converted += t * 60
        case 2:
            converted += t

pts = ans * 4 - (25 - ans)
diff = lmt - converted

if diff > 0:
    if ans >= 5:
        pts += (diff // (7.5 * 60)) * 2
else:
    if diff // 60 > 10:
        pts -= diff // (2.5 * 60)

if diff == 0:
    print("Owo menyelesaikan soal tepat waktu.")
else:
    absdiff = diff * -1 if diff < 1 else diff
    hour, rem = divmod(absdiff, 3600)
    minute, second = divmod(rem, 60)
    diffarr = [hour, minute, second]
    if diff > 0:
        print(
            f"Owo memiliki sisa waktu{f' {hour} jam' if hour > 0 else ''}{f' {minute} menit' if minute > 0 else ''}{f' {second} detik' if second > 0 else ''}."
        )
    else:
        print(
            f"Owo terlambat mengumpulkan selama{f' {hour} jam' if hour > 0 else ''}{f' {minute} menit' if minute > 0 else ''}{f' {second} detik' if second > 0 else ''}."
        )

if pts > 100:
    pts = 100
elif pts < 0:
    pts = 0

print(round(pts))
