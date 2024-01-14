# #1920
# def binary_search_tree(A, s, e, key):#n개의 정렬 된 배열 A에서 찾으려는 수 key
#     if s <= e:
#         mid = (e+s)//2
#         if key == A[mid]:
#             return 1
#         elif key > A[mid]:
#             return binary_search_tree(A, mid+1, e, key)
#         else:
#             return binary_search_tree(A, s, mid-1, key)
#     else:
#         return 0
#
# n = int(input())
# A = list(map(int, input().split()))
# A.sort()
# #print(A)
#
# m = int(input())
# numbers = list(map(int, input().split()))
# #print(numbers)
#
# for i in numbers:
#     if binary_search_tree(A, 0, n-1, i) == 1:
#         print(1)
#     else:
#         print(0)

# #10867
# input()
# numbers = sorted(set(map(int, input().split()))) #집합은 sorted()로 정렬 가능
# for i in numbers:
#     print(i, end=" ")

# #1094 이진수로 바꾸고 1의 개수
# n = int(input())
# b = []
# while True:
#     if n == 0:
#         break
#     else:
#         b.insert(0, n%2)
#         n = n // 2
# print(b.count(1))

# #1475
# import math
# numbers = input()
# max_count = numbers.count('0')
# for i in ['1','2','3','4','5','6','7','8','9']: #0123456789
#     if i == '6' or i == '9':
#         c = math.ceil((numbers.count('6') + numbers.count('9'))/2)
#     else:
#         c = numbers.count(i)
#     if c > max_count:
#         max_count = c
# print(max_count)

# #11004
# n, k = input().split()
# k = int(k)
# numbers = list(map(int, input().split()))
# numbers.sort()
#
# print(numbers[k-1])

# #1316
# n = int(input())
# count = n
# for _ in range(n):
#     words = input()
#     l = len(words)
#     check = []
#     for i in range(l):
#         if words[i] in check:
#             count -= 1
#             break
#         elif i == l-1:
#             check.append(words[i])
#         elif words[i] != words[i+1]:
#             check.append(words[i])
# print(count)

# #2751
# import sys
# n = int(sys.stdin.readline())#.strip()로 개행문자제거
# numbers = []
#
# for _ in range(n):
#     numbers.append(int(sys.stdin.readline()))
#
# for i in sorted(numbers):
#     print(i)

# #14916
# import sys
# n = int(sys.stdin.readline())
# nn = n // 5
# for i in reversed(range(nn+1)):
#     count = 0
#     money = n - i*5
#     if money % 2 == 0:
#         count = i + money//2
#         break
#     elif i == nn:
#         count = -1
# print(count)

# #1764
# import sys
# a_list = set()
# b_list = set()
# a, b = map(int, sys.stdin.readline().split())
# for _ in range(a):
#     a_list.add(sys.stdin.readline().strip())
#
# for _ in range(b):
#     b_list.add(sys.stdin.readline().strip())
#
# result = a_list.intersection(b_list)
#
# print(len(result))
# for i in sorted(result):
#     print(i)

# #1822
# import sys
# a, b = map(int, sys.stdin.readline().split())
# numberA = set(map(int, sys.stdin.readline().split()))
# numberB = set(map(int, sys.stdin.readline().split()))
#
# result = numberA.difference(numberB)
# print(len(result))
# if result:
#     print(*sorted(result))

# #1269
# import sys
# a, b = map(int, sys.stdin.readline().split())
# numberA = set(map(int, sys.stdin.readline().split()))
# numberB = set(map(int, sys.stdin.readline().split()))
#
# count = len(numberA.difference(numberB))
# count += len(numberB.difference(numberA))
#
# print(count)

# #14425
# import sys
# a, b = map(int, sys.stdin.readline().split())
# strA = set()
# count = 0
# for _ in range(a):
#     strA.add(sys.stdin.readline())
#
# for _ in range(b):
#     if sys.stdin.readline() in strA:
#         count+=1
#
# print(count)

# #4673
# result = list(range(10001))
# for x in range(10):
#     for y in range(10):
#         for z in range(10):
#             for n in range(10):
#                 a = x*1001 + y*101 + z*11 + n*2
#                 if a > 10000:
#                     break
#                 elif a in result:
#                     result.remove(a)
#
# for i in result:
#     print(i)

# #1152
# s = list(input().split())
# print(len(s))

# #1312 n번째 소수점 자리 출력하는 함수
# A, B, n = map(int, input().split())
# for i in range(n+1):
#     if(i == n):
#         print(A//B)
#         break
#     A %= B
#     A *= 10
#     #print(A)



# #1655 최소Heap
# import sys
# import heapq
# n = int(sys.stdin.readline())
# leftHeap = []
# rightHeap = []
# answer = []
#
# for i in range(n):
#     inputNum = int(sys.stdin.readline())
#     if len(leftHeap) == len(rightHeap):
#         #leftHeap은 최대힙 모양이여야하므로, -를 붙여 부호를 반대로 하여 정렬(두번째 값에 원본 보존)
#         #길이가 같으면 left에 push
#         heapq.heappush(leftHeap, (-inputNum, inputNum))
#         #print("l",leftHeap)
#         #print("r",rightHeap)
#     else:
#         #길이가 다르면 right에 push
#         heapq.heappush(rightHeap, (inputNum, inputNum))
#         #print("l", leftHeap)
#         #print("r", rightHeap)
#
#     if rightHeap and leftHeap[0][1] > rightHeap[0][0]:
#         #만약 left의 가장 큰값(중간값위치)이 right의 최소값보다 크다면, 둘이 위치 change
#         min = heapq.heappop(rightHeap)[0]
#         max = heapq.heappop(leftHeap)[1]
#         heapq.heappush(leftHeap, (-min, min))
#         heapq.heappush(rightHeap, (max, max))
#         #print(leftHeap)
#         #print(rightHeap)
#
#     answer.append(leftHeap[0][1])
#     #print()
#
# for i in answer:
#     print(i)

# #1874 스택 수열문제(1-n)
# import sys
# n = int(sys.stdin.readline())
# numbers = []
# subList = [0]
# answer = []
#
# for _ in range(n):
#     numbers.append(int(sys.stdin.readline()))
#
# check = 0
# index = 0
# i = 1
#
# while index < n:
#     if i == n+1 and subList[-1] > numbers[index]:
#         check = 1
#         break
#     elif subList[-1] == numbers[index]:
#         #print(subList)
#         subList.pop()
#         answer.append('-')
#         index += 1
#     elif i <= n:
#         subList.append(i)
#         #print(subList)
#         answer.append('+')
#         i += 1
#
# if check == 0:
#     for i in answer:
#         print(i)
# else:
#     print("NO")

# #1065
# def sequence(n):
#     nn = n
#     if nn < 10:
#         return 1
#     else:
#         a = nn % 10
#         nn = nn//10
#         b = nn % 10
#         s = b - a
#         #print(n, ":", a, b, s)
#         while nn//10 != 0:
#             a = nn % 10
#             nn = nn // 10
#             b = nn % 10
#             #print(n, ":", a,b)
#             if s != (b-a):
#                 return 0
#             s = b-a
#         return 1
#
# count = 0
# n = int(input())
# for i in range(1, n+1):
#     count += sequence(i)
#
# print(count)

# #11866
# N, K = map(int, input().split())
# K -= 1
# numbers = list(range(1, N+1))
# answer = []
# pivot = 0
# for _ in range(N):
#     pivot = pivot + K
#     while pivot >= len(numbers):
#         pivot -= len(numbers)
#     answer.append(numbers[pivot])
#     numbers.remove(numbers[pivot])
#     #print(pivot)
#
# answer = map(str, answer)
# s = ", ".join(answer)
# print("<"+s+">")

# #1966
# import sys
# testCase = int(sys.stdin.readline())
# for _ in range(testCase):
#     N, M = map(int, sys.stdin.readline().split())
#     ipt = list(map(int, sys.stdin.readline().split()))
#     count = 0
#     index = 0
#     answer = []
#     while ipt:
#         if ipt[0] != max(ipt):
#             ipt.append(ipt[0])
#             ipt.pop(0)
#         else:
#             answer.append(ipt.pop(0))
#             count+=1
#     print(answer)
#     print(count)

# #1966
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# testCase = int(input())
# for _ in range(testCase):
#     N, M = map(int, sys.stdin.readline().split())
#     q = deque(list(map(int, input().split())))
#     count = 0
#     while q:
#         max_num = max(q)
#         front = q.popleft()
#         M -= 1
#         if max_num == front:
#             count += 1
#             if M < 0:
#                 print(count)
#                 break
#         else:
#             q.append(front)
#             if M < 0:
#                 M = len(q) - 1

# #18258
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# n = int(input())
# q = deque([])
# for _ in range(n):
#     inp = input().split()
#     if inp[0] == "push":
#         q.append(int(inp[1]))
#     elif inp[0] == "pop":
#         if len(q):
#             print(q.popleft())
#         else:
#             print(-1)
#     elif inp[0] == "size":
#         print(len(q))
#     elif inp[0] == "empty":
#         if q:
#             print(0)
#         else:
#             print(1)
#     elif inp[0] == "front":
#         if q:
#             print(q[0])
#         else:
#             print(-1)
#     elif inp[0] == "back":
#         if q:
#             print(q[-1])
#         else:
#             print(-1)

# #9657 #9658
# #0: 상근 1: 창영
# import sys
# input = sys.stdin.readline
# memo = {1: 1, 2: 0, 3: 1, 4: 0}
# def stoneGame(n):
#     if n in memo:
#         return memo[n]
#     else:
#         if stoneGame(n-1) == 1 or stoneGame(n-3) == 1 or stoneGame(n-4) == 1:
#             memo[n] = 0
#             return memo[n]
#         else:
#             memo[n] = 1
#             return memo[n]
#
# n = int(input())
# answer = stoneGame(n)
# if answer == 0:
#     print("SK")
# else:
#     print("CY")

# #2002
# import sys
# input = sys.stdin.readline
# check = {}
# d_list = []
# y_list = []
# n = int(input())
# for _ in range(n):
#     name = input()
#     d_list.append(name)
#     check[name] = 0
# for _ in range(n):
#     name = input()
#     y_list.append(name)
#
# d_index = 0
# y_index = 0
# count = 0
# while True:
#     if y_index == n:
#         break
#     elif d_list[d_index] == y_list[y_index]:
#         d_index += 1
#         check[y_list[y_index]] = 1
#         y_index += 1
#     elif check[d_list[d_index]] == 0: #d_list[d_index] != y_list[y_index]:
#         count += 1#추월 차량 한대 증가
#         check[y_list[y_index]] = 1 #y_list[i]는 이미 통화했으로 check
#         y_index += 1
#     else:
#         d_index += 1
#
# print(count)

# #2839
# import sys
# input = sys.stdin.readline
# n = int(input())
# count = 0
#
# a = n//5
# b = n%5
# if b == 0:
#     print(a)
# elif b == 3:
#     print(a + 1)
# else:
#     while a >= 0:
#         a -= 1
#         b += 5
#         if a < 0:
#             print(-1)
#             break
#         elif b % 3 == 0:
#             print(a + (b // 3))
#             break

# #1358
# def inspect_location(w, h, x, y, xx, yy):
#     if x-h <= xx <= x+w+h and y <= yy <= y+2*h:
#         if x <= xx <= x+w:
#             return 1
#         elif x-h <= xx < x:
#             if(xx-x)**2 + (yy-y-h)**2 <= h**2:
#                 return 1
#             else:
#                 return 0
#         elif x+w < xx <= x+w+h:
#             if(x+w-xx)**2 + (y+h-yy)**2 <= h**2:
#                 return 1
#             else:
#                 return 0
#     else:
#         return 0
#
# w, h, x, y, p = map(int, input().split())
# count = 0
# for i in range(p):
#     xx, yy = map(int, input().split())
#     count += inspect_location(w, h//2, x, y, xx, yy) #여기서 h는 반지름으로 보냄
#
# print(count)

# #1002
# def inspectDistance(x1, y1, r1, x2, y2, r2):
#     d = (x2-x1)**2 + (y2-y1)**2
#     diff_r = (r1-r2)**2
#     sum_r = (r1+r2)**2
#
#     if x1 == x2 and y1 == y2:
#         if r1 == r2:
#             return -1
#         else:
#             return 0
#     elif diff_r < d < sum_r:
#         return 2
#     elif diff_r == d or sum_r == d:
#         return 1
#     else:
#         return 0
#
# n = int(input())
# for _ in range(n):
#     x1, y1, r1, x2, y2, r2 = map(int, input().split())
#     print(inspectDistance(x1, y1, r1, x2, y2, r2))

# #2941
# import re
# n = input()
# count = 0
# while True:
#     if len(n) == 0:
#         break
#     elif 'c=' in n:
#         c = n.count('c=')
#         count += c
#         n = re.sub('c=', ' ', n)
#     elif 'c-' in n:
#         c = n.count('c-')
#         count += c
#         n = re.sub('c-', ' ', n)
#     elif 'dz=' in n:
#         c = n.count('dz=')
#         count += c
#         n = re.sub('dz=', ' ', n)
#     elif 'd-' in n:
#         c = n.count('d-')
#         count += c
#         n = re.sub('d-', ' ', n)
#     elif 'lj' in n:
#         c = n.count('lj')
#         count += c
#         n = re.sub('lj', ' ', n)
#     elif 'nj' in n:
#         c = n.count('nj')
#         count += c
#         n = re.sub('nj', ' ', n)
#     elif 's=' in n:
#         c = n.count('s=')
#         count += c
#         n = re.sub('s=', ' ', n)
#     elif 'z=' in n:
#         c = n.count('z=')
#         count += c
#         n = re.sub('z=', ' ', n)
#     elif '=' in n:
#         n = re.sub('=', ' ', n)
#     elif '-' in n:
#         n = re.sub('-', ' ', n)
#     else:
#         c = n.count(' ')
#         count += len(n)
#         count -= c
#         break
#
# print(count)

# #2941
# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# n = input()
# for i in croatia:
#     n = n.replace(i, '*')
# print(len(n))

# #9012
# import sys
# input = sys.stdin.readline
# n = int(input())
# ss = []
# answer = [1]*n
#
# for j in range(n):
#     s = input().strip()
#     for i in s:
#         if i == '(':
#             ss.append(i)
#         elif i == ')':
#             if len(ss) == 0:
#                 answer[j] = 0
#                 break
#             else:
#                 ss.pop()
#                 continue
#     if len(ss) != 0:
#         answer[j] = 0
#     ss.clear()
#
# for i in answer:
#     if i == 0:
#         print("NO")
#     else:
#         print("YES")

# #4949
# import sys
# input = sys.stdin.readline
# lines = []
# while True:
#     line = input()
#     if line == '.\n':
#         break
#     else:
#         lines.append(line)
#
# n = len(lines)
# ss = []
#
# for j in range(n):
#     s = lines[j]
#     for i in s:
#         if i == '(' or i == '[':
#             ss.append(i)
#         elif i == ')':
#             if len(ss) != 0 and ss[-1] == '(':
#                 ss.pop()
#                 continue
#             else:
#                 ss.append(i)
#                 break
#         elif i == ']':
#             if len(ss) != 0 and ss[-1] == '[':
#                 ss.pop()
#                 continue
#             else:
#                 ss.append(i)
#                 break
#         else:
#             continue
#     if not ss:
#         print("yes")
#     else:
#         print("no")
#     ss.clear()

# #9020
# def prime(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#     else:
#         a = int(n**(1/2))
#         for i in range(2, a+1):
#             if n % i == 0:
#                 return False
#         return True
#
# def findNumber(n):
#     if n == 4:
#         return 2
#     else:
#         mid = n//2
#         aa = mid
#         if mid % 2 == 0:
#             aa = mid - 1
#
#         while aa > 0:
#             if prime(aa) and prime(n-aa):
#                 return aa
#             else:
#                 aa -= 2
# import sys
# input = sys.stdin.readline
# testCase = int(input())
# for _ in range(testCase):
#     n = int(input())
#     a = findNumber(n)
#     print(a, n-a)

#4948
# def prime(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#     else:
#         a = int(n**(1/2))
#         for i in range(2, a+1):
#             if n % i == 0:
#                 return False
#         return True
#
# memo = []
# for i in range(2, 246912):
#     if prime(i):
#         memo.append(i)
#
# while True:
#     n = int(input())
#     count = 0
#     if n == 0:
#         break
#     for i in memo:
#         if n < i <= 2*n:
#             count+=1
#     print(count)

# import math
# import sys
# arr=[True for i in range(246913)]
# for i in range(2,int(math.sqrt(246912))+1):
#   if arr[i]==True:
#     j=2
#     while i*j<=246913:
#       arr[i*j]=False
#       j+=1
# a=int(sys.stdin.readline())
# while a!=0:
#   print(arr[a+1:a*2+1].count(True))
#   a=int(sys.stdin.readline())

# #2164
# import sys
# from collections import deque
# input = sys.stdin.readline
# n = int(input())
# q = deque([j for j in range(1,n+1)])
# while True:
#     if len(q) == 1:
#         print(q.popleft())
#         break
#     else:
#         q.popleft()
#         if len(q) == 1:
#             print(q.popleft())
#             break
#         else:
#             data = q.popleft()
#             q.append(data)

# #10866
# import sys
# from collections import deque
# input = sys.stdin.readline
# n = int(input())
# q = deque()
#
# for _ in range(n):
#     ipt = input().rstrip().split()
#     if ipt[0] == "push_back":
#         data = int(ipt[1])
#         q.append(data)
#     elif ipt[0] == "push_front":
#         data = int(ipt[1])
#         q.insert(0, data)
#     elif ipt[0] == "pop_front":
#         if len(q) == 0:
#             print(-1)
#         else:
#             print(q.popleft())
#     elif ipt[0] == "pop_back":
#         if len(q) == 0:
#             print(-1)
#         else:
#             print(q.pop())
#     elif ipt[0] == "size":
#         print(len(q))
#     elif ipt[0] =="empty":
#         if len(q) == 0:
#             print(1)
#         else:
#             print(0)
#     elif ipt[0] == "front":
#         if len(q) == 0:
#             print(-1)
#         else:
#             print(q[0])
#     elif ipt[0] == "back":
#         if len(q) == 0:
#             print(-1)
#         else:
#             print(q[-1])

# #2608
# def changeR(n):
    # number = 0
    # index = 0
    # l = len(n)
    # while True:
    #     if index == l:
    #         break
    #     elif n[index] == 'M':
    #         number += 1000
    #         index += 1
    #     elif n[index] == 'D':
    #         number += 500
    #         index += 1
    #     elif n[index] == 'C':
    #         index += 1
    #         if index != l:
    #             if n[index] == 'M':
    #                 number += 900
    #                 index += 1
    #                 continue
    #             elif n[index] == 'D':
    #                 number += 400
    #                 index += 1
    #                 continue
    #         number += 100
    #     elif n[index] == 'L':
    #         number += 50
    #         index += 1
    #     elif n[index] == 'X':
    #         index += 1
    #         if index != l:
    #             if n[index] == 'L':
    #                 number += 40
    #                 index += 1
    #                 continue
    #             elif n[index] == 'C':
    #                 number += 90
    #                 index += 1
    #                 continue
    #         number += 10
    #     elif n[index] == 'V':
    #         number += 5
    #         index += 1
    #     elif n[index] == 'I':
    #         index += 1
    #         if index != l:
    #             if n[index] == 'X':
    #                 number += 9
    #                 index += 1
    #                 continue
    #             elif n[index] == 'V':
    #                 number += 4
    #                 index += 1
    #                 continue
    #         number += 1
    # return number
# def changeR(n):
#     nn = 0;
#     pre = ""
#     number = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
#     for i in n:
#         nn += number[i]
#         if pre != "" and number[i] > number[pre]:
#             nn -= 2 * number[pre]
#         pre = i
#     return nn
#
# def changeN(n):
#     check = [0, 0, 0, 0, 0, 0, 0] #V L D I X C M
#     a = []
#     while True:
#         if n == 0:
#             break
#         elif n >= 1000 and check[6] != 3:
#             n-=1000
#             a.append('M')
#             check[6] += 1
#         elif n >= 900:
#             n-=900
#             a.append('CM')
#         elif n >= 500 and check[2] == 0:
#             n-=500
#             a.append('D')
#             check[2] = 1
#         elif n >= 400 and 'CM' not in a:
#             n-=400
#             a.append('CD')
#         elif n >= 100 and check[5] != 3:
#             n-=100
#             a.append('C')
#             check[5] += 1
#         elif n >= 90:
#             n-=90
#             a.append('XC')
#         elif n >= 50 and check[1] == 0:
#             n-=50
#             a.append('L')
#             check[1] = 1
#         elif n >= 40 and 'XC' not in a and 'XL' not in a:
#             n-=40
#             a.append('XL')
#         elif n >= 10 and check[4] != 3:
#             n-=10
#             a.append('X')
#             check[4] += 1
#         elif n>=9:
#             n-=9
#             a.append('IX')
#         elif n>=5 and check[0] == 0:
#             n-=5
#             a.append('V')
#             check[0] = 1
#         elif n>=4 and 'IX' not in a and 'IV' not in a:
#             n-=4
#             a.append('IV')
#         elif n>=1 and check[3] != 3:
#             n-=1
#             a.append('I')
#             check[3] += 1
#     return a
#
# n1 = input()
# n2 = input()
#
# sumNumber = changeR(n1)
# sumNumber += changeR(n2)
# print(sumNumber)
# print(''.join(map(str, changeN(sumNumber))))

# #근규코드
# def rometoarabia(n):
#     nn = 0; pre = ""
#     number = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
#     for i in n:
#         nn += number[i]
#         if pre != "" and number[i] > number[pre]:
#             nn -= 2 * number[pre]
#         pre = i
#     return nn
#
# def arabiatorome(n):
#     n = str(n); nn = ""; multiple = 1
#     number2 = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
#     for i in n[::-1]:
#         i = int(i)
#         if 1 <= i <= 3:
#             nn = nn + number2[multiple] * i
#         elif i == 4:
#             nn = nn + number2[multiple*5] + number2[multiple]
#         elif i == 5:
#             nn = nn + number2[multiple*5]
#         elif 6 <= i <= 8:
#             nn = nn + number2[multiple] * (i-5) + number2[multiple*5]
#         elif i == 9:
#             nn = nn + number2[multiple*10] + number2[multiple]
#         multiple *= 10
#     return nn[::-1]
#
# a = input(); b = input()
#
# sum = rometoarabia(a) + rometoarabia(b)
# print(sum)
# print(arabiatorome(sum))

# #1052
# n, k = map(int, input().split())
# bin_str = bin(n)
# index = 0
# index_list = []
# for i in bin_str[::-1]:
#     if i == '1':
#         index_list.append(index)
#     index+=1
# #print(index_list)
# l = len(index_list) - k #7
# sum = 0
# for i in range(l): #2(0,1)
#     a = int(index_list[i])
#     sum += 2**a
#     #print(sum)
#     if i == l-1:
#         sum = 2**(int(index_list[i+1])) - sum
# print(sum)

# #15828
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# n = int(input())
# q = deque()
# while True:
#     inp = int(input())
#     if inp == -1:
#         break
#     elif inp > 0:
#         if len(q) == n:
#             continue
#         else:
#             q.append(inp)
#     else: #inp == 0
#         if len(q) == 0:
#             continue
#         else:
#             q.popleft()
# if q:
#     for i in q:
#         print(i, end=" ")
# else:
#     print("empty")

# #2407
# def conbination(n, r, memo):
#     if memo[n][r] != 0:
#         return memo[n][r]
#     elif r == 0 or n == r:
#         memo[n][r] = 1
#     elif r == 1:
#         memo[n][r] = n
#     elif n//2 < r:
#         memo[n][r] = conbination(n, n-r, memo)
#     else:
#         memo[n][r] = conbination(n-1, r, memo) + conbination(n-1, r-1, memo)
#     return memo[n][r]
#
# import sys
# input = sys.stdin.readline
# n, r = map(int, input().split())
# memo = [[0]*(r+1) for _ in range(n+1)]
# print(conbination(n, r, memo))

# #2477
# import sys
# input = sys.stdin.readline
# k = int(input())
# w_max = 0
# w_maxIndex = -1
# h_max = 0
# h_maxIndex = -1
# i = [] #index
# l = [] #길이
# for s in range(6):
#     j, ll = map(int, input().split())
#     i.append(j); l.append(ll);
#     if j == 1 or j == 2:
#         if ll > w_max:
#             w_max = ll
#             w_maxIndex = s
#     else:
#         if ll > h_max:
#             h_max = ll
#             h_maxIndex = s
#
# i[w_maxIndex] = 0
# i[h_maxIndex] = 0
#
# a = 1
# check = 0
# for index in range(6):
#     if check == 2:
#         break
#     elif i[index] == 0:
#         check+= 1
#         a *= l[(index+3)%6]
# # print(h_max, w_max)
# # print(a)
# # print(h_max*w_max-a)
# print((h_max*w_max-a)*k)

# #2491
# import sys
# input = sys.stdin.readline
# n = int(input())
# num_list = list(map(int, input().split()))
#
# def get_subsequence(nums):
#     if len(nums) == 1:
#         return 1
#     max_length = 1
#     current_length = 1
#     sign = 0
#     same = 1
#
#     for i in range(1, n):
#         if nums[i-1] < nums[i]:#증가할때
#             if sign == -1:
#                 current_length = 1 + same
#             else:
#                 current_length += 1
#                 max_length = max(max_length, current_length)
#             sign = 1
#             same = 1
#         elif nums[i-1] > nums[i]:#감소할때
#             if sign == 1:
#                 current_length = 1 + same
#             else:
#                 current_length += 1
#                 max_length = max(max_length, current_length)
#             sign = -1
#             same = 1
#         else: #같을떄
#             same += 1
#             current_length += 1
#             max_length = max(max_length, current_length)
#     return max_length
#
# print(get_subsequence(num_list))

# #1436
# import sys
# input = sys.stdin.readline
# n = int(input())
#
# def count_six(index):
#     index = list(str(index))
#     count = 0
#     for i in index[::-1]:
#         if i != '6':
#             break
#         count+=1
#     if count > 3:
#         count = 3
#     return count
#
# def tripleSix(n):
#     index1 = 0
#     index2 = 0
#     for i in range(n):
#         a = index1%10
#         if a != 6: #index1의 마지막 자리가 6이 아닐 경우
#             if index1 == 0:
#                 answer = "666"
#             else:
#                 answer = str(index1) + "666"
#             index1 += 1
#         else: #index1의 마지막 자리가 6인경우
#             c = count_six(index1)
#             c = 3 - c
#             l = 3-c
#             answer = str(index1) + "6"*c + str(index2).zfill(l)
#             if index2 == (10**l)-1:
#                 index1 += 1
#                 index2 = -1
#             index2 += 1
#         #print(i, answer)
#     return answer
#
# print(tripleSix(n))

# #9461
# import sys
# input = sys.stdin.readline
# memo = {1:1, 2:1, 3:1, 4:2, 5:2}
# t = int(input())
#
# def p(n):
#     if n in memo:
#         return memo[n]
#     else:
#         memo[n] = p(n-5) + p(n-1)
#         return memo[n]
#
# for _ in range(t):
#     n = int(input())
#     print(p(n))

# #근규코드
# t = int(input())
# k = [1, 1, 1, 2, 2]
#
# def p(n):
#     if len(k) >= n:
#         return k[n - 1]
#     else:
#         k.append(p(n-5) + p(n-1))
#         return k[n-1]
#
# for _ in range(t):
#     n = int(input())
#     print(p(n))

# #1018
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# data = []
# answer = 33
#
# for _ in range(n):
#     inp = list(input().strip())
#     data.append(inp)
# #print(data)
# def check(i, j):
#     count = 0
#     for a in range(i, i+8):
#         for b in range(j, j+8):
#             if a == i and b == j:
#                 pivot = data[a][b]
#             elif data[a][b] == "W":
#                 if pivot == "W":
#                     count += 1
#                     pivot = "B"
#                 else:
#                     pivot = "W"
#             elif data[a][b] == "B":
#                 if pivot == "B":
#                     count += 1
#                     pivot = "W"
#                 else:
#                     pivot = "B"
#
#             if b == j+7:
#                 if pivot == "B":
#                     pivot = "W"
#                 else:
#                     pivot = "B"
#     #print(count)
#     if count > 32:
#         count = 64 - count
#     return count
#
# mm = m - 8#0부터 mm까지 가로까지 for문
# nn = n - 8
#
# for j in range(mm+1):
#     for i in range(nn+1):
#         answer = min(answer, check(i, j))
# print(answer)

# #1004
# import sys
# input = sys.stdin.readline
# t = int(input())
# result = []
# for _ in range(t):
#     x1, y1, x2, y2 = map(int, input().split())
#     n = int(input())
#     count = 0
#     for _ in range(n):
#         xc, yc, r = map(int, input().split())
#         r1 = (x1-xc)**2+(y1-yc)**2
#         r2 = (x2-xc)**2+(y2-yc)**2
#         powR = r**2
#         if r1 < powR and r2 < powR:
#             continue
#         if r1 < powR or r2 < powR:
#             count += 1
#     result.append(count)
# for i in result:
#     print(i)

# #2631
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# pokemon = {}
#
# for i in range(n):
#     name = input().strip()
#     a = str(i + 1)
#     pokemon[a] = name
#     pokemon[name] = a
#
# for _ in range(m):
#     inp = input().strip()
#     print(pokemon[inp])

# #12865
# n, k = map(int, input().split())
#
# bag = []
#
# for _ in range(n):
#     a, b = map(int, input().split())
#     bag.append((a,b))
#
# #여기서부터 수정
# dp = [0] * (k+1)
#
# for j in range(n):
#     for i in range(k, 0, -1):
#         if i >= bag[j][0]:
#             dp[i] = max(dp[i], dp[i-bag[j][0]] + bag[j][1])
#
# print(dp[k])

# bag_sort = sorted(bag)
#
# for i in range(1, n+1):
#     comb = list(combinations(bag_sort, i))
#     for j in comb:
#         if sum(j) <= k:#무게합이 7미만인 튜플출력
#             s = 0
#             for l in j:
#                 s = s+bag[l]
#             max_v = max(max_v, s)
# print(max_v)

# #2002
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# t = int(input())
# out_list = []
# in_list = deque()
# dic = {}
# count = 0
#
# for i in range(t):
#     car = input()
#     in_list.appendleft(car)
#     dic[car] = 0
# for j in range(t):
#     car = input()
#     out_list.append(car)
#
# index = 0
# while True:
#     if len(in_list) == 0 or index == t-1:
#         break
#     target = in_list[-1]
#     if dic[target] == 1:
#         in_list.pop()
#         continue
#     if target == out_list[index]:
#         in_list.pop()
#         dic[target] = 1
#     else:
#         dic[out_list[index]] = 1
#         count += 1
#     index += 1
#
# print(count)

# #7795
# import sys
# input = sys.stdin.readline
# t = int(input())
#
# def solve(a,b):
#     a.sort()
#     b.sort()
#
#     answer = 0
#     j = 0
#
#     for i in range(len(a)):
#         while j < len(b) and b[j] < a[i]:
#             j += 1
#         answer += j
#     return answer
#
# for i in range(t):
#     aSize, bSize = map(int, input().split())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#     result = solve(a,b)
#     print(result)

# #4892
# import sys
# input = sys.stdin.readline
# answer = []
# while True:
#     n0 = int(input())
#     result = 'null'
#     if n0 == 0:
#         break
#     n1 = 3 * n0
#     if n1%2 == 0:
#         n2 = n1//2
#         result = 'even'
#     else:
#         n2 = (n1+1)//2
#         result = 'odd'
#     n3 = 3 * n2
#     n4 = n3//9
#     answer.append((result, n4))
# index = 1
# for i in answer:
#     print(str(index)+".", i[0], i[1])
#     index += 1

#24052


