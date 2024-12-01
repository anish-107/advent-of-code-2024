# Lists and Variables used
list1 = []
list2 = []
dis_list = []
sum = 0

# Reading the File
with open("input.txt", "r") as file:
    for line in file:
        numbers = line.split("   ")

        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))

# Sort the files
list1.sort()
list2.sort()

# Create list for distances
for i in range(0, len(list1)):
    dis_list.append(abs(list1[i] - list2[i]))
    sum = sum + abs(list1[i] - list2[i])

# Print Result
print(sum)