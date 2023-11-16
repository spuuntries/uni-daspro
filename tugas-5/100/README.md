# **In all seriousness, here's why there are so many damn implementations:**

## **A writeup on my programming assignment lmfao**

### _(tl;dr is: I was in way over my head with this lol, big sadge)_

## Problem Description:

Given `p` and `t`, find number of possible 1−6 integer combinations to, when summed with `p`, reach 100, without having an increment that hits `t`.

## _My_ interpretation:

A major requirement to fulfill for this set of problems, `tugas-5`, was to do things _recursively_. _I_ interpreted this as a challenge to make it as recursive as possible, where, y'know, we shouldn't rely on `for` and `while`s, but I'll quickly realize that (as you'll see below), that's not really the case.

At least, that wasn't the hard bit. <img src="./wu-assets/Harold1.png" width="24px" height="24px" alt=":hide_the_pain:">

## So wat do?

To calculate all possible combinations, one has to track the current array of combinations and pass that to the next frame in the call stack.

Do you know what this means?  
_EXPONENTIAL GROWTH_ on the call stack, this can lead to a multitude of issues, namely _everything_. (That's got to do with memory, at least.)

Now, I knew this, but what _I_ interpreted from the problem definition, was to get _all_ combinations, and not the total number of _possible_ combinations. So, `sys.setrecursionlimit()` it is.

I realized halfway through that life would've been a much better and easier time had I taken this other route. Buuuuuut, being the egotisitical prick that I am, I tried to force my way through _anyway_, mostly because I alrd did my initial implementation (see [./100.py](./100.py)), and that it just, didn't "click" in my head to do this.

So, [after my initial implementation broke down and cried on the side of the road](#below-is-my-initial-implementation-uses-a-lot-of-memory-and-prime-example-of-what-i-meant-by-exponential-see-the-lines-that-deallocated-700-ish-mibs-lol), I tried again. The first thought that came to mind was reducing the number of memory overheads, but how?

So I did what everyone does when they get stuck, they _steal_.  
Jk, but one of my classmates, Kevin, was working on the same problem and he found an algorithm to just, get the number of possible combinations. So he came to me to confirm his programming bit, and I confirmed that it was all good, so he sent it off, and got AC.

Now, I _could_, probably should tbh in hindsight, have done his approach, which is fine in theory, I've already put this to practice in [kursi](../kursi/), but as I said above, I was way too egotistical for this.

But anyway, what I noticed, was that, his thingy, didn't use as much memory, because it didn't track a lot of parameters _(fewer things to track = less memory use? Who would've thought? Crazy amirite)_, so I tried to do the same with my implementation.

I did this, by _not_ passing all of, everything; current sequence, current result array, current memo state, etc etc.; to the next recursive call.
Instead, what I did was I only passed the current result to the next frame, and pass the `p`, current index, `t`, and the 100.

This ["worked"](#below-is-second-attempt-when-we-try-to-get-all-possible-combinations-but-reducing-number-of-memory-use-by-not-tracking-so-damn-many-function-parameters), and reduced the memory use, by a l o t. But as I quickly found out (by submitting it to DOMJudge), this wasn't going to be enough.

<img src="./wu-assets/bjir.jpg" width="240px" height="240px" alt="Pake Nanya" style="border-radius: 2em">

So wat happun nex? Do me keep tryin me bes? Do me push thru to becom da bes? Na broh, we cave in lmfao.

So I caved in, gave up on finding all possible combinations whilst staying low on memory footprint, and just, worked on that "find number of possibilities" algorithm.

After a while of trying, I arrived on a similar flow to Kevin's regardless of what I did, so I just grabbed his and added memoization + QoL to reduce the footprint even further.

## Well damn, disappointment.

Life isn't all sunshine and rainbows, sometimes enough is... enough. If everyone got everything they wanted in life, there would be no sadness. But to live is to experience life in its entirety, to accept life for all of its beauty and ugly. [To end suffering, is to end desire and attachment.](https://www.youtube.com/watch?v=ECYT7npIeMY)

Why is this section here? I don't know.

<img src="./wu-assets/hooni.jpg" width="512px" height="512px" alt="Pake Nanya" style="border-radius: 2em">

---

## Here are my benchmark logs for the above:

### Before memo:

```
(.venv) PS C:\Users\kek\projects\uni-daspro\tugas-5\100> python -m memory_profiler 100butbut.py
90 -1
Ada 492 cara nih!
Filename: 100butbut.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4   22.051 MiB   22.047 MiB        3001   @profile
     5                                         def ways(p, t):
     6   22.051 MiB    0.000 MiB        3001       if p == 100:
     7   22.051 MiB    0.000 MiB         492           return 1
     8   22.051 MiB    0.000 MiB        2509       elif p > 100:
     9   22.051 MiB    0.000 MiB        2009           return 0
    10   22.051 MiB    0.000 MiB         500       elif p == t:
    11                                                 return 0
    12                                             else:
    13   22.051 MiB    0.000 MiB         500           res = 0
    14   22.051 MiB    0.000 MiB        3500           for i in range(1, 7):
    15   22.051 MiB    0.004 MiB        3000               res += ways(p + i, t)
    16   22.051 MiB    0.000 MiB         500           return res
```

### After Memo: => Final implementation:

```
(.venv) PS C:\Users\kek\projects\uni-daspro\tugas-5\100> python -m memory_profiler 100butbut.py
90 -1
Ada 492 cara nih!
Filename: 100butbut.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    19   21.816 MiB   21.816 MiB          61   @profile
    20                                         def ways(p, t, memo={}):
    21   21.816 MiB    0.000 MiB          61       if p == 100:
    22   21.816 MiB    0.000 MiB           6           return 1
    23   21.816 MiB    0.000 MiB          55       elif p > 100 or p == t:
    24   21.816 MiB    0.000 MiB          15           return 0
    25   21.816 MiB    0.000 MiB          40       elif p in memo:
    26   21.816 MiB    0.000 MiB          30           return memo[p]
    27                                             else:
    28   21.816 MiB    0.000 MiB          10           res = 0
    29   21.816 MiB    0.000 MiB          70           for i in range(1, 7):
    30   21.816 MiB    0.000 MiB          60               res += ways(p + i, t, memo)
    31   21.816 MiB    0.000 MiB          10           memo[p] = res
    32   21.816 MiB    0.000 MiB          10           return res
```

### Below is second attempt, when we try to get all possible combinations, but reducing number of memory use by not tracking so damn many function parameters:

```
(.venv) PS C:\Users\kek\projects\uni-daspro\tugas-5\100> python -m memory_profiler 100but.py
90 -1
Ada 492 cara nih!
Filename: 100but.py
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    14   22.363 MiB   22.355 MiB        6001   @profile
    15                                         def count_ways(p, t, i=1, target=100):
    16   22.363 MiB    0.004 MiB        6001       if p == target:
    17   22.363 MiB    0.000 MiB         492           return [[]] if i == 1 else []
    18   22.363 MiB    0.000 MiB        5509       elif p > target or p == t or i > 6:
    19   22.363 MiB    0.000 MiB        2509           return []
    20                                             else:
    21   22.363 MiB    0.004 MiB        3000           ways = rprepend(i, count_ways(p + i, t, 1)) + count_ways(p, t, i + 1)
    22   22.363 MiB    0.000 MiB        3000           return ways
```

### Below is my initial implementation, uses a lot of memory and prime example of what I meant by "exponential" (see the lines that deallocated 700-ish MiBs lol):

```
(.venv) PS C:\Users\kek\projects\uni-daspro\tugas-5\100> python -m memory_profiler 100.py
90 -1
Ada 492 cara nih!
Filename: 100.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    13   29.598 MiB   26.047 MiB        1024   @profile
    14                                         def ways(p, t, memo={}, i=1, c=[], res=[], adj=False):
    15   29.598 MiB    0.121 MiB        1024       if p == t:
    16                                                 return []
    17                                             # Check if value is already in memo
    18   29.602 MiB    2.746 MiB        1024       if str((p, t, i, tuple(c), tuple(res), adj)) in memo:
    19                                                 return memo[str((p, t, i, tuple(c), tuple(res), adj))]
    20
    21   29.602 MiB    0.051 MiB        1024       c = c.copy()
    22   29.602 MiB    0.410 MiB        1024       res = res.copy()
    23                                             # To initialize, we'll basically recurse +i until we hit t
    24   29.602 MiB    0.004 MiB        1024       if t > 0:
                                                    ... truncated
    68   29.602 MiB    0.000 MiB        1024           if p + sum(c) != 100:
    69   29.605 MiB -757.941 MiB         512               return ways(p, t, memo, i, c + [i], res)
    70                                                 else:
    71   29.602 MiB    0.215 MiB         512               res.append(c.copy())
    72   29.602 MiB    0.004 MiB         512               last = c.pop()
    73   29.602 MiB    0.004 MiB         512               if not c:
    74   29.602 MiB    0.000 MiB           1                   memo[str((p, t, i, tuple(c), tuple(res), adj))] = res
    75   29.602 MiB    0.000 MiB           1                   return res
    76   29.590 MiB    0.000 MiB         511               new_last = c.pop()
    77   29.605 MiB -744.086 MiB         511               return ways(p, t, memo, i, c + [new_last + 1], res)
```
