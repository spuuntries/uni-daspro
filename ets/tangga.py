n = int(input())
inputs = []


def is_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


for i in range(n):
    inputs.append([int(e) if is_int(e) else e for e in input().split()])

for i, e in enumerate(inputs):
    dot = ".." if (i + 1) % 2 == 0 else "."
    width = e[0] - len(dot)
    if width % 2 != 0:
        print("Invalid width!")
        break
    pad_w = width // 2
    print(f"Tangga {i+1}:")
    match e[2]:
        case "right":
            for i in range(e[1]):
                print(f"{' '*i}{'#'*pad_w}{dot}{'#'*pad_w}")
        case "left":
            for i in range(e[1], 0, -1):
                print(f"{' '*i}{'#'*pad_w}{dot}{'#'*pad_w}")
