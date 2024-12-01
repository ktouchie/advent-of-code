import sys

import pandas as pd


class Day01:
    def __init__(self, input_file):
        self.input_file = input_file

    def calculate_differences_sum(self):
        # Load the data into a pandas DataFrame
        df = pd.read_csv(
            self.input_file, sep=r"\s+", header=None, names=["col1", "col2"]
        )

        # Sort each column
        sorted_col1 = df["col1"].sort_values().reset_index(drop=True)
        sorted_col2 = df["col2"].sort_values().reset_index(drop=True)

        # Calculate the differences between the corresponding sorted values
        differences = abs(sorted_col1 - sorted_col2)

        # Calculate the sum of all differences
        total_difference = differences.sum()

        # Display the results
        print(differences)
        print(f"Sum of all differences: {total_difference}")
        return total_difference


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day01.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    day01 = Day01(input_file)
    day01.calculate_differences_sum()
