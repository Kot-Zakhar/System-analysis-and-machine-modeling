from math import log
import numpy as np


def lehmer(a, m, R0):

    # m > a > 0
    R_prev = R0
    x = []
    x_set = set()
    while True:
        R_curr = a * R_prev % m
        x_i = R_curr / m
        R_prev = R_curr
        if x_i in x_set:
            # period = len(x) - x.index(x_i)
            break
        else:
            x_set.add(x_i)
            x.append(x_i)
    return x  # , period


def uniform_distribution(a, b, **kwargs):

    def uniform_kernel(a, b, R):
        return a + (b - a)*R

    R = lehmer(a=kwargs['A'], m=kwargs['M'], R0=kwargs['R0'])
    return [uniform_kernel(a, b, r) for r in R]


def normal_distribution(m, sigma, n=6, **kwargs):

    def normal_kernel(m, sigma, Ri_sum, n):
        return m + sigma * (Ri_sum - n/2) * ((12/n)**(1/2))

    R = lehmer(a=kwargs['A'], m=kwargs['M'], R0=kwargs['R0'])
    return [normal_kernel(m, sigma, sum(R[i-n: i]), n) for i in range(n, len(R), n)]


def exponential_distribution(lmbd, **kwargs):

    def exp_kernel(lmbd, R):
        return -(1/lmbd) * log(R)

    R = lehmer(a=kwargs['A'], m=kwargs['M'], R0=kwargs['R0'])
    return [exp_kernel(lmbd, r) for r in R]


def gamma_distribution(lmbd, eta, **kwargs):

    def gamma_kernel(lmbd, R, eta):
        return -1/lmbd * sum(map(log, R))

    R = lehmer(a=kwargs['A'], m=kwargs['M'], R0=kwargs['R0'])
    return [gamma_kernel(lmbd, R[i-eta: i], eta) for i in range(eta, len(R), eta)]


def triangular_distribution(a, b, **kwargs):

    def triangular_kernel(a, b, R1, R2):
        return a + (b-a)*min(R1, R2)

    R = lehmer(a=kwargs['A'], m=kwargs['M'], R0=kwargs['R0'])
    np.random.shuffle(R)
    return [triangular_kernel(a, b, R[i-1], R[i]) for i in range(1, len(R), 2)]


def simpson_distribution(a, b, **kwargs):

    def simpson_kernel(y, z):
        return y + z

    y = uniform_distribution(a/2, b/2, A=kwargs['A'], M=kwargs['M'], R0=kwargs['R0'])
    np.random.shuffle(y)
    z = uniform_distribution(a/2, b/2, A=kwargs['A'], M=kwargs['M'], R0=kwargs['R0'])
    np.random.shuffle(z)
    return [simpson_kernel(y_i, z_i) for y_i, z_i in zip(y, z)]


if __name__ == '__main__':
    # A 39999
    # m: 59999
    # R0: 19999
    a = 39999
    m = 59999
    R0 = 19999
    # print(uniform_distribution(1, 10, A=a, M=m, R0=R0)[0:20])
    # print(normal_distribution(3, 3, A=a, M=m, R0=R0)[0:20])
    # print(exponential_distribution(3, A=a, M=m, R0=R0)[0:20])
    # print(gamma_distribution(3, 10, A=a, M=m, R0=R0)[0:20])
    # print(triangular_distribution(3, 10, A=a, M=m, R0=R0)[0:20])
    print(simpson_distribution(3, 10, A=a, M=m, R0=R0)[0:20])
