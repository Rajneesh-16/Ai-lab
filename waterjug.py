from collections import deque

def solve_water_jug(jug1_cap, jug2_cap, target):
    # Queue stores (amt_in_jug1, amt_in_jug2, path_taken)
    queue = deque([(0, 0, [])])
    visited = set([(0, 0)])

    while queue:
        j1, j2, path = queue.popleft()

        # Check if we reached the target in either jug
        if j1 == target or j2 == target:
            return path + [(j1, j2)]

        # Define all possible moves
        moves = [
            (jug1_cap, j2),        # Fill Jug 1
            (j1, jug2_cap),        # Fill Jug 2
            (0, j2),               # Empty Jug 1
            (j1, 0),               # Empty Jug 2
            # Pour Jug 1 -> Jug 2
            (j1 - min(j1, jug2_cap - j2), j2 + min(j1, jug2_cap - j2)),
            # Pour Jug 2 -> Jug 1
            (j1 + min(j2, jug1_cap - j1), j2 - min(j2, jug1_cap - j1))
        ]

        for move in moves:
            if move not in visited:
                visited.add(move)
                queue.append((move[0], move[1], path + [(j1, j2)]))

    return None

# Parameters: Jug 1 Capacity, Jug 2 Capacity, Target
jug1, jug2, goal = 4, 3, 2
solution = solve_water_jug(jug1, jug2, goal)

if solution:
    print(f"Steps to get {goal} gallons:")
    for step in solution:
        print(step)
else:
    print("No solution possible.")

    '''Steps to get 2 gallons:
(0, 0)
(0, 3)
(3, 0)
(3, 3)
(4, 2)'''