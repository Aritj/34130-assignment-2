import numpy as np
import matplotlib.pyplot as plt

from q1_1 import SpS, A
from q1_3 import bit_sequence

# Set figure DPI to 300 (increasing plot resolution)
plt.rcParams["savefig.dpi"] = 300

# 1. Repeat the bit sequence to match the samples per symbol (like repmat)
nrz_signal = np.repeat(bit_sequence, SpS)

# 2. Reshape is not needed here because np.repeat already gives a 1D array.
# Scaling the signal by amplitude
nrz_signal_res = nrz_signal * A


def plot_eye_diagram(signal, samples_per_symbol, title, color):
    plt.figure(figsize=(10, 6))

    # Split the signal into chunks of two symbols for the eye-diagram
    num_symbols = len(signal) // samples_per_symbol
    for i in range(0, num_symbols - 1):
        # Extract two symbols at a time
        plt.plot(
            signal[i * samples_per_symbol : (i + 2) * samples_per_symbol], color=color
        )

    plt.grid(True)
    plt.title(title, fontsize=14)
    plt.xlabel("Time (samples)", fontsize=12)
    plt.ylabel("Amplitude (A.U.)", fontsize=12)
    plt.show()


def main():
    plot_eye_diagram(
        nrz_signal_res,
        SpS,
        "Eye Diagram of NRZ signal",
        "red",
    )


if __name__ == "__main__":
    main()
