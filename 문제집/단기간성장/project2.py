#10775
G = int(input())
P = int(input())
check = [0] * G

for i in range(P):
    f_num = int(input())
    if check[f_num-1] == 0:
        check[f_num-1] = 1

print(check.count(1))