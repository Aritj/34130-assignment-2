import numpy as np
import matplotlib.pyplot as plt

from q1_1 import SpS, A, time_vector
from q1_3 import bits_OOK

# Set figure DPI to 300 (increasing plot resolution)
plt.rcParams["savefig.dpi"] = 300

# Generate the NRZ waveform of L "random" bits repeated SpS times and scaled by amplitude A
nrz_waveform = np.repeat(bits_OOK, SpS) * A


def main():
    x_scale = 1e12  # s to ps
    time_slot = 12 * SpS  # first 12 time slots

    # Plot the NRZ signal for the first 12 symbols
    plt.figure(figsize=(10, 4))
    plt.plot(time_vector[:time_slot] * x_scale, nrz_waveform[:time_slot])
    plt.title("NRZ Signal in Time Domain (first 12 time slots)")
    plt.xlabel("Time (ps)")
    plt.ylabel("Amplitude")
    plt.xlim(time_vector.min() * x_scale, time_vector[:time_slot].max() * x_scale)
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
