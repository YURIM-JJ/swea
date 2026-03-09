import sys
sys.stdin = open("C:\\dbfan_py\\셤셤셤\\20260303_월말평가\\미로1.txt", encoding="utf-8")

# def dfs(st_y, st_x, arr):

#     st = [(st_y, st_x)]
#     arr[st_y][st_x] = 1

#     while st:
#         cy, cx = st.pop()

#         for dy,dx in [(0,1),(-1,0),(0,-1),(1,0)]:
#             ny = dy + cy
#             nx = dx + cx

#             if 0<=ny<N and 0<=nx<N and arr[ny][nx] != 1:
#                 if arr[ny][nx] == 3:
#                     return 1
                
#                 arr[ny][nx] = 1 
#                 st.append((ny, nx))

#     return 0

from collections import deque

def bfs(st_y, st_x, arr):
    q = deque([(st_y, st_x, 0)])
    arr[st_y][st_x] = 1

    while q:
        cy, cx, cnt = q.popleft()

        for dy, dx in [(0,1), (-1,0),(0,-1),(1,0)]:
            ny = dy + cy
            nx = dx + cx

            if 0<=ny<N and 0<=nx<N and arr[ny][nx] != 1:
                if arr[ny][nx] == 3:
                    return cnt + 1
                
                arr[ny][nx] = 1
                q.append((ny, nx))
    return 0

for tc in range(1, 11):
    
    N = 16
    T = int(input())

    arr = [list(map(int, input())) for _ in range(N)]

    for y in range(N):
        for x in range(N):

            if arr[y][x] == 2:
                st_y = y
                st_x = x
    
    # result = dfs(st_y, st_x, arr)
    result = bfs(st_y, st_x, arr)

    print(f'#{T} {result}')