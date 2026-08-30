"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

This program demonstrates how Python lists behave when elements
are inserted, removed, and searched. It also explains how these
operations affect the position of other elements and their performance.
"""


def insert_at(lst, index, value):
    """
    Insert a value into the list at the specified index.

    Python's insert() operation places the new value at the requested
    position. Existing elements at that position and after it are
    shifted one position to the right.

    Insertion at the beginning or middle can require more shifting,
    making those operations O(n) in the worst case. Insertion at the
    end is generally more efficient because fewer elements need to move.
    """

    # The insert() method adds the value at the specified index.
    # Existing elements from that index onward are shifted to the right.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    Remove and return the value at the specified index.

    Returns None if the index is invalid.
    """

    # Validate the index before attempting to delete anything.
    # This prevents an IndexError and makes the function safer to use.
    if index < 0 or index >= len(lst):
        return None

    # Save the value before removing it so it can be returned.
    removed_value = lst[index]

    # Removing an element causes elements after it to shift left
    # to fill the empty position. This can take O(n) time.
    lst.pop(index)

    return removed_value


def search_value(lst, value):
    """
    Search for a value within the list.

    Returns the index if the value is found.
    Returns -1 if the value is not found.
    """

    # Python lists use sequential searching when using this approach.
    # Each element is checked one at a time from the beginning of the list.
    # Therefore, this is a linear search with O(n) worst-case performance.
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    # If the loop finishes without finding the value, return -1.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # INSERTION TESTS
    # ===============================

    print("\n=== INSERTION TESTS ===")

    # Create a list containing several values.
    numbers = [10, 20, 30, 40, 50]

    # Display the original list before making any changes.
    print("Original list:", numbers)

    # Insert a value at the beginning of the list.
    # All existing elements must shift one position to the right.
    insert_at(numbers, 0, 5)
    print("After inserting 5 at the beginning:", numbers)

    # Insert a value in the middle of the list.
    # Elements after the insertion point shift one position to the right.
    insert_at(numbers, 3, 25)
    print("After inserting 25 in the middle:", numbers)

    # Insert a value at the end of the list.
    # Since no existing elements need to move, this is generally faster.
    insert_at(numbers, len(numbers), 60)
    print("After inserting 60 at the end:", numbers)

    # ===============================
    # DELETION TESTS
    # ===============================

    print("\n=== DELETION TESTS ===")

    # Delete an item from the beginning of the list.
    # Elements after the removed item shift one position to the left.
    removed = delete_at(numbers, 0)
    print("Removed from beginning:", removed)
    print("List after beginning deletion:", numbers)

    # Delete an item from the middle of the list.
    # Elements after the removed item shift left to fill the empty space.
    middle_index = len(numbers) // 2
    removed = delete_at(numbers, middle_index)
    print("Removed from middle:", removed)
    print("List after middle deletion:", numbers)

    # Delete an item from the end of the list.
    # No other elements need to shift, so this is generally efficient.
    removed = delete_at(numbers, len(numbers) - 1)
    print("Removed from end:", removed)
    print("List after end deletion:", numbers)

    # ===============================
    # SEARCH TESTS
    # ===============================

    print("\n=== SEARCH TESTS ===")

    # Search for a value that exists in the list.
    # The function returns the position where the value was found.
    search_result = search_value(numbers, 30)
    print("Searching for 30...")
    print("Result: 30 found at index", search_result)

    # Search for a value that does not exist in the list.
    # The function returns -1 when the value cannot be found.
    search_result = search_value(numbers, 100)
    print("Searching for 100...")
    print("Result: 100 found at index", search_result)

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    # Edge Case 1: Attempt to delete using an invalid index.
    # The function checks the index first and returns None instead
    # of causing an IndexError.
    invalid_delete = delete_at(numbers, 100)
    print("Attempting to delete index 100:", invalid_delete)

    # Edge Case 2: Search for a value that is not in the list.
    # A result of -1 indicates that the value was not found.
    missing_search = search_value(numbers, 999)
    print("Searching for 999:", missing_search)

    # Edge Case 3: Insert into an empty list.
    # Python allows insert() to add an item to an empty list.
    empty_list = []
    insert_at(empty_list, 0, 42)
    print("After inserting 42 into an empty list:", empty_list)

    # Edge Case 4: Attempt to delete from an empty list.
    # Since there is no valid index, the function safely returns None.
    empty_delete = delete_at(empty_list, 5)
    print("Attempting to delete invalid index from the list:", empty_delete)


if __name__ == "__main__":
    main()