import numpy as np

# Given values
B = 10e9  # Bit rate in bits per second
Rs = 10e9  # Symbol rate in baud (symbols per second)
A = 2  # Amplitude
SpS = 100  # Samples per symbol
L = 100  # Number of symbols

# Calculations
N = L * SpS  # a) Total number of samples (unitless)
Ts = 1 / Rs  # b) Symbol time slot width (seconds)
Tsa = Ts / SpS  # c) Sampling time (seconds)
Fsa = 1 / Tsa  # d) Sampling frequency (Hz)
Tw = N * Tsa  # e) Temporal width of the total time window (seconds)
Delta_F = 1 / Tw  # f) Frequency bin (Hz)

# Generate time vector and frequency vector
time_vector = np.arange(0, N) * Tsa  # Time vector
frequency_vector = np.fft.fftshift(np.fft.fftfreq(N, Tsa))  # Frequency vector centered at 0


def main():
    # Display results with units
    print(f"Total number of samples (N): {N}")
    print(f"Symbol time slot width (Ts): {Ts*1e12:.0f} [ps]")  # ps = picoseconds
    print(f"Sampling time (Tsa): {Tsa*1e12:.0f} [ps]")
    print(f"Sampling frequency (Fsa): {Fsa*1e-9:.0f} [GHz]")  # GHz = gigahertz
    print(f"Temporal width of total time window (Tw): {Tw*1e12} [ps]")
    print(f"Frequency resolution (Delta_F): {Delta_F*1e-9:.2f} [GHz]")


if __name__ == "__main__":
    main()
