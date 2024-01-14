# #17298
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n = int(input())
# case = list(map(int, input().split()))
#
# sub_case = deque()
# sub_case = [case[-1]]
# answer = [-1]
# index = n-2
# while index >= 0:
#     data = case[index]
#     #print(i, end=" ")
#     if len(sub_case) == 0:
#         answer.append(-1)
#         sub_case.append(data)
#         index -= 1
#         continue
#     target = sub_case[-1]
#     if target > data:
#         answer.append(target)
#         sub_case.append(data)
#         index -= 1
#     else:
#         sub_case.pop()
#
# for i in answer[::-1]:
#     print(i, end=" ")

# #10816
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# dic_card = {}
#
# for i in input().split():
#     if i in dic_card:
#         dic_card[i] += 1
#     else:
#         dic_card[i] = 1
#
# t = int(input())
# for i in input().split():
#     if i in dic_card:
#         print(dic_card[i], end=" ")
#     else:
#         print(0, end=" ")

# #1927 최소힙
# import sys, heapq
# input = sys.stdin.readline
#
# heap = []
# t = int(input())
#
# for i in range(t):
#     num = int(input())
#     if num == 0:
#         if len(heap) == 0:
#             print(0)
#         else:
#             print(heapq.heappop(heap))
#     else:
#         heapq.heappush(heap, num)

# #11279 최대힙
# import sys, heapq
# input = sys.stdin.readline
#
# heap = []
# t = int(input())
#
# for i in range(t):
#     num = int(input())
#     if num == 0:
#         if len(heap) == 0:
#             print(0)
#         else:
#             print(heapq.heappop(heap)[1])
#     else:
#         heapq.heappush(heap, (-num, num))

# #11286
# import sys, heapq
# input = sys.stdin.readline
#
# heap = []
# t = int(input())
#
# for i in range(t):
#     num = int(input())
#     if num == 0:
#         if len(heap) == 0:
#             print(0)
#         else:
#             print(heapq.heappop(heap)[1])
#     else:
#         heapq.heappush(heap, (abs(num), num))

# #5430
# import sys
# input = sys.stdin.readline
#
# t = int(input())
# for i in range(t):
#     error = 0
#     p = input().strip()
#     n = int(input())
#     X = input().strip()[1:-1].split(',')
#     if n == 0 and 'D' in X:
#         print('error')
#         continue
#
#     if X == ['']:
#         X = []
#
#     r = 0
#     front = 0
#     rear = n-1
#     for j in p:
#        if j == 'R':
#           r = 1 - r
#        else:
#            if front > rear:
#                print('error')
#                error = 1
#                break
#            else:
#                if r == 0:
#                   front += 1
#                else:
#                    rear -= 1
#
#     if error == 0:
#         if r == 0:
#             X = list(map(int, X[front:rear+1]))
#         else: #r==1
#             if front == 0:
#                 X = list(map(int, X[rear::-1]))
#             else:
#                 X = list(map(int, X[rear:front-1:-1]))
#         result = '[' + ','.join(map(str, X)) + ']'
#         print(result)

# #1406
# import sys
# input = sys.stdin.readline
#
# left_stack = list(input().strip())
# right_stack = []
# t = int(input())
#
# for _ in range(t):
#     inp = input().split()
#     if inp[0] == 'L'and left_stack:#옮길 커서가 있을 때
#         right_stack.append(left_stack.pop())
#     elif inp[0] == 'D'and right_stack:
#         left_stack.append(right_stack.pop())
#     elif inp[0] == 'B'and left_stack:
#         left_stack.pop()
#     elif inp[0] == 'P':
#         left_stack.append(inp[1])
#
# print(''.join(left_stack+list(reversed(right_stack))))

#17219
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = {}
for _ in range(n):
    site, password = input().split()
    l[site] = password

for _ in range(m):
    print(l[input().strip()])