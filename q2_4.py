from q1_1 import SpS
from q1_7 import plot_eye_diagram
from q2_1 import filters, filter_color_map
from q2_3 import output_time_signals


def main():
    for i, fc in enumerate(filters):
        plot_eye_diagram(
            output_time_signals[i, :], 
            SpS,
            SpS//2,
            f"Eye Diagram (Filter {i+1}, Fc = {fc / 1e9:.2f} GHz)",
            color=filter_color_map.get(fc),
        )


if __name__ == "__main__":
    main()
