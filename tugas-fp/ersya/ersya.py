import string

inputs = input()
shift = int(input())
l_chr = string.ascii_lowercase
u_chr = string.ascii_uppercase
# PROBLEM STATES ONLY LOWERCASED ALPHABETICAL, WHY IS IT LIKE THIS. 😭

print(
    "".join(
        map(
            lambda c: l_chr[
                l_chr.index(c) + shift
                if l_chr.index(c) + shift < len(l_chr)
                else l_chr.index(c) + shift - len(l_chr)
            ]
            if c.islower()
            else u_chr[
                u_chr.index(c) + shift
                if u_chr.index(c) + shift < len(l_chr)
                else u_chr.index(c) + shift - len(l_chr)
            ]
            if c.isupper()
            else c,  # WHY
            inputs,
        )
    )
)
