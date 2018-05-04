import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

def lagrange(x, p, value):
    result = 0
    for i in range(5):
        current = 1
        for j in range(5):
            if i == j:
                continue
            current *= value - x[j]
        result += p[i] * current
    return result


def lagrange_to_string(x, p):
    for i in range(5):
        if i != 0 and p[i] >= 0:
            print("+ ", end="")
        print(str(p[i]) + " * ", end="")
        for j in range(5):
            if i == j:
                continue
            if x[j] > 0:
                print("(x - " + str(x[j]) + ")", end="")
            else:
                print("(x + " + str(-1 * x[j]) + ")", end="")
        if i != 4:
            if p[i + 1] > 0:
                print(" +")
            else:
                print(" -")



for i in range(5):
    print("input X" + str(i + 1) + ": ", end="")
    x.append(float(input()))
    print("input Y" + str(i + 1) + ": ", end="")
    y.append(float(input()))

p = []

for i in range(5):
    result = 1.0
    for j in range(5):
        if i == j:
            continue
        result *= (x[i] - x[j])
    p.append(1 / result * y[i])

lagrange_to_string(x, p)
t = np.arange(0., 5., 0.2)
plt.plot(t, lagrange(x, p, t), 'r', x, y, 'b')
plt.show()



