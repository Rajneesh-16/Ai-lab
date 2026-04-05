import random, time

b=[' ']*9
w=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def win(p): return any(all(b[i]==p for i in c) for c in w)

def ab(p,a,beta):
    if win('X'): return 1
    if win('O'): return -1
    if ' ' not in b: return 0
    
    if p=='X':
        v=-2
        for i in range(9):
            if b[i]==' ':
                b[i]=p
                v=max(v,ab('O',a,beta))
                b[i]=' '
                a=max(a,v)
                if a>=beta: break
        return v
    else:
        v=2
        for i in range(9):
            if b[i]==' ':
                b[i]=p
                v=min(v,ab('X',a,beta))
                b[i]=' '
                beta=min(beta,v)
                if beta<=a: break
        return v

t='X'
while ' ' in b and not(win('X') or win('O')):
    print(f"Player {t}'s turn:")
    m=[]
    for i in range(9):
        if b[i]==' ':
            b[i]=t
            s=ab('O' if t=='X' else 'X',-2,2)
            b[i]=' '
            m.append((s,i))
    
    bs=(max(m)[0] if t=='X' else min(m)[0])
    b[random.choice([i for s,i in m if s==bs])]=t
    
    for i in range(0,9,3): print(b[i],'|',b[i+1],'|',b[i+2])
    print('-'*10)
    
    t='O' if t=='X' else 'X'
    time.sleep(1)

print("Game Over:", "X Wins" if win('X') else "O Wins" if win('O') else "Draw")