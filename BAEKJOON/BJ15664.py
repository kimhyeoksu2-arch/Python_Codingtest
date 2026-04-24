import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))

rs = []
chk = [False] * (n)

def recur(num, start):
    if num == m :
        print(' '.join(map(str, rs)))
        return
    last_used = 0
    for i in range(start, n):
        if chk[i] == False and last_used != arr[i]:
            rs.append(arr[i])
            chk[i] = True
            last_used=arr[i]
            recur(num+1, i)
            rs.pop()
            chk[i] = False
            
recur(0, 0)
