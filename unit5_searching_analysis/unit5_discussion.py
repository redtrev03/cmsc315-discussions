"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

In this assignment, two fundamental search algorithms are
implemented and tested: linear search and binary search.

The program tests both algorithms using small and large
datasets and demonstrates several edge cases.
"""


def linear_search(lst, target):
    """
    Implement a linear search algorithm.

    Linear search checks each element from the beginning
    of the list until the target is found. In the worst case,
    every element must be checked, giving it O(n) time
    complexity.
    """

    # Start at the beginning and check each element one at a time.
    for i in range(len(lst)):
        if lst[i] == target:
            return i

    # If the loop finishes, the target was not found.
    return -1


def binary_search(lst, target):
    """
    Implement a binary search algorithm.

    Binary search assumes the list is already sorted. Each
    iteration checks the middle element and eliminates half
    of the remaining search space. This gives binary search
    an O(log n) time complexity.
    """

    left = 0
    right = len(lst) - 1

    while left <= right:
        # Find the middle position of the current search area.
        middle = (left + right) // 2

        # If the middle value is the target, return its index.
        if lst[middle] == target:
            return middle

        # If the target is larger, search the right half.
        elif lst[middle] < target:
            left = middle + 1

        # If the target is smaller, search the left half.
        else:
            right = middle - 1

        # Each iteration removes approximately half of the
        # remaining elements from consideration.

    # If the search area becomes empty, the target was not found.
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # SMALL DATASET
    # ===============================
    #
    # A small sorted list is created and both search algorithms
    # are tested with values that exist and do not exist.

    print("\n=== SMALL DATASET TEST ===")

    small_data = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    print("Dataset:", small_data)

    # Test a value that exists.
    target = 50

    linear_result = linear_search(small_data, target)
    binary_result = binary_search(small_data, target)

    print("\nSearching for:", target)
    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    # Test a value that does not exist.
    target = 55

    linear_result = linear_search(small_data, target)
    binary_result = binary_search(small_data, target)

    print("\nSearching for:", target)
    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    # Both searches return -1 when the target is not found.
    # Binary search can find values faster because it eliminates
    # half of the remaining search space during each iteration.

    # ===============================
    # LARGE DATASET
    # ===============================
    #
    # A much larger sorted dataset is created to demonstrate
    # why binary search becomes more efficient as the dataset
    # increases in size.

    print("\n=== LARGE DATASET TEST ===")

    large_data = list(range(1, 100001))

    target = 98765

    linear_result = linear_search(large_data, target)
    binary_result = binary_search(large_data, target)

    print("Large dataset contains", len(large_data), "values.")
    print("Searching for:", target)
    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    # Linear search may need to check thousands of values before
    # reaching the target. Its worst-case time complexity is O(n).
    #
    # Binary search repeatedly cuts the search area in half.
    # Even with 100,000 values, it only needs a relatively small
    # number of comparisons. Its time complexity is O(log n).
    #
    # Therefore, binary search becomes much more efficient than
    # linear search when working with large sorted datasets.

    # ===============================
    # EDGE CASES
    # ===============================
    #
    # Several edge cases are tested to make sure both functions
    # handle unusual inputs correctly.

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty list
    empty_list = []

    print("\nEdge Case 1: Empty list")
    print("Linear search:", linear_search(empty_list, 10))
    print("Binary search:", binary_search(empty_list, 10))

    # Both algorithms return -1 because there are no elements
    # available to search.

    # Edge Case 2: Single-element list
    single_list = [42]

    print("\nEdge Case 2: Single-element list")

    print("Searching for 42:")
    print("Linear search:", linear_search(single_list, 42))
    print("Binary search:", binary_search(single_list, 42))

    print("Searching for 100:")
    print("Linear search:", linear_search(single_list, 100))
    print("Binary search:", binary_search(single_list, 100))

    # The searches return index 0 when the only value is found.
    # They return -1 when the requested value is not present.

    # Edge Case 3: First element
    print("\nEdge Case 3: Target at first position")

    first_target = small_data[0]

    print("Searching for:", first_target)
    print("Linear search:", linear_search(small_data, first_target))
    print("Binary search:", binary_search(small_data, first_target))

    # Edge Case 4: Last element
    print("\nEdge Case 4: Target at last position")

    last_target = small_data[-1]

    print("Searching for:", last_target)
    print("Linear search:", linear_search(small_data, last_target))
    print("Binary search:", binary_search(small_data, last_target))


if __name__ == "__main__":
    main()