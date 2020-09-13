from scipy import optimize


def lehmer(param):

    # m > a > 0
    R_prev = param[2]
    x = []

    while True:
        R_curr = param[0] * R_prev % param[1]
        x_i = R_curr / param[1]
        R_prev = R_curr
        if x_i in x:
            period = len(x) - x.index(x_i)
            break
        else:
            x.append(x_i)
    return -period


if __name__ == '__main__':
    # print(lehmer(a=3, m=5, R0=1))
    # x, period = lehmer(a=5, m=4096, R0=2451)
    param = [4, 4096, 2451]
    res = optimize.minimize(lehmer, param)
    print(res.x)
