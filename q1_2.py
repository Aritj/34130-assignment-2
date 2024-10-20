import numpy as np
import matplotlib.pyplot as plt

from q1_1 import N, Tsa, SpS, A

# Time vector
t = np.arange(0, N * Tsa, Tsa)  # Total time duration

# Generate square pulse
square_pulse = np.zeros(N)
square_pulse[:SpS] = A  # First SpS samples set to amplitude A

# FFT and FFT shift
square_pulse_freq = np.fft.fftshift(np.fft.fft(square_pulse))

# Frequency vector
freq = np.fft.fftfreq(N, Tsa)
freq = np.fft.fftshift(freq)


def plot_square_pulse():
    plt.figure(figsize=(10, 4))
    plt.plot(t[: 2 * SpS], square_pulse[: 2 * SpS])  # Plot first two symbols
    plt.title("Square Pulse in Time Domain")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()


def plot_normalized_spectrum():
    plt.figure(figsize=(10, 4))
    plt.plot(freq, np.abs(square_pulse_freq) / N)
    plt.title("Spectrum of Square Pulse (Linear Scale)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Normalized Magnitude")
    plt.grid(True)
    plt.show()


def plot_normalized_spectrum_log():
    plt.figure(figsize=(10, 4))
    plt.semilogy(freq, np.abs(square_pulse_freq) / N)
    plt.title("Spectrum of Square Pulse (Logarithmic Scale)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Normalized Magnitude (Log Scale)")
    plt.grid(True)
    plt.show()


def main():
    plot_square_pulse()  # 1st plot
    plot_normalized_spectrum()  # 2nd plot
    plot_normalized_spectrum_log()  # 3rd plot


if __name__ == "__main__":
    main()
