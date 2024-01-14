import sys
from collections import deque
input = sys.stdin.readline

def remove(x, y, state, n, m): #왼, 오, 위, 아 지우는 함수
    if x < 0 or x >= n or y < 0 or y >= m:
        return 0
    if y >= 0:
        if x-1 >= 0 and state[y][x-1] == 'X':
            state[y][x-1] = '*'
        if x+1 < n and state[y][x+1] == 'X':
            state[y][x+1] = '*'
    if x >= 0:
        if y-1 >= 0 and state[y-1][x] == 'X':
            state[y-1][x] = '*'
        if y+1 < m and state[y+1][x] == 'X':
            state[y+1][x] = '*'

def state_set(m, n, state):
    for i in range(m):
        for j in range(n):
            if state[i][j] == '*':
                state[i][j] = '.'

def dfs(x, y, state, m, n, check):
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if state[y][x] != 'X' and check[y][x] == 0:
        check[y][x] = 1
        dfs(x - 1, y, state, m, n, check)
        dfs(x + 1, y, state, m, n, check)
        dfs(x, y - 1, state, m, n, check)
        dfs(x, y + 1, state, m, n, check)

m, n = map(int, input().split()) #m:r, n:c
state = [] #현재상태
l = []

for i in range(m):
    list_r = list(map(str, input().strip()))
    state.append(list_r)
#print(state)
for i in range(m):
    for j in range(n):
        if state[i][j] == 'L':
            l.append([i, j])
count = 0
#print(l)
if len(l) == 1 or len(l) == 0:
    print(0)
    exit()

x, y = l[0][1], l[0][0]
x_t, y_t = l[1][1], l[1][0]
check = [[0] * n for _ in range(m)]
dfs(x, y, state, m, n, check)

while check[y_t][x_t] == 0:
    for i in range(m):
        for j in range(n):
            if state[i][j] == '.':
                remove(j, i, state, n, m)
    #print(state)
    state_set(m, n, state)
    count += 1
    check = [[0] * n for _ in range(m)]
    dfs(x, y, state, m, n, check)

print(count)