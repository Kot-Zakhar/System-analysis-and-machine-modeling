import matplotlib.pyplot as plt


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
