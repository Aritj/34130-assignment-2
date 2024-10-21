import numpy as np
import matplotlib.pyplot as plt

from q1_1 import N
from q1_2 import freq
from q1_5 import nrz_waveform

# Set figure DPI to 300 (increasing plot resolution)
plt.rcParams["savefig.dpi"] = 300

# Step 1: Perform FFT and shift
nrz_spectrum = np.fft.fftshift(np.fft.fft(nrz_waveform))


def main():
    plt.figure(figsize=(10, 4))
    plt.semilogy(freq / 1e9, np.abs(nrz_spectrum) / N)
    plt.title("Spectrum of NRZ Signal (Logarithmic Scale)")
    plt.xlabel("Frequency (GHz)")
    plt.ylabel("Normalized Magnitude (Log Scale)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
