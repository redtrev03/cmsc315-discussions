"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

This program demonstrates how a Binary Search Tree (BST)
stores, searches, and traverses values.
"""


class Node:
    def __init__(self, value):
        # Store the value contained in this node.
        self.value = value

        # Each node can have a left and right child.
        # They start as None because the node has no children yet.
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # The root is the starting point of the tree.
        # None means the tree is initially empty.
        self.root = None

    def insert(self, value):
        """
        Insert a value into the BST.

        The recursive helper is used to find the correct
        location for the new value.
        """

        # If the tree is empty, the new node becomes the root.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        Recursively insert a value into the BST.
        """

        # If we reach an empty position, create a new node.
        if node is None:
            return Node(value)

        # Smaller values belong in the left subtree.
        # This keeps all smaller values on the left side.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values belong in the right subtree.
        # This keeps all larger values on the right side.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Duplicate values are ignored in this implementation.
        # The existing node remains unchanged.

        # Return the current node so the tree connections
        # are maintained as recursion moves back upward.
        return node

    def search(self, value):
        """
        Search for a value in the BST.

        Returns True if the value exists and False otherwise.

        BST search is often more efficient than linear search
        because each comparison eliminates an entire subtree.
        In a balanced BST, this can reduce the search time to
        approximately O(log n), compared with O(n) for a
        linear search.
        """

        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        Recursively search for a value in the BST.
        """

        # If we reach None, the value is not in the tree.
        if node is None:
            return False

        # The value was found.
        if value == node.value:
            return True

        # If the search value is smaller, only search the left
        # subtree because larger values cannot be there.
        if value < node.value:
            return self._search_recursive(node.left, value)

        # If the search value is larger, only search the right
        # subtree.
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        Return a list containing the values from an
        in-order traversal.
        """

        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        Perform an in-order traversal.

        The order is:
        1. Left subtree
        2. Current node
        3. Right subtree

        Because a BST stores smaller values on the left and
        larger values on the right, visiting nodes in this
        order produces the values in sorted order.
        """

        # Stop when there is no node to visit.
        if node is None:
            return

        # First visit all smaller values.
        self._inorder_recursive(node.left, values)

        # Then visit the current node.
        values.append(node.value)

        # Finally visit all larger values.
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # BUILD A TREE
    # ===============================

    print("\n=== TREE CONSTRUCTION ===")

    # Create an empty BST.
    tree = BST()

    # Insert seven values.
    # 50 becomes the root.
    # Smaller values are placed on the left.
    # Larger values are placed on the right.
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]

    for value in values_to_insert:
        tree.insert(value)

    print("Values inserted:", values_to_insert)

    # The BST reduces the search space because each comparison
    # tells us whether to continue searching left or right.
    # For example, if searching for 20, we start at 50 and know
    # immediately that 20 can only be in the left subtree.

    print("Tree created successfully.")

    # ===============================
    # IN-ORDER TRAVERSAL
    # ===============================

    print("\n=== IN-ORDER TRAVERSAL ===")

    traversal = tree.inorder()

    print("In-order traversal:", traversal)

    # In-order traversal visits the left subtree first,
    # then the current node, and finally the right subtree.
    # Since the BST keeps smaller values on the left and larger
    # values on the right, the resulting list is sorted.

    print("The traversal is sorted because of the BST structure.")

    # ===============================
    # SEARCH TESTS
    # ===============================

    print("\n=== SEARCH TESTS ===")

    # These values exist in the tree.
    print("Searching for 40:", tree.search(40))
    print("Searching for 80:", tree.search(80))

    # These values do not exist in the tree.
    print("Searching for 25:", tree.search(25))
    print("Searching for 90:", tree.search(90))

    # The successful searches return True because those values
    # are present in the tree. The unsuccessful searches return
    # False because the recursive search eventually reaches
    # an empty position.

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    # Test an empty tree.
    empty_tree = BST()

    print("Empty tree in-order traversal:", empty_tree.inorder())
    print("Search empty tree for 10:", empty_tree.search(10))

    # An empty tree has no root, so its traversal returns an
    # empty list and its search returns False.
    # This demonstrates that the program can safely handle
    # a tree before any values have been inserted.

    # Test a single-node tree.
    single_node_tree = BST()
    single_node_tree.insert(100)

    print("Single-node tree traversal:", single_node_tree.inorder())
    print("Search single-node tree for 100:",
          single_node_tree.search(100))
    print("Search single-node tree for 50:",
          single_node_tree.search(50))


if __name__ == "__main__":
    main()