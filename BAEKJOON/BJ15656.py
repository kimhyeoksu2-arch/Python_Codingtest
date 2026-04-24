import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = map(int, input().split())

rs = []

# arr sort하기
arr_sort = sorted(arr)

def recur(num):
    if num == m:
        print(' '.join(map(str, rs)))
        return
    for i in range(0, n):
        rs.append(arr_sort[i])
        recur(num+1)
        rs.pop()
        
recur(0)
