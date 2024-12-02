# Red-Nosed Reports Puzzle Solution (Day 2)

## Problem Description

You are helping engineers analyze unusual data from the Red-Nosed reactor. Each report contains a list of numbers called "levels," and the goal is to determine if the reports are **safe**. A report is safe if it meets the following conditions:

1. The levels must either be all **increasing** or all **decreasing**.
2. The difference between any two adjacent levels must be **at least 1** and **at most 3**.

### Example Reports:

```
7 6 4 2 1  → Safe (all decreasing by 1 or 2)
1 2 7 8 9  → Unsafe (difference of 5 between 2 and 7)
9 7 6 2 1  → Unsafe (difference of 4 between 6 and 2)
1 3 2 4 5  → Unsafe (not fully increasing or decreasing)
8 6 4 4 1  → Unsafe (difference is 0 between two 4s)
1 3 6 7 9  → Safe (all increasing by 1, 2, or 3)
```

### Results for Part 1:
Only 2 reports from the example above are considered **safe**.

---

## Part 1: Finding Safe Reports

You must check if the reports follow the rules for being safe. If a report is monotonic (always increasing or always decreasing) and the difference between adjacent levels is between 1 and 3, it is safe.

### Example:

| Report          | Safe?              | Reason                                     |
|-----------------|--------------------|--------------------------------------------|
| 7 6 4 2 1       | Yes                | Decreasing, differences within 1-3         |
| 1 2 7 8 9       | No                 | Difference between 2 and 7 is 5 (too large)|
| 9 7 6 2 1       | No                 | Difference between 6 and 2 is 4 (too large)|
| 1 3 2 4 5       | No                 | Not fully increasing or decreasing         |
| 8 6 4 4 1       | No                 | Adjacent 4s have a difference of 0         |
| 1 3 6 7 9       | Yes                | Increasing, differences within 1-3         |

In the real dataset, **299 reports** were found to be safe.

---

## Part 2: Using the Problem Dampener

Now, the engineers introduce a **Problem Dampener** that can tolerate one bad level in the report. If removing a single level makes the report safe, it should still be counted as safe.

### Updated Example:

| Report          | Safe with Dampener? | Reason                                      |
|-----------------|---------------------|---------------------------------------------|
| 7 6 4 2 1       | Yes                 | Safe without removing any level             |
| 1 2 7 8 9       | No                  | Unsafe even if one level is removed         |
| 9 7 6 2 1       | No                  | Unsafe even if one level is removed         |
| 1 3 2 4 5       | Yes                 | Safe if the second level (3) is removed     |
| 8 6 4 4 1       | Yes                 | Safe if one of the 4s is removed            |
| 1 3 6 7 9       | Yes                 | Safe without removing any level             |

### Results for Part 2:
Using the Problem Dampener, more reports are safe. **364 reports** are considered safe in total.

---

## Summary of Results

1. **Part 1 (No Dampener):** 299 safe reports.
2. **Part 2 (With Dampener):** 364 safe reports.

By using the Problem Dampener, 65 additional reports were deemed safe.