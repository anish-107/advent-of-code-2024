# Advent of Code: Day 1 - Historian Hysteria

## Problem Description

The Chief Historian has gone missing, and the Elvish Senior Historians need help to reconcile two lists of location IDs. These lists represent historically significant locations. Your task is to solve two puzzles by comparing the two lists.

### Part One: Calculating Total Distance

Given two lists of numbers, pair the smallest numbers from each list and measure the distance between them. Repeat this for all pairs, and find the sum of these distances.

### Example Input:

```
Left List   Right List
3           4
4           3
2           5
1           3
3           9
3           3
```

### Pairs and Distances:

| Pair      | Distance |
|-----------|----------|
| 1 and 3   | 2        |
| 2 and 3   | 1        |
| 3 and 3   | 0        |
| 3 and 4   | 1        |
| 3 and 5   | 2        |
| 4 and 9   | 5        |

### Total Distance:

```
2 + 1 + 0 + 1 + 2 + 5 = 11
```

### Solution for given Input:

**Answer:** 2367773

---

## Part Two: Calculating Similarity Score

This time, compute how often each number in the left list appears in the right list. Multiply each number by the count of its appearances and find the total similarity score.

### Example Input:

```
Left List   Right List
3           4
4           3
2           5
1           3
3           9
3           3
```

### Similarity Score Calculation:

1. **3 appears 3 times** in the right list: `3 * 3 = 9`
2. **4 appears 1 time** in the right list: `4 * 1 = 4`
3. **2 appears 0 times** in the right list: `2 * 0 = 0`
4. **1 appears 0 times** in the right list: `1 * 0 = 0`
5. **3 appears 3 times** again: `3 * 3 = 9`
6. **3 appears 3 times** again: `3 * 3 = 9`

### Total Similarity Score:

```
9 + 4 + 0 + 0 + 9 + 9 = 31
```

### Solution for given Input:

**Answer:** 21271939

---