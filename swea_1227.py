import sys
sys.stdin = open("C:\\dbfan_py\\셤셤셤\\20260303_월말평가\\미로2.txt", encoding="utf-8")

def dfs(st_y, st_x, arr):

    st = [(st_y, st_x)]
    arr[st_y][st_x] = 1

    while st:
        cy, cx = st.pop()    

        for dy, dx in [(0,1),(-1,0),(0,-1),(1,0)]:
            ny = dy + cy
            nx = dx + cx

            if 0<=ny<N and 0<=nx<N and arr[ny][nx] != 1:
                if arr[ny][nx] == 3:
                    return 1
                
                arr[ny][nx] = 1
                st.append((ny, nx))
    return 0

from collections import deque

def bfs(st_y, st_x, arr):
    que = deque([(st_y, st_x)])
    arr[st_y][st_x] = 1

    while que:
        cy, cx = que.popleft()
        
        for dy, dx in [(0,1),(-1,0),(0,-1),(1,0)]:
            ny = cy + dy
            nx = cx + dx

            if 0<=ny<N and 0<=nx<N and arr[ny][nx] != 1:
                if arr[ny][nx] ==3:
                    return 1
                
                arr[ny][nx] = 1
                que.append((ny,nx))
    return 0


for _ in range(1, 11):

    N = 100
    T = int(input())

    arr = [list(map(int, input())) for _ in range(N)]

    for y in range(N):
        for x in range(N):

            if arr[y][x] == 2:
                st_y = y
                st_x = x
    
    result = dfs(st_y, st_x, arr)
    result = bfs(st_y, st_x, arr)

    print(f'#{T} {result}')
