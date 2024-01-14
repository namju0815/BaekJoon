# #1747
# import sys
# input = sys.stdin.readline
#
# def pan(n):
#     n = str(n)
#     l = len(n)//2
#     j = -1
#     for i in range(l):
#         if n[i] != n[j]:
#             return 0 #팰린드롬x
#         j -= 1
#     return 1#팰린드롬o
# def prime(n):
#     if n == 1:
#         return 0
#     elif n <= 3:
#         return 1
#     elif n % 2 == 0 or n % 3 == 0:
#         return 0
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i+2) == 0:
#             return 0
#         i += 6
#     return 1
#
# t = int(input())
# while True:
#     if pan(t) == 1 and prime(t) == 1:
#         print(t)
#         sys.exit()
#     else:
#         t += 1

# #1652
# import sys
# input = sys.stdin.readline
# n = int(input())
# room = []
# s = 0
# t = 0
# for i in range(n):
#     room.append(list(input().strip()))
#
# for i in range(n):
#     count = 0
#     check = 0
#     for j in room[i]:
#         if j == '.':
#             count += 1
#             if count >= 2 and check == 0:
#                 s += 1
#                 check = 1
#         else:
#             count = 0
#             check = 0
# print(s, end=" ")
#
# for i in range(n):
#     count = 0
#     check = 0
#     for j in room:
#         if j[i] == '.':
#             count += 1
#             if count >= 2 and check == 0:
#                 t += 1
#                 check = 1
#         else:
#             count = 0
#             check = 0
# print(t)

# #2621
# import sys
# input = sys.stdin.readline
# n = input().strip()
# count = 0
#
# if len(n) < 2:
#     n = '0' + n
#
# t = n
# while True:
#     if len(t) < 2:
#         t = '0'+t
#     a = str(int(t[0]) + int(t[1]))
#     t = t[1] + a[-1]
#     count += 1
#
#     if t == n:
#         break
#
# print(count)

# #2621
# import sys
# input = sys.stdin.readline
# colors = {}
# card = []
#
# for i in range(5):
#     c, n = input().split()
#     n = int(n)
#     card.append((c, n))
#     if c in colors:
#         colors[c] += 1
#     else:
#         colors[c] = 1
#
# card.sort()

# #18870
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# N = list(map(int, input().split()))
# A = sorted(N)
#
#
# sorted_A = sorted((set(A)))
# l = len(sorted_A)
# #print(sorted_A)
#
# result = {}
# result[A[0]] = 0
# count = 0
# i = 1
# j = 0
# while i < n and j < l:
#     a = A[i]
#     if a in result:
#         i += 1
#     elif a > sorted_A[j]:
#         count += 1
#         j += 1
#     else:
#         result[a] = count
#         i += 1
#
# for i in N:
#     print(result[i], end= " ")

# #18870
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# a = list(map(int, input().split()))
# sorted_a = sorted(set(a))
# dic_a = {}
# for i in range(len(sorted_a)):
#     dic_a[sorted_a[i]] = i
# print(*map(lambda x:dic_a[x], a))
# #x값을 dic_a에 넣고, x값은 리스트 a값을하나씩 대입(map)

# #10819
# import sys
# from itertools import permutations
# input = sys.stdin.readline
#
# t = int(input())
# A = list(map(int, input().split()))
# maxN = 0
# for i in permutations(A, t):
#     s = 0
#     for j in range(t-1):
#         a = i[j] - i[j+1]
#         if a == 0:
#             continue
#         elif a > 0:
#             s += a
#         else:
#             s -= a
#     maxN = max(maxN, s)
# print(maxN)

# #1205
# import sys
# input = sys.stdin.readline
#
# # def binary_search_tree(arr, start, end, key):
# #     if end < start:
# #         return start
# #     else:
# #         mid = (start + end) // 2
# #         if arr[mid] == key:
# #             return mid
# #         elif arr[mid] > key:
# #             return binary_search_tree(arr, mid+1, end, key)
# #         else:
# #             return binary_search_tree(arr, start, mid-1, key)
#
# n, newScore, p = map(int, input().split())
# if n == 0:
#     print(1)
#     sys.exit()
# arr = list(map(int, input().split()))
# if arr[-1] >= newScore and len(arr) == p:
#     print(-1)
#     sys.exit()
# arr.append(newScore)
# arr.sort(reverse=True)
# answer = arr.index(newScore)+1
# #answer = binary_search_tree(arr, 0, n-1, newScore)
# if answer > p:
#     print(-1)
# else:
#     print(answer)

# #8979
# import sys

# input = sys.stdin.readline
#
# t, target = map(int, input().split())
# rank = []
# a = 0; b = 0; c = 0;
# for _ in range(t):
#     country, m1, m2, m3 = map(int, input().split())
#     rank.append((m1, m2, m3))
#     if country == target:
#         a = m1; b = m2; c= m3;
# sorted_rank = sorted(rank, reverse=True)
# #print(sorted_rank)
#
# print(sorted_rank.index((a, b, c))+1)

# #11401 페르마의 소정리
# import sys
# input = sys.stdin.readline
# p = 1000000007
#
# def factorial(n):
#     a = 1
#     for i in range(2, n+1):
#         a = (a*i) % p
#     return a
# def binomial_theorem(n, k):
#     if k == 0:
#         return 0
#     elif k == 1:
#         return n
#
#     t = binomial_theorem(n, k//2)
#     if k % 2:
#         return t * t * n % p
#     else:
#         return t * t % p
#
#
# n, r = map(int, input().split())
# top = factorial(n)
# bot = factorial(n-r) * factorial(r) % p
# print(top * binomial_theorem(bot, p-2) % p)

# #1759
# import sys
# from itertools import combinations
# input = sys.stdin.readline
# L, C = map(int, input().split())
# chars = list(input().split())
# chars.sort()
#
# list_comb = list(combinations(chars, L))
# for comb in list_comb:
#     vowels = set("aeiou")
#     consonant_count = 0
#     vowel_count = 0
#     string = "".join(comb)
#     for c in string:
#         if c in vowels:
#             vowel_count += 1
#         else:
#             consonant_count += 1
#     if vowel_count > 0 and consonant_count > 1:
#         print(string)

# #2798
# import sys
# from itertools import combinations
# input = sys.stdin.readline
# N, M = map(int, input().split())
# numbers = list(input().split())
#
# answer = 0
# list_comb = combinations(numbers, 3)
# for comb in list_comb:
#     sum_number = sum(map(int, comb))
#     if M >= sum_number > answer:
#         answer = sum_number
#
# print(answer)

# #2231
# import sys
# input = sys.stdin.readline
#
# N = int(input())
#
# for i in range(1, N+1):
#     s = sum(map(int, str(i)))
#     s += i
#     if s == N:
#         print(i)
#         break
#     if i == N:
#         print(0)

#14501












