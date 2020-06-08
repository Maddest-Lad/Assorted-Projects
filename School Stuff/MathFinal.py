# Problem 12


# Recursively Calculate Bonus Based On Years Since Hiring
def bonus(year) -> int:
    if year > 0:
        return bonus(year - 1) + 1500 * year
    else:
        return 0


# Returns 67500 To Represent Constant Yearly Salary
def salary() -> int:
    return 67500


total = 0
year = 1

while total < 1000000:
    total += salary() + bonus(year)
    year += 1

# (1,005,000 In The 11th Year)
print(total, year)
