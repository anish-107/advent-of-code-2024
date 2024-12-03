import re

with open("input.txt", "r") as file:
    content = file.read()

enabled = True
result = 0

index = 0

while index < len(content):
    if content[index:index+4] == "do()":
        enabled = True
        index = index + 4
    elif content[index:index+7] == "don't()":
        enabled = False
        index = index + 7
    elif content[index:index+3] == "mul":
        match = re.match(r"mul\((\d+),\s*(\d+)\)", content[index:])
        if match:
            x = int(match.group(1))
            y = int(match.group(2))
            if enabled:
                result += x * y
            index += len(match.group(0)) 
        else:
            index += 1 
    else:
            index += 1
print(result)
print(match)