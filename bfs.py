from collections import deque

def BFS(start, graph):
    queue = deque([start])
    explored = []
    step = 1

    print("Step\tQueue (frontier)\tExplored")

    while queue:
        print(step, "\t", list(queue), "\t\t", explored)
        current = queue.popleft()
        explored.append(current)

        for neighbour in graph[current]:
            if neighbour not in explored and neighbour not in queue:
                queue.append(neighbour)

        step += 1

    print(step, "\t", list(queue), "\t\t", explored)


graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}

BFS(1, graph)

'''Step    Queue (frontier)        Explored
1        [1]             []
2        [2, 3]                  [1]
3        [3, 4, 5]               [1, 2]
4        [4, 5, 6]               [1, 2, 3]
5        [5, 6]                  [1, 2, 3, 4]
6        [6]             [1, 2, 3, 4, 5]
7        []              [1, 2, 3, 4, 5, 6]'''