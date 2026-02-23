from collections import deque

# State = (monkey_pos, box_pos, banana_pos, has_banana)
start = ('door', 'floor', 'middle', False)
goal = lambda s: s[3] is True

actions = [
    lambda s: ('middle', s[1], s[2], s[3]) if s[0] != 'middle' else None,          # move
    lambda s: ('middle', 'middle', s[2], s[3]) if s[0] == s[1] else None,          # push box
    lambda s: ('middle', 'middle', 'middle', s[3]) if s[1] == 'middle' else None, # climb
    lambda s: ('middle', 'middle', 'middle', True) if s[0]==s[1]==s[2] else None  # grab
]

def bfs():
    q = deque([(start, [])])
    visited = {start}
    step = 1

    while q:
        state, path = q.popleft()
        print(f"Step {step}: {state}")
        step += 1

        if goal(state):
            print("\n Banana obtained!")
            for p in path:
                print(p)
            print("Final State:", state)
            return

        for a in actions:
            ns = a(state)
            if ns and ns not in visited:
                visited.add(ns)
                q.append((ns, path + [ns]))

bfs()

'''Step 1: ('door', 'floor', 'middle', False)
Step 2: ('middle', 'floor', 'middle', False)'''