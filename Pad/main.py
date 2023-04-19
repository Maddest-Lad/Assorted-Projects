with open("headlines") as file:
    for line in file.read().split("\n"):
        print("<li>", line.strip(), "</li>")
