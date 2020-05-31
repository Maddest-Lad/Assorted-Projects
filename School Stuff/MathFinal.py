import matplotlib.pyplot as plt

total = 0
loop_count = 0

salary = 67500
bonus = 1500

y = []
x = [k for k in range(15)]

for i in range(15):
    total += salary + bonus
    bonus += 1500

    y.append(total)


plt.plot(x, y)

plt.xlabel('years')
plt.ylabel('Millions earned')

plt.title('Mayas Earnings Over ~14 Years')

plt.show()