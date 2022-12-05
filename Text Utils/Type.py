
with open("input.txt", "r") as f:
    text = f.read().split("\n")
    x = True
    for line in text:

        if x:
            print(line + ",", end="")
            x = not x
        else:
            x = not x

