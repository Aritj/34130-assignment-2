import numpy as np
import matplotlib.pyplot as plt

from q1_1 import N, frequency_vector
from q1_2 import square_pulse_freq
from q1_5 import nrz_waveform

# Set figure DPI to 300 (increasing plot resolution)
plt.rcParams["savefig.dpi"] = 300

nrz_spectrum = np.fft.fftshift(np.fft.fft(nrz_waveform))

def main():
    x_scale = 1e-9 # Hz to GHz
    plt.figure(figsize=(10, 4))
    
    # N-normalised absolute value of the spectrum
    plt.semilogy(
        frequency_vector * x_scale, 
        np.abs(nrz_spectrum) / N,
        label="NRZ waveform spectrum",
    )
    
    # N-normalised absolute value of the square pulse spectrum
    plt.semilogy(
        frequency_vector * x_scale,
        np.abs(square_pulse_freq) / N,
        label="Square Pulse Spectrum",
    )
    
    # Plot settings
    plt.title("Spectrum of NRZ Signal (Logarithmic Scale)")
    plt.xlabel("Frequency (GHz)")
    plt.ylabel("Normalized Magnitude (Log Scale)")
    plt.grid()
    plt.legend(loc='upper right')
    plt.xlim(frequency_vector.min() * x_scale, frequency_vector.max()* x_scale)
    plt.ylim(10e-7, 1)
    plt.show()


if __name__ == "__main__":
    main()
