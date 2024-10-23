import numpy as np

L = 100

np.random.seed(34130)

# Generate random bits (0 or 1)
bit_sequence = np.random.randint(0, 2, L)


def main():
    print(bit_sequence)


if __name__ == "__main__":
    main()
