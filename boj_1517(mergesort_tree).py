import sys
input = sys.stdin.readline


def merge_sort(arr1, arr2):
    merge = []
    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i == len(arr1):
            merge.extend(arr2[j:])
            break
        if j == len(arr2):
            merge.extend(arr1[i:])
            break
        if arr1[i] <= arr2[j]:
            merge.append(arr1[i])
            i += 1
        else:
            merge.append(arr2[j])
            answer[0] += len(arr1) - i
            j += 1
    return merge


def init_tree(start, end, node):
    if start == end:
        tree[node] = [arr[start]]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = merge_sort(init_tree(start, mid, node*2), init_tree(mid+1, end, node*2+1))
    return tree[node]


n = int(input())
arr = list(map(int, input().split()))
answer = [0]
tree = [0] * (4*n)
init_tree(0, n-1, 1)
print(answer[0])

