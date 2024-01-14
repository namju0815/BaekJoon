# #23881
# #1.주어진 배열에서 최솟값을 뽑는다
# #2.그 값을 맨 앞에 위치한 값과 교체한다
# #3.맨 청음 위치를 뺀 나머지 리스트를 같은방법으로 교체
# #4.하나의 원소만 남을 때 까지 1-3과정 반복
# import sys
# input = sys.stdin.readline
#
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
#
# count = 0
#
# for i in range(N-1, 0, -1):
#     if K == count:
#         break
#     maxNumber = max(A[:i+1])
#     if maxNumber == A[i]:
#         continue
#     maxIndex = A.index(maxNumber)
#     data = A[i]
#     A[i] = maxNumber
#     A[maxIndex] = data
#     count += 1
#
# if count < K:
#     print(-1)
# elif data < maxNumber:
#     print(data, maxNumber)
# else:
#     print(maxNumber, data)

# #23883
# import sys
# input = sys.stdin.readline
#
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
#
# count = 0
# index = N-1
# sorted_A = sorted(A)
# d = {}
#
# for index, value in enumerate(A):
#     d[value] = index
#
# while True:
#     if index == -1:
#         break
#     if count == K:
#         print(data, maxNumber)
#         break
#     maxNumber = sorted_A[index]
#     data = A[index]
#     if maxNumber != data:
#         maxIndex = d.get(maxNumber)
#         count += 1
#         A[maxIndex] = data
#         d[data] = maxIndex
#     A[index] = 0
#     index -= 1
#
# if count < K:
#     print(-1)

# #23884
# import sys
# input = sys.stdin.readline
#
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
#
# count = 0
# index = N-1
# sorted_A = sorted(A)
# d = {}
#
# for index, value in enumerate(A):
#     d[value] = index
#
# while True:
#     if index == -1:
#         break
#     if count == K:
#         for i in A:
#             print(i, end=" ")
#         break
#     maxNumber = sorted_A[index]
#     data = A[index]
#     if maxNumber != data:
#         maxIndex = d.get(maxNumber)
#         count += 1
#         A[maxIndex] = data
#         d[data] = maxIndex
#     A[index] = maxNumber
#     index -= 1
#
# if count < K:
#     print(-1)

#23899 23900
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
arr = list(map(int, input().split()))

index = N-1
sorted_A = sorted(A)
d = {}
check = 0

for index, value in enumerate(A):
    d[value] = index

while index >= 0:
    if A == arr:
        check = 1
        break
    maxNumber = sorted_A[index]
    data = A[index]
    if maxNumber != data:
        maxIndex = d.get(maxNumber)
        A[maxIndex] = data
        d[data] = maxIndex
    A[index] = maxNumber
    index -= 1

print(check)




