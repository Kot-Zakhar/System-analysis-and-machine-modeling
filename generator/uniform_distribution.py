

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
            period = len(x) - x.index(x_i)
            break
        else:
            x_set.add(x_i)
            x.append(x_i)
    return x, period


if __name__ == '__main__':
    print(lehmer(a=3, m=5, R0=1))
