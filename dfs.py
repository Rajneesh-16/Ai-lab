def dfs_with_steps(graph, start):
    stack = [start]
    explored = []
    step = 1

    print("Step\tStack (frontier)\tExplored")

    while stack:
        print(step, "\t", stack, "\t\t", explored)
        current = stack.pop()

        if current not in explored:
            explored.append(current)
            for neighbour in reversed(graph[current]):
                if neighbour not in explored and neighbour not in stack:
                    stack.append(neighbour)

        step += 1

    print(step, "\t", stack, "\t\t", explored)


graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}
dfs_with_steps(graph, 1)

'''Step    Stack (frontier)        Explored
1        [1]             []
2        [3, 2]                  [1]
3        [3, 5, 4]               [1, 2]
4        [3, 5]                  [1, 2, 4]
5        [3]             [1, 2, 4, 5]
6        [6]             [1, 2, 4, 5, 3]
7        []              [1, 2, 4, 5, 3, 6]'''