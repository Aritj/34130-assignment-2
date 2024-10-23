import numpy as np
import matplotlib.pyplot as plt

from q1_1 import N, frequency_vector
from q1_6 import nrz_spectrum
from q2_1 import filters, filter_color_map, H

# Set figure DPI to 300 (increasing plot resolution)
plt.rcParams["savefig.dpi"] = 300

# Calculate output spectra
output_spectra = np.zeros((len(filters), len(frequency_vector)), dtype=complex)
for i, fc in enumerate(filters):
    output_spectra[i, :] = nrz_spectrum * H[i, :]


def main():
    # Create plots for each filter
    plot_scale = 1e-9  # Hz to GHz

    for i, fc in enumerate(filters):
        plt.figure(figsize=(9, 6))

        # Plot input and output spectra
        plt.semilogy(
            frequency_vector * plot_scale,
            np.abs(nrz_spectrum) / N,
            linewidth=2,
            color="black",
            label="Input Spectrum",
        )
        plt.semilogy(
            frequency_vector * plot_scale,
            np.abs(output_spectra[i, :]) / N,
            color=filter_color_map.get(fc),
            linewidth=2,
            label="Output Spectrum",
        )

        # Add vertical line at cutoff frequency
        plt.axvline(
            fc * plot_scale,
            linestyle=":",
            color=filter_color_map.get(fc),
            linewidth=2,
        )

        # Plot settings
        plt.grid()
        plt.xlabel("Frequency (GHz)", fontsize=12, color="black")
        plt.ylabel("Magnitude (dB)", fontsize=12, color="black")
        plt.title(f"Filter {i+1} (Fc = {fc * plot_scale:.1f} GHz)")
        plt.legend()
        plt.xlim(0, frequency_vector.max() * plot_scale)
        plt.show()


if __name__ == "__main__":
    main()
