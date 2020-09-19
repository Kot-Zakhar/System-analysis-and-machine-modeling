import generator
import evaluator
from math import pi


def get_statistics(x, P):
    M = evaluator.math_expectation(x)
    D = evaluator.dispersion(x)
    sigma = evaluator.standard_deviation(x)

    return "\n".join([
        f'M: {M}',
        f'D: {D}',
        f'σ: {sigma}'
    ])


def process(a, m, R0):
    x, period = generator.lehmer(a=a, m=m, R0=R0)
    out_x = x[: 20] if len(x) > 20 else x
    print(f'X:', *out_x)
    print(get_statistics(x, period))
    evaluator.hist(x, bins=20)


def get_distribution_dict():
    return {
        "uniform": None,
        "normal": None,
        "exponential": None,
        "gamma": None,
        "triangular": None,
        "simpson": None
    }


def main():
    dist_dict = get_distribution_dict()
    dists = list(dist_dict.keys())
    while True:
        for i in range(len(dists)):
            print(f"{i+1}. {dists[i]};")
        exit_option = len(dists) + 1
        print("----------------")
        print(f"{exit_option}. exit.")
        option = int(input("Select the distribution: "))
        if option == exit_option:
            break



if __name__ == '__main__':
    main()


    # a = int(input('a: '))
    # m = int(input('m: '))
    # R0 = int(input('R0: '))
    # # a, m, R0 = 3, 5, 1
    # process(a=a, m=m, R0=R0)






