"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # CREATE A HASH TABLE
    # ===============================
    #
    # A Python dictionary works similarly to a hash table
    # because it stores data using key-value pairs. The key
    # is used to find the associated value efficiently.
    #
    # Create an empty dictionary first.
    inventory = {}

    # Add five key-value pairs to the dictionary.
    inventory["Laptop"] = 10
    inventory["Keyboard"] = 25
    inventory["Mouse"] = 30
    inventory["Monitor"] = 15
    inventory["Headset"] = 20

    print("\n=== INSERT OPERATIONS ===")
    print("Inventory after inserting five items:")
    print(inventory)

    # ===============================
    # LOOKUP OPERATIONS
    # ===============================
    #
    # Dictionary lookups use a key to retrieve its associated
    # value. Python uses the dictionary's hash table structure
    # to locate the value efficiently.

    print("\n=== LOOKUP OPERATIONS ===")

    laptop_quantity = inventory["Laptop"]
    mouse_quantity = inventory["Mouse"]

    print("Laptop quantity:", laptop_quantity)
    print("Mouse quantity:", mouse_quantity)

    # ===============================
    # UPDATE OPERATIONS
    # ===============================
    #
    # Assigning a new value to an existing key updates the
    # value associated with that key. The key remains in the
    # dictionary, but its value is replaced.

    print("\n=== UPDATE OPERATIONS ===")

    print("Dictionary before update:")
    print(inventory)

    inventory["Laptop"] = 12

    print("Dictionary after updating Laptop quantity:")
    print(inventory)

    # ===============================
    # DELETE OPERATIONS
    # ===============================
    #
    # The del statement removes the specified key and its
    # associated value from the dictionary.

    print("\n=== DELETE OPERATIONS ===")

    print("Dictionary before deletion:")
    print(inventory)

    del inventory["Headset"]

    print("Dictionary after deleting Headset:")
    print(inventory)

    # ===============================
    # EDGE CASES
    # ===============================
    #
    # Edge case 1: Looking up a key that does not exist.
    # Using the get() method allows the program to safely
    # handle a missing key without causing a KeyError.

    print("\n=== EDGE CASES ===")

    missing_item = inventory.get("Printer")

    if missing_item is None:
        print("Lookup for Printer: Key not found.")
    else:
        print("Printer quantity:", missing_item)

    # Edge case 2: Attempting to delete a key that does not
    # exist. Checking whether the key exists first prevents
    # the program from causing a KeyError.

    if "Tablet" in inventory:
        del inventory["Tablet"]
        print("Tablet was deleted.")
    else:
        print("Delete attempt for Tablet: Key not found, so nothing was deleted.")

    # Edge case 3: Updating a key that does not exist.
    # Assigning a value to a new key adds that key to the
    # dictionary instead of producing an error.

    inventory["Printer"] = 5
    print("Printer was not previously in the dictionary, so it was added.")
    print("Final dictionary:")
    print(inventory)


if __name__ == "__main__":
    main()