import matplotlib.pyplot as plt
import numpy as np

from q1_1 import frequency_vector

# Set figure DPI to 300 (increasing plot resolution)
plt.rcParams["savefig.dpi"] = 300

# Cutoff frequencies for the four filters
filters = [10e9, 7.5e9, 5e9, 2.5e9]
colors = ["blue", "orange", "green", "red"]
filter_color_map = dict(zip(filters, colors))

# Calculate transfer function for each filter
H = np.zeros((len(filters), len(frequency_vector)), dtype=complex)
for i, fc in enumerate(filters):
    H[i, :] = 1 / (1 + 1j * (abs(frequency_vector) / fc))

def find_3db_point(frequencies, H_magnitude):
    target_value = 20 * np.log10(1 / np.sqrt(2))  # -3 dB value
    # Find the index where the value is closest to -3dB
    idx = np.argmin(np.abs(20 * np.log10(np.abs(H_magnitude)) - target_value))
    return np.abs(frequencies[idx]), 20 * np.log10(np.abs(H_magnitude[idx]))

def plot_transfer_functions():
    plot_scale = 1e-9  # Hz to GHz    
    plt.figure(figsize=(10, 6))
    
    plt.axhline(
        -3,
        linestyle="--",
        label="-3dB",
        color="black",
        linewidth=1,
    )

    for i, fc in enumerate(filters):
        
        plt.semilogx(
            frequency_vector * plot_scale,
            20 * np.log10(np.abs(H[i, :])),  # Magnitude in dB
            label=f"Filter {i+1} (Fc = {fc / 1e9:.2f} GHz)",
            color=filter_color_map.get(fc),
            linewidth=2,
        )

        # Mark cutoff frequency (Fc) on the plot
        plt.axvline(
            fc * plot_scale,
            color=filter_color_map.get(fc),
            linestyle="--",
            linewidth=1,
        )
        
        # Find and mark the -3 dB point
        f_3db, mag_3db = find_3db_point(frequency_vector, H[i, :])
        print(f_3db * plot_scale, mag_3db)
        plt.plot(
            np.abs(f_3db) * plot_scale, 
            mag_3db,
            'o',
            linewidth=4,
            color=filter_color_map.get(fc), 
            #label=f'-3dB point (Fc = {fc / 1e9:.2f} GHz)'
        )

    plt.title("Magnitude of Transfer Functions")
    plt.xlabel("Frequency (GHz)")
    plt.ylabel("Magnitude (dB)")
    plt.xlim(right=frequency_vector.max() * plot_scale)
    plt.grid()
    plt.legend()
    plt.show()


def main():
    plot_transfer_functions()


if __name__ == "__main__":
    main()
