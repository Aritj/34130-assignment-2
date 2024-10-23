import numpy as np
import matplotlib.pyplot as plt

from q1_1 import N, SpS, A, time_vector, frequency_vector

# Set figure DPI to 300 (increasing plot resolution)
plt.rcParams["savefig.dpi"] = 300

# Generate square pulse
square_pulse = np.zeros(N)
square_pulse[:SpS] = A  # First SpS samples set to amplitude A

# FFT and FFT shift
square_pulse_freq = np.fft.fftshift(np.fft.fft(square_pulse))


def plot_square_pulse():
    plt.figure(figsize=(10, 4))
    plt.plot(time_vector[: 2 * SpS] * 1e12, square_pulse[: 2 * SpS])
    plt.title("Square Pulse in Time Domain")
    plt.xlabel("Time (ps)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()


def plot_normalized_spectrum():
    plt.figure(figsize=(10, 4))
    plt.plot(frequency_vector * 1e-9, np.abs(square_pulse_freq) / N)
    plt.title("Spectrum of Square Pulse (Linear Scale)")
    plt.xlabel("Frequency (GHz)")
    plt.ylabel("Normalized Magnitude")
    plt.grid(True)
    plt.show()


def plot_normalized_spectrum_log():
    plt.figure(figsize=(10, 4))
    plt.semilogy(frequency_vector * 1e-9, np.abs(square_pulse_freq) / N)
    plt.title("Spectrum of Square Pulse (Logarithmic Scale)")
    plt.xlabel("Frequency (GHz)")
    plt.ylabel("Normalized Magnitude (Log Scale)")
    plt.grid(True)
    plt.show()


def main():
    plot_square_pulse()  # 1st plot
    plot_normalized_spectrum()  # 2nd plot
    plot_normalized_spectrum_log()  # 3rd plot


if __name__ == "__main__":
    main()
