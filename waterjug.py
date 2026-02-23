from collections import deque

def water_jug():
    visited = set()
    queue = deque([((0, 0), [])])

    while queue:
        (a, b), path = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        path = path + [(a, b)]

        if a == 2:
            return path

        moves = [
            (4, b),                         # Fill jug A
            (a, 3),                         # Fill jug B
            (0, b),                         # Empty jug A
            (a, 0),                         # Empty jug B
            (a - min(a, 3 - b), b + min(a, 3 - b)),  # Pour A -> B
            (a + min(b, 4 - a), b - min(b, 4 - a))   # Pour B -> A
        ]

        for move in moves:
            if move not in visited:
                queue.append((move, path))


solution = water_jug()

for step in solution:
    print(step)

'''(0, 0)
(4, 0)
(1, 3)
(1, 0)
(0, 1)
(4, 1)
(2, 3)'''