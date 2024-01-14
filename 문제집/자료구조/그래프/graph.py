#그래프
# graph = {1:[2, 3, 4], 2:[5], 3:[5], 4:[], 5:[6, 7], 6:[], 7:[]}
#
# #DFS(깊이 우선 탐색) 그래프구현
# dfs_visited=[]
# def dfs(v, visited): #시작 노드와 방문순서 리스트
#     visited.append(v)
#     for i in graph[v]:
#         if not i in visited:
#             visited = dfs(i,visited)
#     return visited
#
# print(dfs(1, dfs_visited))
#
# #BFS(너비 우선 탐색) 그래프구현
# from collections import deque
# def bfs(v):
#     visited = [v]
#     que = deque([v])
#     while que:
#         v = que.popleft() #맨 앞 노드 빼기
#         for i in graph[v]:
#             if not i in visited:
#                 visited.append(i)
#                 que.append(i)
#     return visited
#
# print(bfs(1))

# #1260
# from collections import deque
# import sys
# input = sys.stdin.readline
#
# def create_gragh(n, m):
#     graph = [[] for _ in range(n+1)]
#     for _ in range(m):
#         n1, n2 = map(int, input().split())
#         graph[n1].append(n2)
#         graph[n2].append(n1)
#     return graph
#
# def dfs(v, visited):
#     visited[v] = True
#     print(v, end=" ")
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(i, visited)
#
# def bfs(v):
#     visited = [False] * (n+1)
#     que = deque([v])
#     visited[v] = True
#     while que:
#         v = que.popleft()
#         print(v, end=" ")
#         for i in graph[v]:
#             if not visited[i]:
#                 visited[i] = True
#                 que.append(i)
#
#
# n, m, s = map(int, input().split())
# graph = create_gragh(n, m)
# for index in range(n+1):
#     graph[index].sort()
# #print(graph)
# dfs_visited = [False] * (n+1)
# dfs(s, dfs_visited)
# print()
# bfs(s)

# #11724
# import sys
# sys.setrecursionlimit(10**6)  # 재귀 호출 깊이 한계를 늘립니다.
# input = sys.stdin.readline
#
# def create_graph(n, m):
#     graph = [[] for _ in range(n+1)]
#     for _ in range(m):
#         a, b = map(int, input().split())
#         graph[a].append(b)
#         graph[b].append(a)
#     return graph
#
# def dfs(v, visited, count):
#     visited[v] = count
#     #print(v, end=" ")
#     for i in graph[v]:
#         if visited[i] != count:
#             dfs(i, visited, count)
#
# n, m = map(int, input().split())
# graph = create_graph(n, m) #그래프 생성
#
# visited = [0] * (n + 1)
# count = 1
# for i in range(1, n+1):
#     if visited[i] == 0:
#         dfs(i, visited, count)
#         count += 1
# #print()
# #print(visited)
# a = set(visited)
# print(len(a)-1)

# #2606
# import sys
# input = sys.stdin.readline
#
# def create_graph(c, t):
#     graph =[[] for _ in range(c+1)]
#     for _ in range(t):
#         a, b = map(int, input().split())
#         graph[a].append(b)
#         graph[b].append(a)
#     return graph
#
# def dfs(v, visited):
#     global count
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(i, visited)
#             count += 1
#
# c = int(input())
# t = int(input())
# count = 0
# graph = create_graph(c, t)
# visited = [False] * (c+1)
# dfs(1, visited)
# print(count)

# #7576
# import sys
# input = sys.stdin.readline
# count = 0
# tomato = []
# n, m = map(int, input().split())
#
# for _ in range(m):
#     tomato.append(list(map(int, input().split())))

# 1012
# import sys
# input = sys.stdin.readline
# def dfs(x, y, state, check, c, n, m):
#     if x < 0 or x >= m or y < 0 or y >= n:
#         return
#     if state[y][x] and check[y][x] == 0:
#         check[y][x] = c
#         dfs(x - 1, y, state, check, c, n, m)
#         dfs(x + 1, y, state, check, c, n, m)
#         dfs(x, y - 1, state, check, c, n, m)
#         dfs(x, y + 1, state, check, c, n, m)
#
# n = int(input())
# for i in range(n):
#     m, n, k = map(int, input().split())
#     check = [[0] * m for _ in range(n)]
#     state = [[False] * m for _ in range(n)]
#     #print(check)
#     for j in range(k):
#         a, b = map(int, input().split())
#         state[b][a] = True
#     #print(state)
#     if m * n == k or k == 1:
#         print(1)
#         continue
#     c = 1
#     for i in range(n):
#         for j in range(m):
#             if state[i][j] and check[i][j] == 0:
#                 dfs(j, i, state, check, c, n, m)
#                 c += 1
#     s = set(check[y][x] for y in range(n) for x in range(m))
#     s.discard(0)
#     print(len(s))

# #2583
# import sys
# sys.setrecursionlimit(10000000)
# input = sys.stdin.readline
# def dfs(x, y, state, check, c, m, n):
#     if x < 0 or x >= n or y < 0 or y >= m:
#         return
#     if state[y][x] and check[y][x] == 0:
#         check[y][x] = c
#         dfs(x - 1, y, state, check, c, m, n)
#         dfs(x + 1, y, state, check, c, m, n)
#         dfs(x, y - 1, state, check, c, m, n)
#         dfs(x, y + 1, state, check, c, m, n)
#
# m, n, k = map(int, input().split()) #m:세로, n:가로
# check = [[0] * n for _ in range(m)]
# state = [[True] * n for _ in range(m)]
#
# for _ in range(k):
#     x1, y1, x2, y2 = map(int, input().split())
#     for i in range(y1, y2):
#         for j in range(x1, x2):
#             state[i][j] = False
# #print(state)
# c1 = 1
# for i in range(m):
#     for j in range(n):
#         if state[i][j] and check[i][j] == 0:
#             dfs(j, i, state, check, c1, m, n)
#             c1 += 1
#
# #print(check)
# s = set(check[y][x] for y in range(m) for x in range(n))
# s.discard(0)
#
# area = []
# for i in s:
#     c = 0
#     for j in range(m):
#         c += check[j].count(i)
#     area.append(c)
#
# area.sort()
# print(len(s))
# for i in area:
#     print(i, end=" ")

# #2667
# import sys
# input = sys.stdin.readline
#
# def dfs(x, y, state, check, c, N):
#     if x < 0 or x >= N or y < 0 or y >= N:
#         return
#     if state[y][x] and check[y][x] == 0:
#         check[y][x] = c
#         dfs(x - 1, y, state, check, c, N)
#         dfs(x + 1, y, state, check, c, N)
#         dfs(x, y - 1, state, check, c, N)
#         dfs(x, y + 1, state, check, c, N)
#
# N = int(input())
# state = []
# check = [[0]*N for _ in range(N)]
# for i in range(N):
#     state.append(list(map(int, list(input())[:-1])))
# #print(state)
#
# c = 1
# for i in range(N):
#     for j in range(N):
#         if state[i][j] and check[i][j] == 0:
#                  dfs(j, i, state, check, c, N)
#                  c += 1
#
# s = set(check[y][x] for y in range(N) for x in range(N))
# s.discard(0)
# print(len(s))
# area = []
# for i in s:
#     c = 0
#     for j in range(N):
#         c += check[j].count(i)
#     area.append(c)
#
# area.sort()
# for i in area:
#     print(i)

#7576
import sys
input = sys.stdin.readline

def dfs(x, y, state, m, n):
    if x < 0 or x >= m or y < 0 or y >= n:
        return
    if state[y][x] == 1:
        state[y][x] == 1
        dfs(x - 1, y, state, m, n)
        dfs(x + 1, y, state, m, n)
        dfs(x, y - 1, state, m, n)
        dfs(x, y + 1, state, m, n)

m, n = map(int, input().split())
state = []

for i in range(n):
    state.append(list(map(int, input().split())))
#print(state)

count = 0
for i in range(n):
    for j in range(m):
        if state[i][j] == 1:
            dfs(j, i, state, m, n)
print(count)