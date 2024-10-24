import numpy as np
import matplotlib.pyplot as plt

from q1_1 import SpS
from q1_5 import nrz_waveform

# Set figure DPI to 300 (increasing plot resolution)
plt.rcParams["savefig.dpi"] = 300

def plot_eye_diagram(signal, sps, offset, title, color="r"):
    x_scale = 1
    print(x_scale)
    for i in range(0, len(signal) - 2 * sps, sps):
        plt.plot(
            np.arange(-sps, sps) * x_scale / sps, 
            signal[i+offset:i+offset + 2*sps],
            color=color,
        )
    plt.xlabel('Time (ps)')
    plt.ylabel('Amplitude')
    plt.title(title)
    plt.grid()
    plt.show()

def main():
    plot_eye_diagram(
        nrz_waveform,
        SpS, 
        SpS//2,
        title="Eye Diagram of NRZ signal",
    )


if __name__ == "__main__":
    main()
