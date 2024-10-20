import matplotlib.pyplot as plt
import numpy as np

from scipy.signal import freqz, butter
from q1_1 import Fsa


# Function to calculate and plot the transfer functions for different cutoff frequencies
def plot_transfer_functions(cutoff_freqs, sampling_freq, num_points=1000):
    plt.figure(figsize=(10, 6))

    # Create the frequency vector
    freq_range = np.logspace(
        8, 11, num_points
    )  # Frequency range from 100 MHz to 100 GHz

    for cutoff_freq in cutoff_freqs:
        # Design a Butterworth filter for each cutoff frequency
        nyquist = 0.5 * sampling_freq
        normal_cutoff = cutoff_freq / nyquist
        b, a = butter(4, normal_cutoff, btype="low", analog=False)

        # Compute the frequency response of the filter
        w, h = freqz(b, a, worN=num_points, fs=sampling_freq)

        # Plot the magnitude response (logarithmic scale)
        plt.semilogx(w, 20 * np.log10(abs(h)), label=f"Fc = {cutoff_freq / 1e9} GHz")

    plt.title("Magnitude of Transfer Functions")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.grid(True, which="both", axis="both")
    plt.legend()
    plt.show()


# Cutoff frequencies for the four filters
cutoff_freqs = [10e9, 7.5e9, 5e9, 2.5e9]

# Plot the transfer functions
plot_transfer_functions(cutoff_freqs, Fsa)  # Use Fsa as the sampling frequency
