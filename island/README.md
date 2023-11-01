# **ISLAND** 🏝️

The classic flood fill island problem, solved in the dumbest manner possible. 🙏

Given a 2D matrix of land and sea (represented by >0 and 0), determine the number of islands, max island size, and min island size.

e.g. given input:

```
0 1 0 0
1 1 0 1
0 0 0 1
1 0 0 0
```

it'd output:

```
3 islands
max 3
min 1
```

My prof. gave an explainer on flood fill to solve this, but I didn't really understand it lol.

**But,** she asked for just, recursion, of _any_ form, in the solution.

So the solution is really just an iterative solution turned recursive. :p

## **Algorithm**

Here's a high-level explainer on how it works:

1. Initialize a data structure to keep track of the islands.

2. Iterate over each cell in the grid. For each cell, do the following:

   If the cell is part of an island, check:

   **a. If the cell is not adjacent to any existing islands**, start a new island with this cell.

   **b. If the cell is adjacent to an existing island**, add it to the appropriate island in the data structure.

3. After all cells in the grid have been processed, the data structure contains all the islands, with each entry representing an island and its constituent cells.

## **O(n)?**

_Afaik_ the big O _should_ be `O(n*m)` with `n` as number of cells in the matrix and `m` is the maximum number of operations performed for each cell in the worst-case scenario, i.e., the size of the largest island.

e.g. Given

```
0 0 0 0 0
0 1 1 0 0
1 0 0 0 1
1 1 1 0 1
0 0 0 0 0
```

the complexity would be `O((5*5)*4)`.
