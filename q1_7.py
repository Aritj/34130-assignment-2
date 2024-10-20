import numpy as np
import matplotlib.pyplot as plt

# Parameters (adapt these based on your previous code)
L = 100  # Number of symbols
SpS = 100  # Samples per symbol
Amplitude = 2  # Amplitude scaling factor

# Example bit sequence (0 and 1)
bit_sequence = np.random.randint(0, 2, L)

# 1. Repeat the bit sequence to match the samples per symbol (like repmat)
nrz_signal = np.repeat(bit_sequence, SpS)

# 2. Reshape is not needed here because np.repeat already gives a 1D array.
# Scaling the signal by amplitude
nrz_signal_res = nrz_signal * Amplitude


# Function to plot the eye diagram
def plot_eye_diagram(signal, eye_periods=2):
    plt.figure(figsize=(10, 6))
    num_segments = len(signal) // SpS

    for i in range(num_segments - eye_periods):
        # Extract a segment of the signal (equivalent to one eye trace)
        segment = signal[i * SpS : (i + eye_periods) * SpS]

        # Adjust time segment for correct plotting (center around 0)
        time_seg = np.linspace(-SpS, SpS, eye_periods * SpS)

        # Plot the trace, using a light red color to replicate MATLAB's 'r' color
        plt.plot(time_seg, segment, alpha=0.2, color="r")

    # Set the title and labels for the plot
    plt.title("Eye Diagram of NRZ Signal")
    plt.xlabel("Time (ps)")
    plt.ylabel("Amplitude (A.U.)")
    plt.grid(True)

    # Set the x-axis limits to center the eye diagram
    plt.xlim([-SpS, SpS])

    # Display the plot
    plt.show()


# 3. Plot the eye diagram with the generated NRZ signal
plot_eye_diagram(nrz_signal_res)
