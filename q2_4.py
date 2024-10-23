from q1_1 import SpS
from q1_7 import plot_eye_diagram
from q2_1 import filters, filter_color_map
from q2_3 import output_time_signals


def main():
    # Plot the eye-diagram for each filtered output signal
    for i, fc in enumerate(filters):
        plot_eye_diagram(
            output_time_signals[i, :],  # Use real part of the output signal
            SpS,
            title=f"Eye Diagram (Filter {i+1}, Fc = {fc / 1e9:.2f} GHz)",
            color=filter_color_map.get(fc),
        )


if __name__ == "__main__":
    main()
