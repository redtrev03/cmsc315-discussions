"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

This program demonstrates Breadth-First Search (BFS) using
an adjacency-list graph. The graph represents locations
connected by paths, and BFS is used to visit each location
level by level.
===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    Perform Breadth-First Search (BFS) on a graph.

    BFS uses a queue so that nodes are processed in the
    order they are discovered. This allows BFS to visit
    nodes level by level before moving farther from the
    starting node.
    """

    # If the starting node does not exist, return an empty list.
    if start not in graph:
        return []

    # The queue keeps track of nodes waiting to be visited.
    # A queue follows First-In, First-Out (FIFO) order.
    queue = deque([start])

    # The visited set prevents the same node from being
    # visited multiple times.
    visited = {start}

    # This list stores the order in which nodes are visited.
    traversal_order = []

    while queue:
        # Remove the next node from the front of the queue.
        current = queue.popleft()

        # Record the node when it is visited.
        traversal_order.append(current)

        # Add each unvisited neighbor to the queue.
        # Neighbors are added so BFS can process them
        # after the current level has been completed.
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # BFS differs from depth-first search because BFS uses
    # a queue to explore level by level. DFS typically uses
    # a stack or recursion to follow one path as deeply as
    # possible before backtracking.
    return traversal_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # CREATE A GRAPH
    # ===============================
    #
    # The graph represents locations on a campus.
    # Each node represents a building, and each edge
    # represents a path between two buildings.
    #
    # The graph is represented using an adjacency list.
    # Each key is a building, and its list contains the
    # buildings that can be reached directly from it.

    graph = {
        "Library": ["Student Center", "Science Building"],
        "Student Center": ["Library", "Gym", "Administration"],
        "Science Building": ["Library", "Engineering Building"],
        "Gym": ["Student Center", "Administration"],
        "Administration": ["Student Center", "Gym", "Engineering Building"],
        "Engineering Building": ["Science Building", "Administration"]
    }

    print("\n=== GRAPH STRUCTURE ===")

    for building, connections in graph.items():
        print(f"{building} -> {connections}")

    # ===============================
    # BFS TRAVERSAL
    # ===============================

    print("\n=== BFS TRAVERSAL ===")

    # Start BFS at the Library.
    start = "Library"

    traversal = bfs(graph, start)

    print(f"Starting node: {start}")
    print("BFS traversal order:")
    print(" -> ".join(traversal))

    print("\nBFS visits the graph level by level.")
    print("Starting from the Library, BFS first visits its")
    print("direct neighbors before moving to buildings farther away.")

    # ===============================
    # ADD AN ADDITIONAL NODE/EDGE
    # ===============================

    print("\n=== UPDATED GRAPH ===")

    # Add a new location to the graph.
    # The Parking Lot is connected to the Gym.
    graph["Parking Lot"] = ["Gym"]
    graph["Gym"].append("Parking Lot")

    for building, connections in graph.items():
        print(f"{building} -> {connections}")

    # Perform BFS again after adding the new location.
    updated_traversal = bfs(graph, "Library")

    print("\nUpdated BFS traversal starting from Library:")
    print(" -> ".join(updated_traversal))

    # ===============================
    # EDGE CASE TESTS
    # ===============================

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Missing starting node
    #
    # The starting node does not exist in the graph.
    # The bfs() function safely returns an empty list.
    missing_start = bfs(graph, "Cafeteria")

    print("\n1. Missing starting node:")
    print("Start node: Cafeteria")
    print(f"BFS result: {missing_start}")
    print("The function returns an empty list because the")
    print("starting node is not present in the graph.")

    # Edge Case 2: Disconnected graph
    #
    # The Dormitory is not connected to any of the other
    # buildings. BFS starting from Library will not reach it.
    disconnected_graph = {
        "Library": ["Student Center"],
        "Student Center": ["Library"],
        "Dormitory": []
    }

    disconnected_traversal = bfs(disconnected_graph, "Library")

    print("\n2. Disconnected graph:")
    print(f"BFS starting from Library: {disconnected_traversal}")
    print("The Dormitory is not visited because there is no")
    print("path connecting it to the Library.")

    # Edge Case 3: Graph containing only one node
    #
    # BFS should simply visit the starting node.
    single_node_graph = {
        "Library": []
    }

    single_node_traversal = bfs(single_node_graph, "Library")

    print("\n3. Single-node graph:")
    print(f"BFS starting from Library: {single_node_traversal}")
    print("The only node is visited, and the traversal is complete.")


if __name__ == "__main__":
    main()