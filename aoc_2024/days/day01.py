import logging
import sys

import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def calculate_differences_sum(input_file):
    # Load the data into a pandas DataFrame
    df = pd.read_csv(input_file, sep=r"\s+", header=None, names=["col1", "col2"])

    # Sort each column
    sorted_col1 = df["col1"].sort_values().reset_index(drop=True)
    sorted_col2 = df["col2"].sort_values().reset_index(drop=True)

    # Calculate the differences between the corresponding sorted values
    differences = abs(sorted_col1 - sorted_col2)

    # Calculate the sum of all differences
    total_difference = differences.sum()

    # Display the results
    logger.info(f"Sum of all differences: {total_difference}")
    return sorted_col1, sorted_col2, total_difference


def calculate_similarity_score(sorted_col1, sorted_col2):
    # Initialize similarity score
    similarity_score = 0

    # Count occurrences of each number in 2nd column
    counts_col2 = _count_occurrences(sorted_col2)

    # Calculate similarity score based on common elements
    for i in sorted_col1:
        if i in counts_col2:
            similarity_score += i * counts_col2[i]

    # Log the similarity score
    logger.info(f"Similarity score: {similarity_score}")
    return similarity_score


def _count_occurrences(sorted_column):
    # Initialize counts dictionary
    counts = {}

    # Initialize current number and count
    current_num = sorted_column[0]
    current_count = 1

    # Count occurrences of each number in the sorted column
    for n in sorted_column[1:]:
        if n == current_num:
            current_count += 1
        else:
            counts[current_num] = current_count
            current_num = n
            current_count = 1

    # Add the last counted number to the dictionary
    counts[current_num] = current_count

    return counts


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day01.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    sorted_col1, sorted_col2, total_difference = calculate_differences_sum(input_file)
    calculate_similarity_score(sorted_col1, sorted_col2)
