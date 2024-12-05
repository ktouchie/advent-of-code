import logging
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_lists_from_file(input_file):
    # Read the input file and return both lists of page numbers
    with open(input_file, "r") as f:
        content = f.read()
    sections = content.strip().split("\n\n")
    page_order_rules = [
        list(map(int, line.split("|"))) for line in sections[0].splitlines()
    ]
    printing_orders = [
        list(map(int, line.split(","))) for line in sections[1].splitlines()
    ]
    return page_order_rules, printing_orders


def printing_order_respects_rule(rule, printing_order):
    # Check if the printing order respects the rule
    if rule[0] in printing_order and rule[1] in printing_order:
        if printing_order.index(rule[0]) > printing_order.index(rule[1]):
            return False
    return True


def get_middle_page(printing_order):
    # Find the middle page in the printing order
    if len(printing_order) % 2 == 0:
        return 0
    middle_index = len(printing_order) // 2
    return printing_order[middle_index]


def reorder_pages(page_order_rules, printing_orders):
    corrected_orders = []

    while printing_orders:
        printing_order = printing_orders.pop(0)
        rules_respected = True

        # Reorder the printing orders based on the rules
        for rule in page_order_rules:
            if not printing_order_respects_rule(rule, printing_order):
                index_0 = printing_order.index(rule[0])
                index_1 = printing_order.index(rule[1])
                printing_order[index_0], printing_order[index_1] = (
                    printing_order[index_1],
                    printing_order[index_0],
                )
                rules_respected = False
                break

        if rules_respected:
            corrected_orders.append(printing_order)
        else:
            # If rules are not respected, add back to the end of the list
            printing_orders.append(printing_order)

    return corrected_orders


def get_sum_of_middle_pages(input_file):
    sum_of_middle_pages = 0
    sum_of_corrected_middle_pages = 0
    unordered_pages = []
    page_order_rules, printing_orders = get_lists_from_file(input_file)
    for printing_order in printing_orders:
        rules_respected = True
        for rule in page_order_rules:
            if not printing_order_respects_rule(rule, printing_order):
                unordered_pages.append(printing_order)
                rules_respected = False
                break
        if rules_respected:
            sum_of_middle_pages += get_middle_page(printing_order)
    corrected_orders = reorder_pages(page_order_rules, unordered_pages)
    for corrected_order in corrected_orders:
        sum_of_corrected_middle_pages += get_middle_page(corrected_order)
    logger.info(f"Sum of middle pages: {sum_of_middle_pages}")
    logger.info(f"Sum of corrected middle pages: {sum_of_corrected_middle_pages}")
    return sum_of_middle_pages, sum_of_corrected_middle_pages


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day05.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    get_sum_of_middle_pages(input_file)
