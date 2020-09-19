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


def uniform_distribution(a, b, **args):
    def uniform_generation_func(a, b, R):
        return a + (b - a)*R
    R = lehmer(a=args['A'], m=args['M'], R0=args['R0'])
    return [uniform_generation_func(a, b, r) for r in R]


def normal_distribution(m, sigma, n=6, **args):
    def normal_generation_func(m, sigma, Ri_sum, n):
        return m + sigma * (Ri_sum - n/2) * ((12/n)**(1/2))
    R = lehmer(a=args['A'], m=args['M'], R0=args['R0'])
    return [normal_generation_func(m, sigma, sum(R[i-n: i]), n) for i in range(n, len(R), n)]


if __name__ == '__main__':
    # A 39999
    # m: 59999
    # R0: 19999
    # print(uniform_distribution(1, 10, A=39999, M=59999, R0=19999))
    print(normal_distribution(3, 3, A=39999, M=59999, R0=19999))
