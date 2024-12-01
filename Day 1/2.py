# List and Variables used
list1 = []
list2 = []
sim_list = []
sum = 0

# Creating the input lists
with open("input.txt", "r") as file:
    for line in file:
        numbers = line.split("   ")
        
        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))

# Counting similarity score
for num in list1:
    count = 0
    for number in list2:
        if number == num:
            count = count + 1

    sim_list.append(num * count)
    sum = sum + (num * count)


# Print Result
print(sum)