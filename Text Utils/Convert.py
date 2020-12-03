"""
Sam Harris
A Bundle of Methods For Decrypting Unknown Information
The Base Format Will Be Decimal
"""


def ascii_to_decimal(text: str) -> list:
    return [str(ord(i)) for i in text]

def hex_to_decimal(text: str) -> list:
    return 

print(ascii_to_decimal("test"))
