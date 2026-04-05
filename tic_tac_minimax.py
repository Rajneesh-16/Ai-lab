import random, time

b=[' ']*9
w=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def win(p): return any(all(b[i]==p for i in c) for c in w)

def mm(p):
    if win('X'): return 1
    if win('O'): return -1
    if ' ' not in b: return 0
    s=[]
    for i in range(9):
        if b[i]==' ':
            b[i]=p
            s.append(mm('O' if p=='X' else 'X'))
            b[i]=' '
    return max(s) if p=='X' else min(s)

t='X'
while ' ' in b and not(win('X') or win('O')):
    print(f"Player {t}'s turn:")
    m=[]
    for i in range(9):
        if b[i]==' ':
            b[i]=t
            s=mm('O' if t=='X' else 'X')
            b[i]=' '
            m.append((s,i))
    bs=(max(m)[0] if t=='X' else min(m)[0])
    b[random.choice([i for s,i in m if s==bs])]=t
    for i in range(0,9,3): print(b[i],'|',b[i+1],'|',b[i+2])
    print('-'*10)
    t='O' if t=='X' else 'X'
    time.sleep(1)

print("Game Over:", "X Wins" if win('X') else "O Wins" if win('O') else "Draw")