def monotonic(lis):
    if all(int(lis[i]) < int(lis[i+1]) for i in range(0, len(lis) - 1)) or all(int(lis[i]) > int(lis[i+1]) for i in range(0, len(lis) - 1)):
        return True
    return False


def adjacent(lis):
    if all(abs(int(lis[i]) - int(lis[i+1])) in {1, 2, 3} for i in range(0, len(lis) - 1)):
        return True
    return False

count = 0

with open("input.txt", "r") as file:
    for line in file:
        numbers = line.split(" ")

        if monotonic(numbers):
            if adjacent(numbers):
                count += 1
        

print(count)