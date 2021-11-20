import sys
input = sys.stdin.readline

string_A = ("-" + input())[:-1]
string_B = ("-" + input())[:-1]
arr = [[0] * len(string_A) for _ in range(len(string_B))]
for i in range(1,len(string_B)):
    for j in range(1,len(string_A)):
        if string_B[i] == string_A[j]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])

print(arr[len(string_B)-1][len(string_A)-1])
