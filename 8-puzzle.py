import heapq

goal = "123456780"

# Heuristic: Manhattan Distance
def h(s):
    return sum(abs(i//3 - int(v)//3) + abs(i%3 - int(v)%3)
               for i,v in enumerate(s) if v!='0')

def show(s):
    for i in range(0,9,3): print(s[i:i+3])
    print()

def solve(start):
    pq = [(h(start), 0, start, [])]
    seen = set()
    
    while pq:
        f, g, s, path = heapq.heappop(pq)
        
        if s == goal:
            print("Steps:", len(path))
            for state in path + [s]:
                show(state)
            return
        
        if s in seen: continue
        seen.add(s)
        
        i = s.index('0')
        for d in [-1,1,-3,3]:
            j = i + d
            if 0 <= j < 9 and (i//3 == j//3 or d in [-3,3]):
                ns = list(s)
                ns[i], ns[j] = ns[j], ns[i]
                ns = ''.join(ns)
                heapq.heappush(pq, (g+1+h(ns), g+1, ns, path+[s]))

# Example
solve("123405678")