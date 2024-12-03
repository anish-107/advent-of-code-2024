# Day 3: Mull It Over  

The North Pole Toboggan Rental Shop's computers are having problems, and the Historians are searching the warehouse for answers. The shopkeeper asks you to check why their computer program is malfunctioning. The program's goal is simple: **multiply numbers**, but the memory is corrupted.  

## Part One: Finding Valid Multiplications  

The program uses instructions like `mul(X,Y)`, where `X` and `Y` are numbers with 1 to 3 digits. For example:  
- `mul(44,46)` calculates `44 * 46 = 2024`  
- `mul(123,4)` calculates `123 * 4 = 492`  

However, the memory also contains **invalid characters**. You should only consider valid `mul()` instructions. Invalid sequences include:  
- `mul(4*`  
- `mul(6,9!`  
- `mul ( 2 , 4 )` (notice the spaces)

### Example  

Given this corrupted memory:  
```
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
```  

Only the following are valid instructions:  
1. `mul(2,4)` → 2 * 4 = 8  
2. `mul(3,7)` → 3 * 7 = 21  
3. `mul(11,8)` → 11 * 8 = 88  
4. `mul(8,5)` → 8 * 5 = 40  

### Result Calculation  

Adding these results together:  
```
8 + 21 + 88 + 40 = 161
```  

The program adds up all the valid multiplication results.  

**Puzzle answer was: 188741603**  

---

## Part Two: Handling `do()` and `don't()` Instructions  

You now notice that some instructions enable or disable `mul()` operations:  
- **`do()`**: Enables future `mul()` instructions.  
- **`don't()`**: Disables future `mul()` instructions.  

At the start, `mul()` instructions are enabled by default. The most recent `do()` or `don't()` determines whether `mul()` instructions will work.  

### Example  

Consider this corrupted memory:  
```
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
```  

The following happens:  
1. `mul(2,4)` → 2 * 4 = 8 (enabled)  
2. `mul(3,7)` → 3 * 7 = 21 (enabled)  
3. `don't()` → Disables all `mul()` instructions  
4. `mul(5,5)` → Skipped (disabled by `don't()`)  
5. `mul(32,64)` → Skipped (disabled)  
6. `do()` → Enables `mul()` again  
7. `mul(11,8)` → Skipped (before `do()`)  
8. `mul(8,5)` → 8 * 5 = 40 (enabled)  

### Result Calculation  

Only valid and enabled `mul()` operations are added:  
```
8 + 40 = 48
```  

**Puzzle answer was: 67269798**  

---  