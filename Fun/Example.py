def transform(message: str, operation: str):
    # Increment Char at index in operation
    if operation.startswith("S"):
        if operation[1].isdigit():
            index = int(operation[1])
            return message[:index] + chr(ord(message[index]) + 1) + message[index + 1:]

    # Rotate N Times
    elif operation.startswith("R"):
        # Rotate String N Times
        if operation[1].isdigit():
            times = int(operation[1])
            # With Exponent
            return message[times:] + message[:times]
        else:
            # Without Exponent
            return message[1:] + message[:1]

    # Dupplicate Letter at Index
    elif operation.startswith("D"):
        index = int(operation[1])
        return message[:index] + message[index] + message[index] + message[index:]

    # Swap Two Letters
    elif operation.startswith("T") and len(operation) < 4:
        index1, index2 = operation[1:3].split(",")
        return message[:int(index1)] + message[int(index2)] + message[int(index1) + 1:int(index2)] + message[int(index1)] + message[int(index2) + 1:]

    # Swap Two Groups of Letters
    elif operation.startswith("T"):
        index1, index2, = operation[1:3].split(",")
        group_size = int(operation[4])
        return message[:int(index1)] + message[int(index2):int(index2) + group_size] + message[int(index1) + group_size:] + message[int(index1):int(index1) + group_size]

    return message


def do_transform(message: str, operation: str):
    # variables
    operations = []
    current = ""

    # split operation into groups by letters
    for char in operation:
        current += char

        if char.isalpha():
            operations.append(current)
            current = ""
            
    operations.append(current)

    print(operations)

    # transform foreach operation
    while operations:
        print(message)
        print(operations.pop(0))
        message = transform(message, operations.pop(0))

    return message


do_transform("ThisIsAGreatString", "R6S6D7D2T25T75")
