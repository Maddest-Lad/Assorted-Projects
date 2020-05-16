import random

lines = []

with open("Grattitude_List.txt", encoding='utf-8') as source:
    for line in source:
        if line is not "\n":
            lines.append(line.split(". ")[1])

print(random.choice(lines))
