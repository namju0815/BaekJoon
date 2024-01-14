# #2042
# import sys
# input = sys.stdin.readline
# n, m, k = map(int, input().split())
# def get_segment_tree_size(n): #n: 배열의 크기
#     i = 1
#     while i < n:
#         i = i*2
#     return i*2
#
# #arr: 입력받은 배열, tree: 세그먼트 트리, node: 세그먼트 트리 index, start:범위 첫번째 end: 범위 끝
# def build_segment_tree(arr, tree, node, start, end):
#     if start == end: #리프노드를 찾으면, 하나씩 대입
#         tree[node] = arr[start]
#         return
#     mid = (start+end)//2
#     build_segment_tree(arr, tree, node*2, start, mid)
#     build_segment_tree(arr, tree, node*2+1, mid+1, end)
#     tree[node] = tree[node*2] + tree[node*2+1]
#
# def update_segment_tree(tree, index, plus):
#     while index > 0:
#         tree[index] += plus
#         index//=2
#
# def sum_segment_tree(tree, node, start, end, left, right):
#     if left > end or right < start:
#         return 0
#     if left <= start and end <= right:
#         #print(node, tree[node])
#         return tree[node]
#     mid = (start + end)//2
#     l_sum = sum_segment_tree(tree, 2*node, start, mid, left, right)
#     r_sum = sum_segment_tree(tree, 2*node+1, mid+1, end, left, right)
#     return l_sum + r_sum
#
# #리프노드개수
# N = get_segment_tree_size(n)
# #print(N)
#
# arr = [0] * N
# segment_tree = [0] * 2 * N #세그먼트 트리 생성
# for i in range(n):
#     arr[i] = int(input())
# #print(arr)
# #end:모든 배열의 값이 레벨이 같은 리프노드에 들어오게 설정하기위해 N-1(7)로 설정
# build_segment_tree(arr, segment_tree, 1, 0, N-1)
# #print(segment_tree)
#
# for _ in range(m+k):
#     a, b, c = map(int, input().split())
#     index = 0
#     sum = 0
#     if a == 1:
#         plus = c - arr[b-1]
#         arr[b-1] += plus
#         #print(arr)
#         update_segment_tree(segment_tree, N+b-1, plus)
#         #print(segment_tree)
#     elif a == 2:
#         sum = sum_segment_tree(segment_tree, 1, 1, N, b, c)
#         print(sum)

# #10999
# import sys
# input = sys.stdin.readline
# n, m, k = map(int, input().split())
#
# def get_segment_tree_size(n): #n: 배열의 크기
#     i = 1
#     while i < n:
#         i = i*2
#     return i
#
# def build_segment_tree(arr, tree, node, start, end):
#     if start == end: #리프노드를 찾으면, 하나씩 대입
#         tree[node] = arr[start]
#         return
#     mid = (start+end)//2
#     build_segment_tree(arr, tree, node*2, start, mid)
#     build_segment_tree(arr, tree, node*2+1, mid+1, end)
#     tree[node] = tree[node*2] + tree[node*2+1]
#
# def update_lazy(tree, lazy, node, start, end):
#     if lazy[node] != 0:
#         tree[node] += (end-start+1)*lazy[node]
#         if start != end:
#             lazy[node*2] += lazy[node]
#             lazy[node*2+1] += lazy[node]
#         lazy[node] = 0
# def update_lazy_segment_tree(tree, lazy, node ,start, end, left, right, data):
#     update_lazy(tree, lazy, node, start, end)
#     if start > end or start > right or end < left:
#         return
#
#     if left <= start and end <= right: #!!!start ~ end(구간)이 구하려는 left~right에 포함되는지
#             tree[node] += (end-start+1) * data
#             if start != end:
#                 lazy[node*2] += data
#                 lazy[node*2+1] += data #자식노드에 lazy푸쉬다운
#             return
#
#     #구간에 포함되지 않으면 게속쪼개서 내려가기
#     mid = (start+end)//2
#     update_lazy_segment_tree(tree, lazy, node*2, start, mid, left, right, data)
#     update_lazy_segment_tree(tree, lazy, node*2+1, mid+1, end, left, right, data)
#     tree[node] = tree[node*2] + tree[node*2+1]
#
# def sum_segment_tree(tree, lazy, node, start, end, left, right):
#     update_lazy(tree, lazy, node, start, end)
#     if start > end or start > right or end < left:
#         return 0
#     if left <= start and end <= right:
#         #print(node, tree[node])
#         return tree[node]
#
#     mid = (start + end)//2
#     l_sum = sum_segment_tree(tree, lazy, 2*node, start, mid, left, right)
#     r_sum = sum_segment_tree(tree, lazy, 2*node+1, mid+1, end, left, right)
#     return l_sum + r_sum
#
# #리프노드개수
# N = get_segment_tree_size(n)
# #print(N)
#
# arr = [0] * N
# segment_tree = [0] * 2 * N
# lazy = [0] * 2 * N #세그먼트 노드개수와 같게 세팅
#
# for i in range(n):
#     arr[i] = int(input())
# #print(arr)
#
# build_segment_tree(arr, segment_tree, 1, 0, N-1)
# #print(segment_tree)
#
# for _ in range(m+k):
#     a = list(map(int, input().split()))
#     left = a[1] - 1;
#     right = a[2] - 1
#     if a[0] == 1:
#         update_lazy_segment_tree(segment_tree, lazy, 1, 0, N - 1, left, right, a[3])
#     elif a[0] == 2:
#         sum = sum_segment_tree(segment_tree, lazy, 1, 0, N-1, left, right)
#         print(sum)

# #11659
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
#
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
#         mid = (end+start)//2
#         l_sum = sum_segment_tree(tree, node*2, start, mid, left, right)
#         r_sum = sum_segment_tree(tree, node*2+1, mid+1, end, left, right)
#         return l_sum + r_sum
#
# N = get_segment_tree_size(n)
# #print(N)
# arr = list(map(int, input().split()))
# for _ in range(N-n):
#     arr.append(0)
# #print(arr)
#
# segment_tree = [0] * N * 2
# build_segment_tree(arr, segment_tree, 1, 0, N-1)
# #print(segment_tree)
#
# for _ in range(m):
#     i, j = map(int, input().split())
#     sum = sum_segment_tree(segment_tree, 1, 0, N-1, i-1, j-1)
#     print(sum)

# #11003
# import sys
# input = sys.stdin.readline
#
# n, l = map(int, input().split())
#
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
#     tree[node] = min(tree[node*2],tree[node*2+1])
#
# def min_segment_tree(tree, node, start, end, left, right):
#     if start > right or left > end:
#         return 5000001
#     elif left <= start and end <= right:
#         return tree[node]
#     else:
#         mid = (end + start) // 2
#         l_sum = min_segment_tree(tree, node * 2, start, mid, left, right)
#         r_sum = min_segment_tree(tree, node * 2 + 1, mid + 1, end, left, right)
#         return min(l_sum, r_sum)
#
# N = get_segment_tree_size(n)
# #print(N)
# arr = list(map(int, input().split()))
# N = get_segment_tree_size(n)
# arr += [5000001] * (N - n)  # 배열을 2^n 크기로 확장하고 나머지 부분을 0으로 초기화
#
# #print(arr)
#
# segment_tree = [0] * N * 2
# build_segment_tree(arr, segment_tree, 1, 0, N-1)
# #print(segment_tree)
# answer = arr[0]
# for i in range(n):
#     if i < l-1:
#         answer = min(answer, arr[i])
#     else:
#         answer = min_segment_tree(segment_tree, 1, 0, N-1, i-l+1, i)
#     print(answer, end=" ")


#17411
import sys
input = sys.stdin.readline



