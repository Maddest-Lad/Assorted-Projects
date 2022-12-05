from collections import OrderedDict

def get_keys(file: str) -> OrderedDict:
    out = OrderedDict()
    with open(file, 'r') as f:
        lines = f.read().split("\n")
        for line in lines:
            out[line.split(" = ")[0]] = line.split(" = ")[1]

    return out


def main():
    title_1 = get_keys('title_1.keys')
    title_2 = get_keys('title_2.keys')

    i = 0
    for key in title_1:
        if key in title_2:
            i += 1
    print(i, "keys in common")

    od = OrderedDict(sorted({**title_1, **title_2}.items(), key=lambda t: t[0]))

    with open("title.keys", 'w') as file:
        for key, value in od.items():
            file.write(f"{key} = {value}\n")


if __name__ == '__main__':
    main()
