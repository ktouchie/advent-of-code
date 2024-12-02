import logging
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_lists_from_file(input_file):
    # Read the input file and return a list of lists
    with open(input_file, "r") as f:
        return [[int(x) for x in line.strip().split()] for line in f]


def check_list_safety(report_lists):
    # Initialize safe lists counter
    safe_lists = 0
    # Check each list for safety
    for report_list in report_lists:
        if is_safe(report_list):
            safe_lists += 1
        else:
            # Check if removing one element makes the list safe
            for i in range(len(report_list)):
                # All elements except the one at index i
                modified_list = report_list[:i] + report_list[i + 1 :]
                if is_safe(modified_list):
                    safe_lists += 1
                    break

    # Log the number of safe lists
    logger.info(f"Number of safe lists: {safe_lists}")
    return safe_lists


def is_safe(report_list):
    if len(report_list) < 2:
        return False

    ascending = report_list[0] < report_list[1]
    return check_list_progression(report_list, ascending)


def check_list_progression(report_list, ascending):
    # Check if the list is safe
    current_num = report_list[0]
    for i in report_list[1:]:
        if not check_difference(current_num, i, ascending):
            return False
        current_num = i
    return True


def check_difference(first, second, ascending=True):
    # Check if the difference between two numbers is safe
    if abs(first - second) < 4:
        # Check if the numbers continue ascending or descending order
        if (ascending and first < second) or (not ascending and first > second):
            return True
    return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day02.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    lists = get_lists_from_file(input_file)
    check_list_safety(lists)
