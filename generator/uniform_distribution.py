

def lehmer(a, m, R0):

    # m > a > 0
    R_prev = R0
    x = []
    while True:
        R_curr = a * R_prev % m
        x_i = R_curr / m
        R_prev = R_curr
        if x_i in x:
            break
        else:
            x.append(x_i)
    return x


if __name__ == '__main__':
    print(lehmer(a=3, m=5, R0=1))
