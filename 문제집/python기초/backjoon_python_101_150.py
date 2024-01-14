# #2908
# a,b = input().split()
#
# a = a[::-1]
# b = b[::-1]
# a = int(a); b = int(b)
# print(max(a, b))

# #2460
# present_people = 0
# max_people = 0
# for _ in range(10):
#     a, b = map(int, input().split())
#     present_people -= a
#     max_people = max(max_people, present_people)
#     present_people += b
#     max_people = max(max_people, present_people)
#
# print(max_people)

# #2592
# count = {}
# sum = 0
# for i in range(10):
#     a = int(input())
#     sum += a
#     if a in count:
#         count[a] += 1 #count값 증가
#     else:
#         count[a] = 1
#
# #max_value = max(count.values()) #사전의 values 값들중에서 최대값 뽑음
# print(sum//10)
# print(max(count, key=count.get)) #values 값드중에서 최대값의 '키'값을 뽑음

# #2577
# a = int(input())
# b = int(input())
# c = int(input())
# result = a*b*c
# count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# while result > 0:
#     rest = result % 10
#     count[rest] += 1
#     result = result // 10
#
# for i in count:
#     print(i)

# #2711
# n = int(input())
#
# for _ in range(n):
#     miss_num, miss_str = map(str, input().split())
#     miss_num = int(miss_num)
#     print(miss_str[:miss_num-1] + miss_str[miss_num:])

# #2953
# winner_index = -1
# max_score = 0
# for i in range(1,6):
#     a, b, c, d = map(int, input().split())
#     score = a+b+c+d
#     if score > max_score:
#         max_score = score
#         winner_index = i
#
#
# print(winner_index, max_score)

# #3052-1
# result = []
# for _ in range(42):#result를 0으로 세팅
#     result.append(0)
#
# for _ in range(10):
#     num = int(input())
#     num = num % 42
#     result[num] += 1
#
# print(42 - result.count(0))

# #3052-2
# result = set() #집합생성(set()), 사전생성({})
# for _ in range(10):
#     num = int(input())%42
#     result.add(num)
#
# print(len(result))

# #1292
# #1 - 0
# #2 - 1~1+1
# #3 - 3~5
# #4 - 6~6+3
# def print_num(n):
#     index = 1 #가장끝 인덱스
#     i = 1 #인덱스증가크기
#
#     while n >= index:
#         index += i
#         i += 1
#         if n < index:
#             i -= 1
#
#     return i
#
# a, b = map(int, input().split())
# sum = 0
# for i in range(a, b+1):
#     sum += print_num(i)
#     #print(print_num(i))
# print(sum)

# #3460
# n = int(input())
# result = []
# for _ in range(n):
#     values = []
#     number = int(input())
#     while number != 0:
#         values.append(number%2)
#         number = number//2
#     result.append(values)
#
# for i in result:
#     for index, value in enumerate(i):
#         if value == 1:
#             print(index, end=" ")
#     print()

# #10807
# n = int(input())
# numbers = list(map(int, input().split()))
# target = int(input())
# count = 0
#
# for i in range(n):
#     if target == numbers[i]:
#         count+= 1
#
# print(count)

# #10818
# n = int(input())
# numbers = list(map(int, input().split()))
#
# print(min(numbers), max(numbers))

# #5054
# n = int(input())
# dis = []
# for _ in range(n):
#     s = int(input())
#     result = list(map(int, input().split()))
#     dis.append((max(result)-min(result))*2)
#
# for i in dis:
#     print(i)

# #2822
# result = []
# result_sort = []
# for _ in range(8):
#     score = int(input())
#     result.append(score)
#     result_sort.append(score)
#
# result_sort.sort()
# result_sort = result_sort[3:]
#
# print(sum(result_sort))
#
# list = []
# for i in range(5):
#     list.append(result.index(result_sort[i]) + 1)
# list.sort()
#
# for i in list:
#     print(i, end=" ")

# #2750
# a = []
# n = int(input())
# for _ in range(n):
#     number = int(input())
#     if number in a:
#         continue
#     else:
#         a.append(number)
#
# a.sort()
# for i in a:
#     print(i)

# #2752
# a = list(map(int, input().split()))
# a.sort()
#
# for i in a:
#     print(i, end=" ")

# #1037
# input()
# numbers = list(map(int, input().split()))
#
# numbers.sort()
# print(numbers[0]*numbers[-1])

# #5543
# h = []
# b = []
# for i in range(5):
#     a = int(input())
#     if i < 3:
#         h.append(a)
#     else:
#         b.append(a)
#
# h.sort()
# b.sort()
# print(h[0]+b[0]-50)

# #2587
# list = []
# for _ in range(5):
#     a = int(input())
#     list.append(a)
#
# list.sort()
# print(sum(list)//5)
# print(list[2])

# #1427
# number = input()
# list = []
# for i in number:
#     list.append(int(i))
#
# list.sort(reverse=True)
#
# for i in list:
#     print(i, end="")

# #2309
# numbers = []
#
# for _ in range(9):
#     a = int(input())
#     numbers.append(a)
#
# sum = sum(numbers)
#
# check = 0
# for i in range(9):
#     for j in range(i):
#         if check != 1:
#             if sum - (numbers[i] + numbers[j]) == 100 :
#                 numbers.remove(numbers[i])
#                 numbers.remove(numbers[j])
#                 check = 1
#                 numbers.sort()
#                 for i in numbers:
#                     print(i)

# #9076
# n = int(input())
# answer = []
# for _ in range(n):
#     scores = list(map(int, input().split()))
#     scores.sort()
#     if scores[3]-scores[1] < 4:
#         scores.remove(scores[0])
#         scores.remove(scores[3])
#         answer.append(sum(scores))
#     else:
#         answer.append("KIN")
#
# for i in answer:
#     print(i)

# #2693
# import sys
#
# n = int(input())
# answer = []
# for i in range(n):
#     numbers = list(map(int, sys.stdin.readline().split()))
#     numbers.sort()
#     print(numbers[-3])

# #5176
# import sys
# n = int(input())
#
# for _ in range(n):
#     p, m = map(int, input().split())
#     count = 0
#     numbers = []
#     for i in range(p):
#         number_sit = int(input())
#         if number_sit in numbers:
#             count += 1
#         else:
#             numbers.append(number_sit)
#     print(count)

# #10809
# word = list(input())
# alphabet = list("abcdefghijklmnopqrstuvwxyz")
# for i in alphabet:
#     if i in word:
#         print(word.index(i), end=" ")
#     else:
#         print(-1, end=" ")

# #3058
# n = int(input())
# sum_num = []
# min_num = []
# for _ in range(n):
#     number = list(map(int, input().split()))
#     result = []
#     for i in range(7):
#         if number[i] % 2 == 0:
#             result.append(number[i])
#     #print(result)
#     sum_num.append(sum(result))
#     min_num.append(min(result))
#
# for i in range(n):
#     print(sum_num[i], min_num[i])

# #5800
# def find_gap(lst, len_lst):
#     max_num = 0
#     for i in range(len_lst): #01234
#         if i == len_lst-1:
#             continue
#         n = lst[i] - lst[i+1]
#         max_num = max(max_num, n)
#     return max_num
#
# k = int(input())
# max_num = []
# min_num = []
# gap = []
# for _ in range(k):
#     math_score = list(map(int, input().split()))
#     n = math_score[0]
#     math_score.remove(n)
#     math_score.sort(reverse=True)
#     max_num.append(math_score[0])
#     min_num.append(math_score[n-1])
#     #print(math_score)
#     gap.append(find_gap(math_score, n))
#
# for i in range(1, k+1):
#     print("Class", i)
#     print(f"Max {max_num[i-1]}, Min {min_num[i-1]}, Largest gap {gap[i-1]}")

# #10870
# memo = {0: 0, 1: 1, 2: 1}
# def fib(n):
#     if n in memo:
#         return memo[n]
#     else:
#         memo[n] = fib(n-1) + fib(n-2)
#         return memo[n]
#
# n = int(input())
# print(fib(n))

# #5576
# list1 = []
# for _ in range(10):
#     score = int(input())
#     list1.append(score)
# list1.sort()
#
# list2 = []
# for _ in range(10):
#     score = int(input())
#     list2.append(score)
# list2.sort()
#
#
# print(sum(list1[7:]), sum(list2[7:]))

# #11047
# n, k = map(int, input().split())
# money_list = []
# for _ in range(n):
#     money = int(input())
#     money_list.append(money)
#
# money_list.sort(reverse=True)
#
# #print(money_list)
# count = 0
# for i in money_list:
#     if i <= k:
#         count += (k//i)
#         k = k % i
#
# print(count)

# #2744
# ###ASCII chr(아스키코드값) = 문자, ord(문자) = 아스키코드값
# ### 65-90:대문자, 97-122:소문자 차이 - 32
# word = list(input())
# l = len(word)
# for i in range(l):
#     n = ord(word[i])
#     if 64 < n < 91:
#         word[i] = chr(n+32)
#     else:
#         word[i] = chr(n-32)
#
# for i in word:
#     print(i, end="")
#
# ###print(input().swapcase())

# #10953
# n = int(input())
# for _ in range(n):
#     a, b = map(int, input().split(','))
#     print(a+b)

# #2902
# names = input().split('-')
# for i in names:
#     print(i[0], end="")

# #1357
# a, b = input().split()
# a = int(a[::-1])
# b = int(b[::-1])
# number = int(str(a+b)[::-1])
# print(number)

# #10987 모음(a, e, i, o, u)
# word = input()
# count = 0
# for i in word:
#     if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#         count += 1
# print(count)

# #4458
# n = int(input())
# name_list = []
# for _ in range(n):
#     name = list(input())
#     name[0] = name[0].upper()
#     for i in name:
#         print(i, end="")
#     print()

# #11654
# n = input()
# print(ord(n))

# #11720
# input()
# number = input()
# sum = 0
# for i in number:
#     sum += int(i)
# print(sum)

# #11721
# word = input()
# l = len(word)
# while len(word) != 0:
#     if len(word) > 10:
#         print(word[:10])
#         word = word[10:]
#     else:
#         print(word)
#         word = ""

# #10821
# a = list(map(int, input().split(',')))
# print(len(a))

# #10808
# word = list(input())
# alphabet = list("abcdefghijklmnopqrstuvwxyz")
# for i in alphabet:
#     print(word.count(i), end=" ")

# #1157
# word = input().upper()
# word_count = {}
# for i in word:
#     if i in word_count:
#         word_count[i] += 1
#     else:
#         word_count[i] = 0
#
# #print(word_count)
# max_count = -1
# max_alphabet = "0"
# check = 0
# for a, b in word_count.items():
#     if max_count == b:
#         check = 1
#     elif max_count < b:
#         max_alphabet = a
#         max_count = b
#         check = 0
#     else:
#         continue
#
# if check == 1:
#     print("?")
# else:
#     print(max_alphabet)

# #9086
# n = int(input())
# for _ in range(n):
#     word = input()
#     l = len(word)
#     print(word[0]+word[l-1])

# #5218
# n = int(input())
# for _ in range(n):
#     word1, word2 = input().split()
#     l = len(word1)
#     print("Distances: ", end="")
#     for i in range(l):
#         w1 = ord(word1[i])
#         w2 = ord(word2[i])
#         if w1 <= w2:
#             print(w2-w1, end=" ")
#         else:
#             print(w2+26-w1, end=" ")
#     print()

# #11365
# list = []
# sentence = ""
# while True:
#     sentence = input()
#     if sentence != "END":
#         break
#     list.append(sentence)
#
# for i in list:
#     print(i[::-1])

# #11170
# n = int(input())
# for _ in range(n):
#     count = 0
#     a, b = map(int,input().split())
#     for i in range(a, b+1):
#         number = str(i)
#         count += number.count("0")
#     print(count)

# #11655
# sentence = input()
# password = []
# index = 0
# for i in sentence:
#     w = ord(i)
#     if 65 <= w <= 77:
#         password.append(chr(w+13))
#     elif 78 <= w <= 90:
#         password.append(chr(w-13))
#     elif 97 <= w <= 109:
#         password.append(chr(w+13))
#     elif 110 <= w <= 222:
#         password.append(chr(w-13))
#     else:
#         password.append(i)
# for i in password:
#     print(i, end="")

# #1676
# memo = {0: 1, 1: 1, 2: 2}
# def factorial(n):
#     if n in memo:
#         return memo[n]
#     else:
#         memo[n] = n * factorial(n-1)
#         return memo[n]
# n = int(input())
# numbers = str(factorial(n))
# count = 0
# i = -1
# while numbers[i] == '0':
#     count += 1
#     i-=1
# print(count)

#2559
#ver1
# import sys
# input = sys.stdin.readline
#
# n, k = map(int, input().split())
# arr = list(map(int, input().split()))
#
# result = sum(arr[:k])
# memo = result
# for i in range(k, n):
#     memo = memo + arr[i] - arr[i-k]
#     result = max(result, memo)
#
# print(result)

#ver2
# import sys
# input = sys.stdin.readline
#
# n, k = map(int, input().split())
# def get_segment_tree_size(n):
#     i = 1
#     while i < n:
#         i *= 2
#     return i
# def build_segment_tree(arr, tree, node, start, end):
#     if start == end:
#         tree[node] = arr[start]
#         return
#     mid = (end+start)//2
#     build_segment_tree(arr, tree, node*2, start, mid)
#     build_segment_tree(arr, tree, node*2+1, mid+1, end)
#     tree[node] = tree[node*2] + tree[node*2+1]
#
# def sum_segment_tree(tree, node, start, end, left, right):
#     if start > right or left > end:
#         return 0
#     elif left <= start and end <= right:
#         return tree[node]
#     else:
#         mid = (end + start) // 2
#         l_sum = sum_segment_tree(tree, node * 2, start, mid, left, right)
#         r_sum = sum_segment_tree(tree, node * 2 + 1, mid + 1, end, left, right)
#         return l_sum + r_sum
#
# N = get_segment_tree_size(n)
# #print(N)
# arr = list(map(int, input().split()))
# N = get_segment_tree_size(n)
# arr += [0] * (N - n)  # 배열을 2^n 크기로 확장하고 나머지 부분을 0으로 초기화
#
# #print(arr)
#
# segment_tree = [0] * N * 2
# build_segment_tree(arr, segment_tree, 1, 0, N-1)
# #print(segment_tree)
#
# m = -100000000
# for i in range(n-k+1):
#     a = sum_segment_tree(segment_tree, 1, 0, N-1, i, i+k-1)
#     m = max(m, a)
# print(m)

#11003
import sys
from collections import deque

input = sys.stdin.readline

n, l = map(int, input().split())
arr = list(map(int, input().split()))

q = deque([])
for i in range(n):
    if q and q[0][0] <= i-l:#인덱스값이 슬라이싱 범위초과시
        q.popleft()
    while len(q) >= 1 and arr[i] < q[-1][1]:#새로들어오는 값이 작으면
        q.pop()
    q.append((i, arr[i]))
    print(q[0][1], end = " ")



