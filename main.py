import generator
import evaluator
from math import pi


def get_statistics(x, P):
    M = evaluator.math_expectation(x)
    D = evaluator.dispersion(x)
    sigma = evaluator.standard_deviation(x)
    k2_on_4 = evaluator.indirect_signs_check(x)
    L = len(x)

    return "\n".join([
        f'M: {M}',
        f'D: {D}',
        f'σ: {sigma}',
        f'2K/4: {k2_on_4}',
        f'pi/4: {pi/4}',
        f'L: {L}',
        f'P: {P}'
    ])


def process(a, m, R0):
    x, period = generator.lehmer(a=a, m=m, R0=R0)
    out_x = x[: 20] if len(x) > 20 else x
    print(f'X:', *out_x)
    print(get_statistics(x, period))
    evaluator.hist(x, bins=20)

# 39999
# m: 59999
# R0: 19999
if __name__ == '__main__':
    a = int(input('a: '))
    m = int(input('m: '))
    R0 = int(input('R0: '))
    # a, m, R0 = 3, 5, 1
    process(a=a, m=m, R0=R0)
    print()
    a, m, R0 = evaluator.find_parameters()
    print(f'a: {a}\nm: {m}\nR0: {R0}')
    process(a=a, m=m, R0=R0)




