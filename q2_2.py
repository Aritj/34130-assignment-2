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


def individual_plots():
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

        # Plot settings
        plt.grid()
        plt.xlabel("Frequency (GHz)", fontsize=12, color="black")
        plt.ylabel("Magnitude (dB)", fontsize=12, color="black")
        plt.title(f"Filter {i+1} (Fc = {fc * plot_scale:.1f} GHz)")
        plt.legend()
        plt.ylim(10e-7, max(np.abs(nrz_spectrum) / N))
        plt.xlim(frequency_vector.min() * plot_scale, frequency_vector.max() * plot_scale)
        plt.show()


def combined_plots():
    # Create plots for each filter
    plot_scale = 1e-9  # Hz to GHz
    plt.figure(figsize=(9, 6))

    # Plot input spectra
    plt.semilogy(
        frequency_vector * plot_scale,
        np.abs(nrz_spectrum) / N,
        linewidth=2,
        color="black",
        label="Input Spectrum",
    )
    
    for i, fc in enumerate(filters):
        plt.semilogy(
            frequency_vector * plot_scale,
            np.abs(output_spectra[i, :]) / N,
            color=filter_color_map.get(fc),
            linewidth=2,
            label=f"Output Spectrum (Fc = {fc*plot_scale:.2f} GHz)",
        )

    # Plot settings
    plt.grid()
    plt.xlabel("Frequency (GHz)", fontsize=12, color="black")
    plt.ylabel("Magnitude (dB)", fontsize=12, color="black")
    plt.title(f"Input and all filtered outputs")
    plt.legend()
    plt.ylim(10e-7, max(np.abs(nrz_spectrum) / N))
    plt.xlim(frequency_vector.min() * plot_scale, frequency_vector.max() * plot_scale)
    plt.show()

def main():
    individual_plots()
    combined_plots()

if __name__ == "__main__":
    main()
