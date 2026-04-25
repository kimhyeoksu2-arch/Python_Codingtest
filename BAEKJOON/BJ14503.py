import sys
input = sys.stdin.readline

n, m = map(int, input().split())
y, x, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while 1:
    
    if map[y][x] == 0:
        map[y][x] = 2
        cnt += 1
        
    chk = False
    
    for i in range(1, 5):
        nd = (d-i) % 4
        
        ny = y + dy[d-i]
        nx = x + dx[d-i]
        
        if 0<ny<=n and 0<nx<=m:
            
            if map[ny][nx] == 0:
                y = ny
                x = nx
                d = nd
                chk = True
                break
    
    if chk == False:     
        ny = y - dy[d]
        nx = x - dx[d]
        
        if 0<ny<=n and 0<nx<=m and map[ny][nx] != 1:
            y = ny
            x = nx
            
        else:
            break
       
print(cnt)
