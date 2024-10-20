import numpy as np

L = 100


def generate_bit_sequence(L, seed=34130):
    # Set seed for reproducibility
    np.random.seed(seed)

    # Generate random bits (0 or 1)
    bit_sequence = np.random.randint(0, 2, L)

    return bit_sequence


def main():
    print(generate_bit_sequence(L))


if __name__ == "__main__":
    main()
