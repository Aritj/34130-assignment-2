import numpy as np

# Set seed to 34130
np.random.seed(34130)

# Generate random bits (0 or 1)
L = 100
bits_OOK = np.random.randint(0, 2, L)


def main():
    print(bits_OOK)


if __name__ == "__main__":
    main()
