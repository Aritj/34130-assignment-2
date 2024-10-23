import matplotlib.pyplot as plt
import numpy as np

from q1_1 import frequency_vector

# Set figure DPI to 300 (increasing plot resolution)
plt.rcParams["savefig.dpi"] = 300

# Cutoff frequencies for the four filters
filters = [10e9, 7.5e9, 5e9, 2.5e9]
colors = ["blue", "orange", "green", "red"]
filter_color_map = dict(zip(filters, colors))

# Initialize transfer functions array
H = np.zeros((len(filters), len(frequency_vector)), dtype=complex)

# Calculate transfer function for each filter
for i, fc in enumerate(filters):
    H[i, :] = 1 / (1 + 1j * (frequency_vector / fc))


# Function to calculate and plot the transfer functions for different cutoff frequencies
def plot_transfer_functions():
    plot_scale = 10e-9  # Hz to GHz
    plt.figure(figsize=(10, 6))

    for i, fc in enumerate(filters):
        plt.semilogx(
            frequency_vector * plot_scale,  # Convert to GHz for plotting
            20 * np.log10(np.abs(H[i, :])),  # Magnitude in dB
            label=f"Filter {i+1} (Fc = {fc / 1e9:.2f} GHz)",
            color=filter_color_map.get(fc),
            linewidth=2,
        )

        # Mark cutoff frequency (Fc) on the plot
        plt.axvline(
            fc / 1e9,
            color=filter_color_map.get(fc),
            linestyle="--",
            linewidth=1,
        )

    print(frequency_vector.max() * plot_scale)
    plt.title("Magnitude of Transfer Functions")
    plt.xlabel("Frequency (GHz)")
    plt.ylabel("Magnitude (dB)")
    plt.xlim(right=frequency_vector.max() * plot_scale)
    plt.grid()
    plt.legend()
    plt.show()


def main():
    plot_transfer_functions()  # Use Fsa as the sampling frequency


if __name__ == "__main__":
    main()
