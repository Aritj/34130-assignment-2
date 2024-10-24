import numpy as np
import matplotlib.pyplot as plt

from q1_1 import N, SpS, A, time_vector, frequency_vector

# Set figure DPI to 300 (increasing plot resolution)
plt.rcParams["savefig.dpi"] = 300


# Create square pulse
square_pulse = np.zeros(N)
pulse_center = N // 2
square_pulse[pulse_center - SpS // 2 : pulse_center + SpS // 2] = A

# Spectrum calculation
square_pulse_freq = np.fft.fftshift(np.fft.fft(square_pulse))

def plot_square_pulse():
    x_scale = 1e12 # s to ps
    plt.figure(figsize=(10, 4))
    
    # Plot the Square Pulse
    plt.plot(time_vector * x_scale, square_pulse)
    
    # Plot settings
    plt.title("Square Pulse in Time Domain")
    plt.xlabel("Time (ps)")
    plt.ylabel("Amplitude")
    plt.xlim([4800, 5200])
    plt.grid()
    plt.show()


def plot_normalized_spectrum():
    x_scale = 1e-9 # Hz to GHz
    plt.figure(figsize=(10, 4))
    plt.plot(frequency_vector * x_scale, np.abs(square_pulse_freq) / N)
    plt.title("Spectrum of Square Pulse (Linear Scale)")
    plt.xlabel("Frequency (GHz)")
    plt.ylabel("Normalized Magnitude")
    plt.xlim(frequency_vector.min() * x_scale, frequency_vector.max() * x_scale)
    plt.grid()
    plt.show()


def plot_normalized_spectrum_log():
    x_scale = 1e-9 # Hz to GHz
    plt.figure(figsize=(10, 4))
    plt.semilogy(frequency_vector * x_scale, np.abs(square_pulse_freq) / N)
    plt.title("Spectrum of Square Pulse (Logarithmic Scale)")
    plt.xlabel("Frequency (GHz)")
    plt.ylabel("Normalized Magnitude (Log Scale)")
    plt.xlim(frequency_vector.min() * x_scale, frequency_vector.max() * x_scale)
    plt.grid()
    plt.show()


def main():
    plot_square_pulse()  # 1st plot
    plot_normalized_spectrum()  # 2nd plot
    plot_normalized_spectrum_log()  # 3rd plot


if __name__ == "__main__":
    main()
