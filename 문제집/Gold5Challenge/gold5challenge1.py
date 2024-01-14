# import sys
# input = sys.stdin.readline
#
# n1 = input().strip()
# n2 = input().strip()
#
# index1 = 0
# index2 = 0
# count = 0
#
# while True:
#     if index1 == len(n1)-1 and index2 == len(n2)-1:
#         break
#     elif n1[index1] != n2[index2]:
#         if index2 == len(n2)-1:
#             index1+=1
#         else:
#             index2+=1
#     else:
#         count += 1
#         if index2 != len(n2)-1:
#             index2+=1
#         index1+=1
#
# print(count)

# #2631
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# arr = []
# dp = []
# for i in range(n):
#     arr.append(int(input()))
#     dp.append(1)
#
# for i in range(1, n):#기준
#     for j in range(i):
#         if arr[i] > arr[j] and dp[i] < dp[j]+1:
#             dp[i] = dp[j]+1
# print(n - max(dp))

# #2225
# import sys
# input = sys.stdin.readline
#
# n, k = map(int, input().split())
# result = 0
# memo = {}
# def fac(n):
#     if n in memo:
#         return memo[n]
#     elif n == 1:
#         memo[n] = 1
#     else:
#         memo[n] = fac(n-1) * n
#     return memo[n]
#
# if k == 1:
#     result = 1
# elif k == 2:
#     result = n+1
# else:
#     result = fac(n+k-1)//(fac(n)*fac(k-1))
#
# if result >= 1000000000:
#     result = result % 1000000000
# print(result)

# #2493
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n = int(input())
# num = list(map(int,input().split()))
# stack = deque()
# stack.append((num[0], 0))
# answer = [0]
#
# for idx, i in enumerate(num[1:], start = 1): #들어오는값
#     while stack:
#         number, index = stack[-1]
#         if i < number:
#             answer.append(index+1)
#             stack.append((i, idx))
#             break
#         else:
#             stack.pop()
#     if not stack:
#         answer.append(0)
#         stack.append((i, idx))
# for i in answer:
#     print(i, end=" ")

# #13325
# import sys
# input = sys.stdin.readline
# h = int(input()) #높이
# N = list(map(int, input().split()))
# A = [[0, 0], [0, 0]]
# for i in N:
#     A.append([i, i])
# #print(A)
# n = len(A)-1 #개수
# leafStart = 2**h
#
# for i in range(n, 0, -2):
#     if i == 1:
#         A[i][1] = A[i*2][1] + A[i*2+1][1]
#         break
#     if i > leafStart: #리프노드
#         if A[i][0] < A[i-1][0]:
#             A[i][0] = A[i-1][0]
#         else:
#             A[i-1][0] = A[i][0]
#         A[i][1] = A[i][0]
#         A[i-1][1] = A[i-1][0]
#     else:
#         right = A[2*i][0]+A[i][0]
#         left = A[2*(i-1)][0]+A[i-1][0]
#         a = max(left, right)
#         A[i][0] = a
#         A[i-1][0] = a
#         A[i][1] = a - A[2*i][0] + A[2*i][1] +A[2*i+1][1]
#         A[i-1][1] = a - A[2*(i-1)][0] + A[2*(i-1)][1] + A[2*(i-1)+1][1]
#
# #print(A)
# print(A[1][1])

#2749
# import sys
# input = sys.stdin.readline
# n = int(input())
# memo = {0: 0, 1: 1}
#
# def fib(n):
#     if not n in memo:
#         if n % 2 == 0:
#             a = fib(n//2)
#             result = a**2 + 2*a*fib(n//2-1)
#         else:
#             result = fib((n+1)//2)**2 + fib(((n+1)//2)-1)**2
#         # if result > 1000000:
#         #     result %= 1000000
#         memo[n] = result
#     return memo[n]
#
# print(fib(n))
# print(memo)

# #2624
# import sys
# input = sys.stdin.readline
#
# t = int(input())
# m = int(input())
# coins = []
# for _ in range(m):
#     a, b = map(int, input().split())
#     coins.append((a, b))
#
# dp = [0] * (t+1)
# dp[0] = 1
#
# for p, n in coins:
#     for i in range(t, -1, -1):
#         for j in range(1, n+1):
#             z = i-j*p
#             if z >= 0:
#                 dp[i] += dp[z]
# print(dp[t])

# #9359
# from itertools import combinations
# import sys
# input = sys.stdin.readline
# def set_prime(n): #소수집합구하기(에라토스테네스의 체)
#     prime = []
#     for i in range(2, int(n**(1/2))+1):
#         if n % i == 0:
#             prime.append(i)
#             while n % i == 0:
#                 n = n // i
#     if n > 1: #n의 제곱근보다 큰 소수인 경우
#         prime.append(n)
#     return prime
#
# n = int(input())
# for i in range(n):
#     a, b, n = map(int, input().split())
#     prime = set_prime(n) #소인수 집합
#     r_a = a-1
#     r_b = b
#     for j in range(1, len(prime)+1): #prime리스트에 있는 소수의 개수
#         for comb in combinations(prime, j):#j개의 조합
#             m = 1#comb에 속한 소수들을 곱해 나가는 변수
#             for k in comb:
#                 m *= k
#             if j % 2:
#                 r_a -= (a-1)//m
#                 r_b -= b//m
#             else:
#                 r_a += (a-1)//m
#                 r_b += b//m
#     print("Case #{0}: {1}".format(i+1, r_b-r_a))








