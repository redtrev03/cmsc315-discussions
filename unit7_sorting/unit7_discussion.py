"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

This project demonstrates two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)
"""


def bubble_sort(lst):
    """
    Sort a list using the Bubble Sort algorithm.

    Bubble Sort compares adjacent elements and swaps them
    when they are in the wrong order.
    """

    # Create a copy so the original list is not changed.
    result = lst.copy()

    # Continue making passes through the list.
    for i in range(len(result)):
        swapped = False

        # Compare adjacent elements that have not already
        # been placed in their correct positions.
        for j in range(0, len(result) - i - 1):

            # Swap the values if they are out of order.
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        # If no swaps occurred, the list is already sorted.
        if not swapped:
            break

    return result


def merge_sort(lst):
    """
    Sort a list using the Merge Sort algorithm.

    Merge Sort recursively divides the list into smaller
    halves and then merges the sorted halves together.
    """

    # A list with zero or one elements is already sorted.
    if len(lst) <= 1:
        return lst.copy()

    # Find the middle of the list.
    middle = len(lst) // 2

    # Divide the list into left and right halves.
    left = lst[:middle]
    right = lst[middle:]

    # Recursively sort each half.
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Merge the two sorted halves.
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    Merge two sorted lists into one sorted list.
    """

    result = []

    # Starting positions for each list.
    left_index = 0
    right_index = 0

    # Compare values from both lists and add the smaller
    # value to the result.
    while left_index < len(left) and right_index < len(right):

        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add any remaining values from the left list.
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    # Add any remaining values from the right list.
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # DATASET #1
    # ===============================

    dataset1 = [64, 25, 12, 22, 11, 90, 34, 7]

    print("\n=== DATASET #1 ===")
    print("Original list:", dataset1)

    bubble_result1 = bubble_sort(dataset1)
    merge_result1 = merge_sort(dataset1)

    print("Bubble Sort:", bubble_result1)
    print("Merge Sort:", merge_result1)

    # Compare the results from both algorithms.
    print("Results match:", bubble_result1 == merge_result1)

    # ===============================
    # DATASET #2
    # ===============================

    dataset2 = [45, 3, 78, 21, 56, 9, 32, 67, 15]

    print("\n=== DATASET #2 ===")
    print("Original list:", dataset2)

    bubble_result2 = bubble_sort(dataset2)
    merge_result2 = merge_sort(dataset2)

    print("Bubble Sort:", bubble_result2)
    print("Merge Sort:", merge_result2)

    # Compare the results from both algorithms.
    print("Results match:", bubble_result2 == merge_result2)

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty list
    empty_list = []

    print("\n1. Empty List")
    print("Original:", empty_list)
    print("Bubble Sort:", bubble_sort(empty_list))
    print("Merge Sort:", merge_sort(empty_list))
    print("Explanation: Both algorithms return an empty list because there are no values to sort.")

    # Edge Case 2: List with duplicate values
    duplicate_list = [5, 2, 8, 2, 5, 1, 8]

    print("\n2. List With Duplicate Values")
    print("Original:", duplicate_list)
    print("Bubble Sort:", bubble_sort(duplicate_list))
    print("Merge Sort:", merge_sort(duplicate_list))
    print("Explanation: Both algorithms correctly sort the values while keeping duplicate values.")

    # Edge Case 3: Already sorted list
    sorted_list = [1, 2, 3, 4, 5, 6, 7]

    print("\n3. Already Sorted List")
    print("Original:", sorted_list)
    print("Bubble Sort:", bubble_sort(sorted_list))
    print("Merge Sort:", merge_sort(sorted_list))
    print("Explanation: The list is already sorted, so Bubble Sort can stop early because no swaps are needed.")

    # Edge Case 4: Reverse-sorted list
    reverse_list = [7, 6, 5, 4, 3, 2, 1]

    print("\n4. Reverse-Sorted List")
    print("Original:", reverse_list)
    print("Bubble Sort:", bubble_sort(reverse_list))
    print("Merge Sort:", merge_sort(reverse_list))
    print("Explanation: Both algorithms rearrange the values into ascending order.")


if __name__ == "__main__":
    main()