# #12015
# import sys
# input = sys.stdin.readline
# n = int(input())
# A = list(map(int, input().split()))
# memo = [0]
#
# for case in A:
#     if memo[-1] < case:
#         memo.append(case)
#
#     else:
#         left = 0
#         right = len(memo)
#         while left < right:
#             mid = (left+right)//2
#             if memo[mid] < case:
#                 left = mid + 1
#             else:
#                 right = mid
#         memo[right] = case
#     print(memo)
# print(len(memo)-1)

# #12738
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# A = list(map(int, input().split()))
#
# def binary_search(start, end, data):
#     if start > end:
#         return start
#     mid = (start+end)//2
#     if memo[mid] < data:
#         return binary_search(mid+1, end, data)
#     elif memo[mid] == data:
#         return mid
#     else:
#         return binary_search(start, mid-1, data)
#
# memo = [A[0]]
# for case in A[1:]:
#     if memo[-1] < case:
#         memo.append(case)
#     else:
#         right = len(memo) - 1
#         memo[binary_search(0, right, case)] = case
#     #print(memo)
# print(len(memo))

# # #14002 -1
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# A = list(map(int, input().split()))
#
# def binary_search(i, start, end, data):
#     if start > end:
#         return end
#     mid = (start+end)//2
#     if memo[i][mid] < data:
#         return binary_search(i, mid+1, end, data)
#     elif memo[i][mid] == data:
#         return mid
#     else:
#         return binary_search(i, start, mid-1, data)
#
# memo = [[A[0]]]
# for case in A[1:]:
#     l = len(memo)
#     for i in range(l):
#         if memo[i][-1] < case:
#             memo[i].append(case)
#         else:
#             memo.append(list(memo[i]))#리스트추가
#             right = len(memo[i]) - 1
#             index = binary_search(i, 0, right, case)
#             memo[-1] = memo[-1][:index+1]
#             if len(memo[-1]) == 0 or memo[-1][-1] != case:
#                 memo[-1].append(case)
#
# maxLen = 1
# index = 0
# for i in range(len(memo)):
#     l = len(memo[i])
#     if  l > maxLen:
#         index = i
#         maxLen = l
# print(maxLen)
# for i in memo[index]:
#     print(i, end=" ")

# #14002
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# A = list(map(int, input().split()))
#
# dp = [1] * n
#
# for i in range(1, n):
#     for j in range(i):
#         if A[i] > A[j]:
#             dp[i] = max(dp[i],dp[j]+1)
#
# count = max(dp)
# print(count)
#
# result = []
# for i in range(n-1, -1, -1):
#     if count == 0:
#         break
#     if dp[i] == count:
#         result.append(A[i])
#         #print(A[i], end=" ")
#         count -= 1
# result.reverse()
# for r in result:
#     print(r, end=" ")

