import numpy as np

# Given data
test_SpS = 4
test_L = 3
test_bits = np.array([1, 2, 3])


def main():
    # Repeating the bits SpS times
    test_wave = np.tile(test_bits, (test_SpS, 1))

    # Reshaping the array into a 1D vector
    test_wave = test_wave.reshape(test_SpS * test_L, 1)

    # Display the result
    print(test_wave)


if __name__ == "__main__":
    main()
