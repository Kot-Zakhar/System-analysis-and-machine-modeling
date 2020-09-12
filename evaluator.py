import matplotlib.pyplot as plt
from math import pi


def hist(x, bins=20):
    plt.hist(x, bins=bins, ec='black')
    plt.show()


def math_expectation(x):
    return sum(x)/len(x)


def dispersion(x):
    n = len(x)
    m = math_expectation(x)
    return sum([(xi - m)**2 for xi in x])/(n-1)


def standard_deviation(x):
    return dispersion(x)**(1/2)


def indirect_signs_check(x, error):
    n = len(x) if (len(x) % 2 == 0) else (len(x) - 1)
    k = 0
    for i in range(0, n-1, 2):
        if x[i]**2 + x[i+1]**2 < 1:
            k += 1

    if 2*k/n - pi/4 < error:
        return True
    return False

