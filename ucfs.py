import heapq

graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('C', 2), ('D', 4), ('E', 1)],
    'C': [('D', 3), ('E', 6)],
    'D': [('E', 2)],
    'E': []
}

start = 'A'
goal = 'E'

def lowest_cost_first_search():
    queue = []
    heapq.heappush(queue, (0, start, [start]))
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node == goal:
            print("Shortest Path:", path)
            print("Total Cost:", cost)
            return

        if node in visited:
            continue

        visited.add(node)

        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    queue,
                    (cost + edge_cost, neighbor, path + [neighbor])
                )

    print("No path found")

lowest_cost_first_search()


'''Shortest Path: ['A', 'B', 'E']
Total Cost: 3'''