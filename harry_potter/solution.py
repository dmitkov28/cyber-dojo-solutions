import itertools
from typing import Dict, List, Set, Tuple


def calculate_discount(n_books: int) -> float:
    SINGLE_BOOK_PRICE = 8
    discount_rates = {1: 0, 2: 0.05, 3: 0.1, 4: 0.2, 5: 0.25}
    if n_books not in discount_rates:
        return 0

    return discount_rates[n_books] * n_books * SINGLE_BOOK_PRICE


def find_combinations(books: List[str], n: int) -> Set[Tuple[int]]:
    return list(itertools.combinations(set(books), n))


def find_all_combinations(books: List[str]) -> List[Dict[int, int]]:
    MAX_GROUP_SIZE = 5
    all_groups = []
    for group_size in range(MAX_GROUP_SIZE, 1, -1):
        remaining_books = books.copy()
        groups = {}
        initial_group_size = group_size
        while remaining_books:
            combinations = find_combinations(remaining_books, initial_group_size)
            if combinations:
                if initial_group_size not in groups:
                    groups[initial_group_size] = 0
                groups[initial_group_size] += 1
                for item in list(combinations)[0]:
                    remaining_books.remove(item)
            else:
                initial_group_size -= 1
        all_groups.append(groups)
    return all_groups


def find_max_discount(groups: List[Dict[int, int]]):
    discounts = []
    for group in groups:
        group_size = list(group.keys())[0]
        count = list(group.values())[0]

        discount = {}
        discount["group_size"] = group_size
        discount["group_count"] = count
        discount["discount"] = calculate_discount(group_size) * count
        discounts.append(discount)
    return [
        group
        for group in discounts
        if max([item.get("discount") for item in discounts]) == group.get("discount")
    ][0]
