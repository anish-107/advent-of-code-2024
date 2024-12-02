def monotonic(lis):
    if all(int(lis[i]) < int(lis[i+1]) for i in range(0, len(lis) - 1)) or all(int(lis[i]) > int(lis[i+1]) for i in range(0, len(lis) - 1)):
        return True
    return False


def adjacent(lis):
    if all(abs(int(lis[i]) - int(lis[i+1])) in {1, 2, 3} for i in range(0, len(lis) - 1)):
        return True
    return False

def is_safe(lis):
    return monotonic(lis) and adjacent(lis)

def is_safe_with_dampener(lis):
    """Check if the list can be safe by removing one element."""
    if is_safe(lis):
        return True

    # Try removing each element one by one
    for i in range(len(lis)):
        new_list = lis[:i] + lis[i + 1:]
        if is_safe(new_list):
            return True

    return False

count = 0

with open("input.txt", "r") as file:
    for line in file:
        numbers = line.split(" ")

        if is_safe_with_dampener(numbers):
                count += 1
        

print(count)


