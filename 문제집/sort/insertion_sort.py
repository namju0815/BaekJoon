#24051
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))

count = 0
for i in range(1, n):
    for j in range(i-1, -1, -1):
        if A[j] < A[j+1]:
            if j != i-1:
                count += 1
                if count == k:
                    print(A[j+1])
            break
        else:
            count += 1
            A[j+1], A[j] = A[j], A[j+1]
            if j == 0:
                count += 1
                if count == k:
                    print(A[j])
            elif count == k:
                print(A[j+1])
if count < k:
    print(-1)
