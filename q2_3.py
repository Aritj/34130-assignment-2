import numpy as np
import matplotlib.pyplot as plt

from q1_1 import time_vector, SpS
from q1_5 import nrz_waveform
from q2_1 import filters, filter_color_map
from q2_2 import output_spectra

# Set figure DPI to 300 (increasing plot resolution)
plt.rcParams["savefig.dpi"] = 300

# Calculate time-domain signals for each filter using inverse FFT to get time-domain signal
output_time_signals = np.zeros((len(filters), len(time_vector)), dtype=complex)
for i, fc in enumerate(filters):
    output_time_signals[i, :] = np.fft.ifft(np.fft.ifftshift(output_spectra[i, :]))


def main():
    # Plotting the first 12 time slots for input and output signals
    num_time_slots = 12
    plot_scale = 1e12  # s to ps

    for i, fc in enumerate(filters):
        plt.figure(figsize=(10, 6))

        # Plot input signal
        plt.plot(
            time_vector[: SpS * num_time_slots] * plot_scale,
            nrz_waveform[: SpS * num_time_slots],
            label="Input Signal",
            color="black",
            linewidth=2,
        )

        # Plot output signal after filtering
        plt.plot(
            time_vector[: SpS * num_time_slots] * plot_scale,
            np.real(output_time_signals[i, : SpS * num_time_slots]),
            label=f"Output Signal",
            color=filter_color_map.get(fc),
            linestyle="--",
            linewidth=2,
        )

        # Plots settings
        plt.grid()
        plt.xlabel("Time (ps)", fontsize=12)
        plt.ylabel("Amplitude (A.U.)", fontsize=12)
        plt.title(
            f"Time Domain Signal: Input vs Output (Filter {i+1}, Fc = {fc / 1e9:.2f} GHz)"
        )
        plt.legend(loc='lower left')
        plt.show()


if __name__ == "__main__":
    main()
