from collections import deque

start = ('door','window','middle',False)
pos = ['door','window','middle']

def bfs():
    q = deque([start])
    vis = set()
    step = 1

    while q:
        s = q.popleft()
        if s in vis: 
            continue

        vis.add(s)
        print(f"Step {step}: {s}")
        step += 1

        m,b,ba,has = s
        if has:
            print("\nBanana obtained!")
            return

        # move
        for p in pos:
            if p != m:
                q.append((p,b,ba,has))

        # push
        if m == b:
            for p in pos:
                if p != b:
                    q.append((p,p,ba,has))

        # grab
        if m == b == ba:
            q.append((m,b,ba,True))

bfs()
