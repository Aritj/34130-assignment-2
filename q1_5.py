import numpy as np
import matplotlib.pyplot as plt

from q1_1 import Tsa
from q1_3 import L, generate_bit_sequence

# Given data
SpS = 100  # Samples per symbol
A = 2  # Amplitude

# Step 1: Generate random bit sequence
bit_sequence = generate_bit_sequence(L)

# Step 2: Generate the NRZ waveform (each bit repeated SpS times)
nrz_waveform = np.repeat(bit_sequence, SpS) * A  # Scale by amplitude

# Step 3: Generate time vector
time_vector = np.arange(0, len(nrz_waveform) * Tsa, Tsa)


def main():
    # Plot the NRZ signal for the first 12 symbols
    plt.figure(figsize=(10, 4))
    plt.plot(time_vector[: 12 * SpS], nrz_waveform[: 12 * SpS])
    plt.title("NRZ Signal in Time Domain (First 12 Symbols)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
