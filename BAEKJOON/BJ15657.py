import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))

rs = []

def recur(num):
    if num == m:
        print(' '.join(map(str, rs)))
        return
    for i in range(0, n):
        if not rs or rs[-1] <= arr[i]:
            rs.append(arr[i])
            recur(num+1)
            rs.pop()
            
recur(0)
            
