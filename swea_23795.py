# T = int(input())
# for tc in range(1, T+1):

#     N = int(input())

#     arr = [list(map(int, input().split())) for _ in range(N)]

#     cnt = 0
#     no_cnt = 0

#     for y in range(N):
#         for x in range(N):
#             if arr[y][x] == 0:
#                 cnt += 1

#             if arr[y][x] == 2:
#                 for dy, dx in [(0,1),(-1,0),(0,-1),(1,0)]:
#                     for j in range(1, N):
#                         ny = dy*j + y
#                         nx = dx*j + x

#                         if 0<=ny<N and 0<=nx<N:
#                             if arr[ny][nx] == 0:
#                                 no_cnt += 1
#                             else:
#                                 if arr[ny][nx] == 1:
#                                     break

#     print(f'#{tc} {cnt-no_cnt}')


T = int(input())
for tc in range(1, T+1):

    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    for y in range(N):
        for x in range(N):

            if arr[y][x] == 2:
                for dy, dx in [(0,1), (-1,0), (1,0), (0,-1)]:
                    for c in range(1, N):
                        ny = y + (dy*c)
                        nx = x + (dx*c)

                        if 0<=ny<N and 0<=nx<N and arr[ny][nx] == 0:
                            arr[ny][nx] = -1
                        else:
                            break

    for y in range(N):
        for x in range(N):
            if arr[y][x] == 0:
                cnt += 1

    print(f"#{tc} {cnt}")