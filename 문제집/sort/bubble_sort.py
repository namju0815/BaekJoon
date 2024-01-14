# # 23970
# import sys
# input = sys.stdin.readline
#
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
#
# count = 0
# for j in range(N - 1, 0, -1):
#     for i in range(j):
#         if A[i] > A[i + 1]:
#             A[i], A[i + 1] = A[i + 1], A[i]
#             count += 1
#             if count == K:
#                 print(A[i], A[i+1])
#                 sys.exit()
#
# if count < K:
#     print(-1)

# #24046
# import sys
# input = sys.stdin.readline
#
# N, K = map(int, input().split())
# n = N - 1
# A = list(map(int, input().split()))
# count = 0
#
# for _ in range(N):
#     i = max(A)
#     maxIndex = A.index(i)#최댓값의 인덱스 값 찾기
#     if maxIndex >= 2:
#         for k in range(maxIndex-1):
#             if A[k] > A[k+1]:
#                 A[k], A[k+1] = A[k+1], A[k]
#                 count += 1
#                 if K == count:
#                     print(A[k], A[k+1])
#                     sys.exit()
#     count += n-maxIndex
#     n -= 1
#     A.pop(maxIndex)
#     #print(A)
#     #print(count)
#     if K <= count:
#         index = K-count-1
#         print(A[index], i)
#         sys.exit()
#
# if count < K:
#     print(-1)

# #23968 23969
# import sys
# input = sys.stdin.readline
#
# N = int(input())
# A = list(map(int, input().split()))
# arr = list(map(int, input().split()))
# check = 0
# count = 0
# for j in range(N-1, 0, -1):
#     for i in range(j):
#         if A[i] > A[i+1]:
#             A[i], A[i+1] = A[i+1], A[i]
#             count += 1
#         if A == arr:
#             check = 1
#             break
#
# print(check)

# import sys
# input = sys.stdin.readline
#
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
#
# count = 0
# for j in range(N - 1, 0, -1):
#     for i in range(j):
#         if A[i] > A[i + 1]:
#             A[i], A[i + 1] = A[i + 1], A[i]
#             count += 1
#             if count == K:
#                 for i in A:
#                     print(i, end=" ")
#                 sys.exit()
# if count < K:
#     print(-1)

# #2605
# import sys
# input = sys.stdin.readline
# n = int(input())
# students = list(map(int, input().split()))
# answer = []
#
# pre = -1
# index = 1
# for i in students:
#     if pre < i:
#         answer.append(index)
#     else:
#         answer.insert(i, index)
#     pre += 1
#     index += 1
# for i in answer[::-1]:
#     print(i, end=" ")

