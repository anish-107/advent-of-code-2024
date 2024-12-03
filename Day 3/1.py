import re

with open("input.txt", "r") as file:
    content = file.read()

pattern = r"mul\((\d+),\s*(\d+)\)"

calls = re.findall(pattern, content)

result = 0

for call in calls:
    product = int(call[0]) * int(call[1])
    result += product

print(result)