import numpy as np

# Given data
test_SpS = 4
test_L = 3
test_bits = np.array([1, 2, 3])


def main():
    # a) Replicate the bits test_SpS times (equivalent to repmat in MATLAB)
    test_wave = np.tile(test_bits, (test_SpS, 1))
    print(f"a)\n{test_wave}\n")

    # b) Reshape the array into a column vector (equivalent to reshape in MATLAB)
    test_wave = np.reshape(test_wave, (test_SpS * test_L, 1))
    print(f"b)\n{test_wave}\n")


if __name__ == "__main__":
    main()
