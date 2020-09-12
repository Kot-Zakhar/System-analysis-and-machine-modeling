from generator import uniform_distribution
import evaluator


if __name__ == '__main__':
    # a = int(input('a: '))
    # m = int(input('m: '))
    # R0 = int(input('R0: '))
    # x = uniform_distribution.lehmer(a=3, m=5, R0=1)
    x = uniform_distribution.lehmer(a=5, m=4096, R0=2451)
    print(len(x))
    print('m:', evaluator.math_expectation(x))
    print('D:', evaluator.dispersion(x))
    print('σ:', evaluator.standard_deviation(x))
    evaluator.hist(x, bins=20)
