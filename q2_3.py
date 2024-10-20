import matplotlib.pyplot as plt
import numpy as np

from q1_1 import N, Fsa, SpS
from q1_5 import nrz_waveform, time_vector
from q1_6 import nrz_spectrum
from q2_1 import cutoff_freqs
from scipy.signal import freqz, butter


# Revised approach to apply filtering and handle signal characteristics better
def apply_filter_time_domain(input_spectrum, cutoff_freqs, sampling_freq, N):
    plt.figure(figsize=(10, 6))

    for i, cutoff_freq in enumerate(cutoff_freqs):
        # Adjust the cutoff frequencies to better match the NRZ signal bandwidth
        nyquist = 0.5 * sampling_freq
        normal_cutoff = cutoff_freq / nyquist
        b, a = butter(4, normal_cutoff, btype="low", analog=False)

        # Get the frequency response of the filter
        w, h = freqz(b, a, worN=len(input_spectrum), fs=sampling_freq)

        # Apply the filter in the frequency domain
        filtered_spectrum = input_spectrum * h

        # Perform inverse FFT to get the time domain signal
        filtered_time_domain = np.fft.ifft(np.fft.ifftshift(filtered_spectrum))

        # Plot the first 12 time slots
        time_slots = 12 * SpS
        plt.plot(
            time_vector[:time_slots],
            filtered_time_domain[:time_slots].real,
            label=f"Fc = {cutoff_freq / 1e9} GHz",
        )

    # Plot the original input signal for comparison
    plt.plot(
        time_vector[:time_slots], nrz_waveform[:time_slots], "k--", label="Input Signal"
    )

    plt.title("Filtered Output Signal in Time Domain (First 12 Time Slots)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.show()


# Apply the filters and plot the output in the time domain
apply_filter_time_domain(nrz_spectrum, cutoff_freqs, Fsa, N)
