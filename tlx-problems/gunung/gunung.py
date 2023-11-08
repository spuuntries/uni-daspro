n = int(input())
c = "*"

print(c)  # Sebagai n = 1


def gunung(n):
    if n >= 2:
        gunung(n - 1)
        print(c * n)
        print(c)  # Sebagai n = 1
        gunung(n - 1)


gunung(n)

"""
4
* <- 1

** <- 2
*  <- 2

*** <- 3
*   <- 3

** <- 2
*  <- 2

****  <- 4
*     <- 4

** <- 2
*  <- 2

*** <- 3
* <- 3

** <- 2
* <- 2

"""
