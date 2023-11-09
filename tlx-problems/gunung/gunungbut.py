# v2, iterative
# We use a stack here to emulate the behaviour of a recursive call.
# P.S. I genuinely despised this solution, istg. Writing the docs was even worse.
n = int(input())


def gunung(n):
    stack = [(n, False)]
    # This initializes the stack with n because we'll be recursing from there,
    # False indicates recursion.
    while stack:  # We stop when stack is empty
        n, visited = stack.pop()  # Take the last entry in the stack, remove it
        if n >= 2:
            if visited:
                # Basically, if visited is set, which means we're on a "local" peak, we're supposed to repeat on n-1 first
                print("*" * n)
                stack.append((n - 1, False))
            else:  # This is used to recurse all the way down to the lowest level of recursion
                stack.append((n, True))
                stack.append((n - 1, False))
        else:  # This only gets called once we're on the lowest level of the recursion, i.e., before or after a peak
            print("*")


gunung(n)

# SAMPLE CASE
# This is a bit hard to explain in text, but I'm gonna try my best here:
"""
For example, if n = 4, and c = "*"

First, we initialize the stack with [(4, False)]

iteration                   stack
                            [(4, False)]

-----

1                           []
    (4, False) 
        ^-- Visited is not set and we're still >=2, 
            so we recurse down to the lowest level 
            by setting [... (n, True), (n-1, False)]

>>>                         [(4, True), (3, False)]

------

2                           [(4, True)]
    (3, False)
        ^-- Same deal, recurse down, 
            setting [... (n, True), (n-1, False)]

>>>                         [(4, True), (3, True), (2, False)]

------

3                           [(4, True), (3, True)]
    (2, False)
        ^-- Same, recurse.

>>>                         [(4, True), (3, True), (2, True), (1, False)]

------

4                           [(4, True), (3, True), (2, True)]
    (1, False)
        ^-- We're at <2!
            So at <2, we print c.

    *

>>>                         [(4, True), (3, True), (2, True)]

------

5                           [(4, True), (3, True)]
    (2, True)
        ^-- Visited is set!
            When visited is set,
            we print c * n, then set
            [... (n-1, False)]
    
    *
    **

>>>                         [(4, True), (3, True), (1, False)]

------

6                           [(4, True), (3, True)]
    (1, False)
        ^-- <2! Print c.

    *
    **
    *

>>>                         [(4, True), (3, True)]

------

7                           [(4, True)]
    (3, True)
        ^-- Visited is set! 
            Print c * n, then set
            [... (n-1, False)]

    *
    **
    *
    ***

>>>                         [(4, True), (2, False)]

------

8                           [(4, True)]
    (2, False)
        ^-- This is both >=2 and visited not set,
            recurse, set [... (n, True), (n-1, False)]

    *
    **
    *
    ***

>>>                         [(4, True), (2, True), (1, False)]

------

9                           [(4, True), (2, True)]
    (1, False)
        ^-- <2! Print c.
    
    *
    **
    *
    ***
    *

>>>                         [(4, True), (2, True)]

------

10                          [(4, True)]
    (2, True)
        ^-- Visited is set,
            so print c * n, then set
            [... (n-1, False)]
    
    *
    **
    *
    ***
    *
    **

>>>                         [(4, True), (1, False)]

------

11                          [(4, True)]
    (1, False)
        ^-- <2, print c.

    *
    **
    *
    ***
    *
    **
    *

>>>                         [(4, True)]

------

12                          []
    (4, True)
        ^-- Visited set,
            print c * n,
            set [... (n-1, False)]
    *
    **
    *
    ***
    *
    **
    *
    ****

>>>                         [(3, False)]

------

13                          []
    (3, False)
        ^-- >=2 and visited not set,
            recurse, set [... (n, True), (n-1, False)]

    *
    **
    *
    ***
    *
    **
    *
    ****

>>>                         [(3, True), (2, False)]

------

14                          [(3, True)]
    (2, False)
        ^-- same deal, recurse.

    *
    **
    *
    ***
    *
    **
    *
    ****

>>>                         [(3, True), (2, True), (1, False)]

------

15                          [(3, True), (2, True)]
    (1, False)
        ^-- <2, print c.

    *
    **
    *
    ***
    *
    **
    *
    ****
    *

>>>                         [(3, True), (2, True)]

------

16                          [(3, True)]
    (2, True)
        ^-- Visited set,
            print c * n,
            set [... (n-1, False)]
    
    *
    **
    *
    ***
    *
    **
    *
    ****
    *
    **

>>>                         [(3, True), (1, False)]

------

17                          [(3, True)]
    (1, False)
        ^-- <2, print c.

        
    *
    **
    *
    ***
    *
    **
    *
    ****
    *
    **
    *

>>>                         [(3, True)]

------

18                          []
    (3, True)
        ^-- Visited set,
            print c * n,
            set [... (n-1, False)]

        
    *
    **
    *
    ***
    *
    **
    *
    ****
    *
    **
    *
    ***

>>>                         [(2, False)]

------

19                          []
    (2, False)
        ^-- >=2 and visited not set,
            recurse, set [... (n, True), (n-1, False)]

    *
    **
    *
    ***
    *
    **
    *
    ****
    *
    **
    *
    ***

>>>                         [(2, True), (1, False)]

------

20                          [(2, True)]
    (1, False)
        ^-- <2, print c.
    
    *
    **
    *
    ***
    *
    **
    *
    ****
    *
    **
    *
    ***
    *

>>>                         [(2, True)]

------

21                          []
    (2, True)
        ^-- Visited set, print c * n,
            set [... (n-1, False)]
    
    *
    **
    *
    ***
    *
    **
    *
    ****
    *
    **
    *
    ***
    *
    **

>>>                         [(1, False)]

------

22                          []
    (1, False)
        ^-- <2, print c.
    
    *
    **
    *
    ***
    *
    **
    *
    ****
    *
    **
    *
    ***
    *
    **
    *

>>>                         []

------

END                         []
    Stack is empty, we stop. 
    🎉🎉🎉
    
    *
    **
    *
    ***
    *
    **
    *
    ****
    *
    **
    *
    ***
    *
    **
    *
"""
