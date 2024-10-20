import matplotlib.pyplot as plt
import numpy as np

from q1_1 import N, Fsa
from q1_2 import freq
from q1_6 import nrz_spectrum
from q2_1 import cutoff_freqs
from scipy.signal import freqz, butter


# Function to apply the filter in the frequency domain and plot the result
def plot_filtered_spectrum(input_spectrum, cutoff_freqs, sampling_freq):
    plt.figure(figsize=(10, 6))

    for i, cutoff_freq in enumerate(cutoff_freqs):
        # Design the low-pass Butterworth filter
        nyquist = 0.5 * sampling_freq
        normal_cutoff = cutoff_freq / nyquist
        b, a = butter(4, normal_cutoff, btype="low", analog=False)

        # Get the frequency response of the filter
        w, h = freqz(b, a, worN=len(input_spectrum), fs=sampling_freq)

        # Apply the filter in the frequency domain (multiply with input spectrum)
        output_spectrum = input_spectrum * h

        # Plot the output spectrum
        plt.semilogy(
            freq, np.abs(output_spectrum) / N, label=f"Fc = {cutoff_freq / 1e9} GHz"
        )

    # Plot the input spectrum for comparison
    plt.semilogy(freq, np.abs(input_spectrum) / N, "k--", label="Input Spectrum")

    plt.title("Filtered Output Spectrum (Logarithmic Scale)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (Log Scale)")
    plt.grid(True)
    plt.legend()
    plt.show()


# Step 2: Apply the filters and plot the filtered spectra
plot_filtered_spectrum(nrz_spectrum, cutoff_freqs, Fsa)
