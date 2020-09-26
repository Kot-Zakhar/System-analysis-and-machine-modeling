import generator
import evaluator
from math import pi


LEHMER_PARAMS = {
    'A': 39999,
    'M': 59999,
    'R0': 19999
}


def get_statistics(x):
    M = evaluator.math_expectation(x)
    D = evaluator.dispersion(x)
    sigma = evaluator.standard_deviation(x)

    return "\n".join([
        f'M: {M}',
        f'D: {D}',
        f'σ: {sigma}'
    ])


def process(dist_dict, chosen_dist):
    generate_distribution = dist_dict[chosen_dist]['generator']
    params = dist_dict[chosen_dist]['params']
    params_dict = {}
    print("Input parameters.")
    for parameter in params:
        params_dict[parameter] = int(input(f'{parameter}: '))

    params_dict.update(LEHMER_PARAMS)
    x = generate_distribution(**params_dict)
    out_x = x[: 20] if len(x) > 20 else x
    print(f'X:', *out_x)
    print(get_statistics(x))
    evaluator.hist(x, bins=20)


def get_distribution_dict():
    return {
        "uniform": {
            'generator': generator.uniform_distribution,
            'params': ['a', 'b']
        },
        "normal": {
            'generator': generator.normal_distribution,
            'params': ['m', 'σ']
        },
        "exponential": {
            'generator': generator.exponential_distribution,
            'params': ['λ']
        },
        "gamma": {
            'generator': generator.gamma_distribution,
            'params': ['λ', 'η']
        },
        "triangular": {
            'generator': generator.triangular_distribution,
            'params': ['a', 'b']
        },
        "simpson": {
            'generator': generator.simpson_distribution,
            'params': ['a', 'b']
        }
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
        if (option <= len(dists)) and (option > 0):
            process(dist_dict=dist_dict, chosen_dist=dists[option-1])


if __name__ == '__main__':
    main()






