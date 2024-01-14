# #2525, 2530
# def calculation_time(h, m, s, time):
#     s += time
#     while s >= 60:
#         m += 1
#         s -= 60
#     while m >= 60:
#         h += 1
#         m -= 60
#     while h >= 24:
#         h -= 24
#     return h, m, s
#
# h, m, s = map(int, input().split())
# time = int(input())
# h, m, s = calculation_time(h, m, s, time)
# print(h,m,s)

# #2914
# a, b = map(int, input().split())
# b -= 1
# print(a*b+1)

# #5355
# def calculation(num, list):
#     for x in list[1:]:
#         if(x == "@"):
#             num *= 3
#         elif(x == "%"):
#             num += 5
#         elif(x == "#"):
#             num -= 7
#     return num
#
# index = int(input())
# list = [] #입력문자열 쪼개서 담을 리스트
# for i in range(index):
#     list = input().split()
#     num = float(list[0])
#     print("{:.2f}".format(calculation(num,list)))

# #2675
# index = int(input())
# for i in range(index):
#     count, str = input().split()
#     count = int(count)
#     for x in str:
#         print(x*count, end="")
#     print()

# #10817
# a, b, c = map(int, input().split())
# list = [a, b, c]
# list.sort()
# print(list[1])

# #11653
# number = int(input())
# i = 1
# count = 0
# while number != 0:
#     number -= i
#     i += 1
#     count += 1
#     if number < 0:
#         count -= 1
#         break
# print(count)

# #1934
# 방법 1
# def calculation(a, b):
#     answer = 1
#     minN = min(a,b)
#     while a != 1 and b != 1: #둘중하나라도 1이면 끝
#         for i in range(2, minN+1):
#             if a%i==0 and b%i==0:
#                 a = a//i
#                 b = b//i
#                 answer *= i
#                 break
#             elif i == minN: #최대 공약수가 1이면 끝
#                 answer = answer * a * b
#                 return answer
#     answer = answer * a * b
#     return answer
# index = int(input())
# for i in range(index):
#     a, b = map(int, input().split())
#     answer = calculation(a, b)
#     print(answer)
# 방법 2
# from math import *
# index = int(input())
# for i in range(index):
#     a, b = map(int, input().split())
#     answer = lcm(a, b)
#     print(answer)

# #4101
# while True:
#     a, b = map(int, input().split())
#     if a == 0 and b == 0:
#         break
#     elif a>b:
#         print("Yes")
#     else:
#         print("No")

# #3009
# x = []
# y = []
# for i in range(3):
#     a, b = map(int, input().split())
#     if a in x:
#         x.remove(a)
#     else:
#         x.append(a)
#     if b in y:
#         y.remove(b)
#     else:
#         y.append(b)
# print(x[0], y[0])

# #2476
# n = int(input())
# max_prize = 0
# for i in range(n):
#     a, b, c = map(int, input().split())
#     prize = 0;
#     if a == b == c:
#         prize = 10000+a*1000
#     elif a == b or a == c:
#         prize = 1000 + a*100
#     elif b == c:
#         prize = 1000 + b*100
#     elif a != b != c:
#         prize = max(a,b,c)*100
#     max_prize = max(prize, max_prize)
# print(max_prize)

#2754
# score = input()
# num = 0
# if score[0]=="A":
#     num = 4.0
# elif score[0]=="B":
#     num = 3.0
# elif score[0]=="C":
#     num = 2.0
# elif score[0]=="D":
#     num = 1.0
# elif score[0]=="F":
#     num = 0.0
# if(len(score) > 1):
#     if score[1]=="+":
#         num += 0.3
#     elif score[1]=="-":
#         num -= 0.3
#
# print(num)

# #2884
# hour, minute = map(int, input().split())
# if minute < 45:
#     hour -= 1
#     minute += 60
# minute -= 45
#
# if hour < 0:
#     hour += 24
#
# print(hour, minute)

# #7567
# plate_list = input()
# plate = plate_list[0]
# total_len = 10
# for i in plate_list[1:]:
#     if plate == i:
#         total_len += 5
#     else:
#         total_len += 10
#     plate = i
# print(total_len)

#5063
# n = int(input())
# list = []
# for i in range(n):
#     r, e, c = map(int, input().split())
#     if r > (e-c):
#         list.append(-1)
#     elif r == (e-c):
#         list.append(0)
#     else:
#         list.append(1)
#
# for i in list:
#     if i == -1:
#         print("do not advertise")
#     elif i == 0:
#         print("does not matter")
#     else:
#         print("advertise")

# #10102
# n = int(input())
# result_list = input()
# a = result_list.count("A")
# b = result_list.count("B")
# if a > b:
#     print("A")
# elif a == b:
#     print("Tie")
# else:
#     print("B")

# #10886
# n = int(input())
# result_list = []
# for i in range(n):
#     result_list += [int(input())]
#
# if result_list.count(0) > result_list.count(1):
#     print("Junhee is not cute!")
# else:
#     print("Junhee is cute!")

# #10988
# str = input()
# len_str = len(str)
# result = 1
# for i in range(len_str//2):
#     if(str[i] == str[len_str-1]):
#         len_str -= 1
#         continue
#     else:
#         result = 0
#         break
#
# print(result)

# #5086
# while True:
#     a, b = map(int, input().split())
#     if a==0 and b==0:
#         break
#     elif a % b == 0:
#         print("multiple")
#     elif b % a == 0:
#         print("factor")
#     else:
#         print("neither")

# #9610
# n = int(input())
# result = [0, 0, 0, 0, 0]
# for i in range(n):
#     x, y = map(float, input().split())
#     if x==0 or y==0:
#         result[0] += 1
#     elif x>0 and y>0:
#         result[1] += 1
#     elif x<0 and y>0:
#         result[2] += 1
#     elif x<0 and y<0:
#         result[3] += 1
#     elif x>0 and y<0:
#         result[4] += 1
#
# for i in range(1,5):
#     print(f"Q{i}: {result[i]}")
#
# print("AXIS:", result[0])

# #9606
# while True:
#     n = int(input())
#     result = [1, ]
#     if n == -1:
#         break
#     i = 2
#     while (i <= n//i):
#         if n%i == 0:
#             if i != n//i:
#                 result.append(i)
#             result.append(n//i)
#         i += 1
#     result.sort()
#     print(result)
#     if(sum(result) == n and n != 1):
#         separator = " + "
#         print(f"{n} =",separator.join(map(str, result)))
#     else:
#         print(f"{n} is NOT perfect.")

# #8958
# n = int(input())
# for _ in range(n):
#     quiz_value = input()
#     total_score = 0
#     recent_score = 0
#
#     for i in quiz_value:
#         if i == "O":
#             recent_score += 1
#             total_score += recent_score
#         else:
#             recent_score = 0
#     print(total_score)

# n = int(input())
# for _ in range(n):
#     quiz_value = input()
#     count = 0
#     sum = 0
#     for i in quiz_value:
#         if i == "O":
#             count+=1
#             sum+=count
#         else:
#             count = 0
#
#     print(sum)

# #10162
# m = int(input())
# a=0
# b=0
# c=0
# while m > 0:
#     if m >= 300:
#         a += 1
#         m -= 300
#     elif m >= 60:
#         b += 1
#         m -= 60
#     else:
#         c += 1
#         m -= 10
# if m >= 0:
#     print(a, b, c)
# else:
#     print(-1)

#10103
# n = int(input())
# c_score = 100
# s_score = 100
# for i in range(n):
#     a, b = map(int, input().split())
#     if a > b:
#         s_score -= a
#     elif a < b:
#         c_score -= b
#
# print(c_score)
# print(s_score)

# #10214
# n = int(input())
# for i in range(n):
#     yensei_score = 0
#     korea_score = 0
#     for _ in range(9):
#         a, b = map(int, input().split())
#         yensei_score += a
#         korea_score += b
#
#     if yensei_score> korea_score:
#         print("Yonsei")
#     elif yensei_score < korea_score:
#         print("Korea")
#     else:
#         print("Draw")
#
# #11557
# n = int(input())
# for _ in range(n):
#     uv_count = int(input())
#     uv_max = ""
#     alcohol_max = 0
#     for _ in range(uv_count):
#         uv, alcohol = input().split()
#         alcohol = int(alcohol)
#         if alcohol > alcohol_max:
#             alcohol_max = alcohol
#             uv_max = uv
#     print(uv_max)

# #10757
# a, b = input().split()
# result = []
# carry = 0
# a = a[::-1]
# b = b[::-1]
# a_len = len(a)
# b_len = len(b)
# max_len = max(a_len, b_len)
#
# #print(a, b) #12345 789 54321 98700
# if a_len > b_len:
#     for i in range(b_len, a_len):
#         b = b + "0"
# else:
#     for i in range(a_len, b_len):
#         a = a + "0"
#
# for i in range(max_len):
#     v1 = int(a[i])
#     v2 = int(b[i])
#     #print(v1, v2)
#     v3 = v1 + v2 + carry
#     if i == max_len-1 and v3 > 9:
#         result.insert(0, v3)
#     elif v3 > 9:
#         result.insert(0, v3 - 10)
#         carry = 1
#     elif v3 < 10:
#         result.insert(0, v3)
#         carry = 0
#
# #print(result)
# for x in result:
#     print(x, end="")
# a, b = map(int, input().split())
# print(sum(a,b))

#1408
# present_time = list(map(int, input().split(":")))
# pre_time = list(map(int, input().split(":")))
# for i in [2, 1, 0]:
#     a = pre_time[i] - present_time[i]
#     if a < 0 and i != 0:
#         pre_time[i] = a + 60
#         pre_time[i-1] = pre_time[i-1]-1
#     else:
#         pre_time[i] = a
#         if a < 0:
#             pre_time[i] += 24
#
#
# print(str(pre_time[0]).zfill(2)+":"+str(pre_time[1]).zfill(2)+":"+str(pre_time[2]).zfill(2))

# #1977
# from math import sqrt, ceil
#
# a1 = int(input())
# b1 = int(input())
#
# a2 = ceil(sqrt(a1))
# b2 = int(sqrt(b1))
#
# result = []
# for i in range(a2, b2+1):
#     result.append(i*i)
#
# if result:
#     print(sum(result))
#     print(result[0])
# else:
#     print(-1)

# #11098
# n = int(input())
# list = []
# for i in range(n):
#     count = int(input())
#     large_price = 0
#     large_name = ""
#     for j in range(count):
#         price, name = input().split()
#         price = int(price)
#         if price > large_price:
#             large_price = price
#             large_name = name
#     list.append(large_name)
# for item in list:
#     print(item)

# #5635
# n = int(input())
#
# young_name =""
# young_birth = [1980, 0, 0]
# old_name = ""
# old_birth = [2020, 13, 32]
#
# for _ in range(n):
#     name, day, month, year = input().split()
#     birth = [year, month, day]
#     birth = list(map(int, birth))
#
#     for i in range(3):
#         if birth[i] < old_birth[i]:
#             old_birth = birth
#             old_name = name
#             break
#         elif birth[i] == old_birth[i]:
#             continue
#         else:
#             break
#
#     for i in range(3):
#         if birth[i] > young_birth[i]:
#             young_birth = birth
#             young_name = name
#             break
#         elif birth[i] == young_birth[i]:
#             continue
#         else:
#             break
#
# print(young_name)
# print(old_name)

# #2742
# num = int(input())
# for i in range(num, 0, -1):
#     print(i)

# #2609
# a, b = map(int, input().split())
# min_num = min(a, b)
# list = []
# i = 2
# while i <= min_num:
#     if a % i == 0 and b % i == 0:
#         list.append(i)
#         a = a // i
#         b = b // i
#         min_num = min(a, b)
#         continue
#     i += 1
#
# divisor_num = 1
# factor_num = 1
# for i in list:
#     divisor_num *= i
# factor_num = divisor_num * a * b
# print(divisor_num)
# print(factor_num)

# #2748
# memo = {0: 0, 1: 1, 2: 1}
# def fib(n):
#     if n in memo:
#         return memo[n]
#     else:
#         memo[n] = fib(n-2) + fib(n-1)
#         return memo[n]
#
# n = int(input())
# print(fib(n))

# #5565
# total_price = int(input())
# sum = 0
# for _ in range(9):
#     price = int(input())
#     sum += price
#
# print(total_price - sum)

# #10950
# while True:
#     a, b = map(int, input().split())
#     if a == 0 and b == 0:
#         break
#     print(a+b)

# #10984
# n = int(input())#학기수
# list_c = []
# list = []
# for _ in range(n):
#     total_c = 0
#     total_g = 0
#     s = int(input())  # 과목수
#     for _ in range(s):
#         c, g = map(float, input().split())#학점/점수
#         total_c += c
#         total_g += (g*c)
#     list_c.append(total_c)
#     list.append(total_g/total_c)
#
# for i in range(n):
#     print(int(list_c[i]), round(list[i], 1))

# #10833
# n = int(input())
# rest_num = 0
# for _ in range(n):
#     stu_num, apple_num = map(int ,input().split())
#     rest_num += (apple_num % stu_num)
#
# print(rest_num)

# #2442
# n = int(input())
# for i in range(n):
#     j = n-i-1
#     print(" " * j, end="")
#     print("*" * i, end="")
#     print("*", end="")
#     print("*" * i)

# #2443
# n = int(input())
# nn = n*2-1 # 012345678
# for i in range(nn):
#     if i >= n: #5678
#         i = nn-1-i
#     print(" " * (n-i-1), end="")#43210
#     print("*" * i, end="")#01234
#     print("*", end="")
#     print("*" * i)

# #9325
# n = int(input())
# result = []
# for _ in range(n):
#     price = int(input())
#     option_num = int(input())
#     for _ in range(option_num):
#         q, p = map(int, input().split())
#         price += (q*p)
#     result.append(price)
#
# for i in result:
#     print(i)

# #2010
# import sys #성능개선
# input = sys.stdin.readline
#
# n = int(input())
# list = []
# for _ in range(n):
#     i = int(input())
#     list.append(i)
# print(sum(list)-(n+1))

# #2523
# import sys
# input = sys.stdin.readline
#
# n = int(input()) #5
# nn = n*2-1 #9
# for i in range(nn):#012345678
#     if i >= n: #5678 -> 3210
#         i = nn-1-i
#     print("*" * (i+1))

# #10178
# import sys
# s = sys.stdin.readline
#
# n = int(s())
# for _ in range(n):
#     candy, count = map(int, input().split())
#     dad_candy = candy % count
#     child_candy = candy // count
#     print("You get {1} piece(s) and your dad gets {0} piece(s).".format(dad_candy, child_candy))

# #9295
# n = int(input())
# sum_list = []
# for _ in range(1, n+1):
#     a, b = map(int, input().split())
#     sum_list.append(a+b)
# i=1
# for s in sum_list:
#     print(f"Case {i}: {s}")
#     i+=1

# #10569
# n = int(input())
# list = []
# for _ in range(n):
#     a, b = map(int, input().split())
#     list.append(2 - a + b)
#
# for i in list:
#     print(i)

# #2921
# n = int(input())
# total = 0
# for i in range(n+1):
#     for j in range(i, n+1):
#         total += i
#         total += j
#
# print(total)

# #10871
# N, X = map(int, input().split())
# P = list(map(int, input().split()))
#
# for i in P:
#     if i < X:
#         print(i, end=" ")

# #10872
# memo = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120}
# def factorial(n):
#     if n in memo:
#         return memo[n]
#     else:
#         memo[n] = n * factorial(n-1)
#         return memo[n]
#
# n = int(input())
# print(factorial(n))

# #1978
# def prime_num(n): #소수면 1, 소수가 아니면 0
#     if n == 1:
#         return 0
#     else:
#         for i in range(2, n):
#             if n%i == 0:
#                 return 0
#         return 1
#
# n = int(input())
# P = list(map(int, input().split()))
# count = 0
# for i in P:
#     if prime_num(i) == 1:
#         count += 1
#
# print(count)

# #2581
# def prime_num(n): #소수면 1, 소수가 아니면 0
#     if n == 1:
#         return 0
#     else:
#         for i in range(2, n):
#             if n%i == 0:
#                 return 0
#         return 1
#
# a = int(input())
# b = int(input())
# prime_min = -1
# sum = 0
# for i in range(a, b+1):
#     if prime_num(i) == 1 and prime_min == -1:
#         prime_min = i
#         sum += i
#     elif prime_num(i) == 1:
#         sum += i
#
# if sum > 0:
#     print(sum)
# print(prime_min)

# #2445
# n = int(input()) #5
# nn = n * 2 - 1 #9 nn-1=8
# for i in range(nn): #01234 56789
#     if i >= n:
#         i = nn-1-i
#     print("*"*(i+1), end="")#12345
#     print(" "*(nn-1-(i*2)), end="")#86420
#     print("*"*(i+1))

# #2501
# n, k = map(int, input().split())
# count = 0
# i = 1
#
# while i <= n:
#     if n % i == 0:
#         count += 1
#         if count == k:
#            print(i)
#            break
#     i += 1
#
# if count < k:
#     print(0)

# #2562-1
# max_num = 0
# index = 0
# for i in range(1, 10):
#     a = int(input())
#     if a > max_num:
#         index = i
#         max_num = a
#
# print(max_num)
# print(index)
#
# #2562-2
# index = []
# result = []
# for i in range(9):
#     a = int(input())
#     index.append(a)
#     result.append(a)
#
# result.sort()
# v = result[8]
# print(v)
# print(index.index(v)+1)

# #2475
# numbers = list(map(int, input().split()))
# sum = 0
# for i in numbers:
#     sum += i*i
# print(sum%10)

# #2576
# odd = []
# for _ in range(7):
#     a = int(input())
#     if a % 2 == 1:
#         odd.append(a)
#
# odd.sort()
# if odd:
#     print(sum(odd))
#     print(odd[0])
# else:
#     print(-1)

# #2747
# memo = {0: 0, 1: 1, 2: 1}
# def fib(n):
#     if n in memo:
#         return memo[n]
#     else:
#         memo[n] = fib(n-2) + fib(n-1)
#         return memo[n]
#
# n = int(input())
# print(fib(n))

# #9085
# n = int(input())
# result = []
# for _ in range(n):
#     s = int(input())
#     numbers = list(map(int, input().split()))
#     result.append(sum(numbers))
#
# for i in result:
#     print(i)

# #2490
# result = []
# for _ in range(3):
#     a = list(map(int, input().split()))
#     result.append(sum(a))
#
# for i in result:#01234 윺 걸 개 도 모 (D C B A E)
#     if i == 0:
#         print("D")
#     elif i == 1:
#         print("C")
#     elif i == 2:
#         print("B")
#     elif i == 3:
#         print("A")
#     else:
#         print("E")

# #10797
# n = int(input())
# cars = list(map(int, input().split()))
# count = 0
# for i in cars:
#     if n == i:
#         count += 1
#
# print(count)

# #2506
# score = 0
# total = 0
# n = int(input())
# answer = list(map(int, input().split()))
# for i in answer:
#     if i == 1:
#         score += 1
#         total += score
#     else:
#         score = 0
# print(total)

# #1546
# n = int(input())
# scores = list(map(float, input().split()))
# max_score = max(scores)
# new_score = []
# for i in scores:
#     i = i/max_score*100
#     new_score.append(i)
#
# print(round(sum(new_score)/n, 6))

# #2455
# total = 0
# result = []
# for _ in range(4):
#     a, b = map(int, input().split())
#     total -= a
#     result.append(total)
#     total += b
#     result.append(total)
#
# result.sort()
# print(result[7])

# #10995
# n = int(input())
# for i in range(1, n+1):
#     if i % 2 == 1: #홀수
#         print("* "*n)
#     else:
#         print(" *"*n)

# #10991
# n = int(input())
# for i in range(n):#0123
#     print(" " * (n - i-1), end="")
#     for _ in range(i+1):
#         print("*"*1, end="")
#         print(" "*1, end="")
#     print()

# #12865
# from itertools import combinations
# N, K = map(int, input().split())
# bag = {}
# max = 0
# for _ in range(N):
#     W, V = map(int, input().split())
#     bag[W] = V
#
# #print(bag)
# w_list = list(bag.keys())
# w_list.sort()
# #print(w_list)
# result = []
# for i in range(1, N+1): #1개부터 n개까지 뽑기
#     result = list(combinations(w_list,i))
#     result = [list(item) for item in result]
#     print(result)
#     for j in result:
#         total = 0
#         if sum(j) <= K:
#             for w in j:
#                 total += bag.get(w)
#             print(total)
#             if total > max:
#                 max = total
# print(max)

