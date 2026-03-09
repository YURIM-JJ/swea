# 1번
# def miro(x, y, total):
#
#     if x == N-1 and y == N-1:
#         total = sum(path)
#         print(f'{tc} {total}')
#         return
#
#     for y in range(N):
#         for x in range(N):
#
#             path.append(arr[y][x])
#
#             for dy, dx in [(0,1),(-1,0),(0,-1),(1,0)]:
#                 ny = y + dy
#                 nx = x + dx
#
#                 if ny == N-1 and nx == N-1:
#                     continue
#                 else:
#                     if 0<=ny<N and 0<=nx<N and arr[ny][nx] != -1:
#                         path.append(arr[ny][nx])
#                         arr[ny][nx] = -1
#
# T = int(input())
# for tc in range(1, T+1):
#
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     path = []
#     total = 0
#
#     miro(0,0,total)


# 2번
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# total = []
# total_sum = []
#
# for y in range(N):
#     for x in range(N):
#
#         # total.append(arr[y][x])
#
#         if y == 2 and x == 2 :
#             break
#         else:
#             total.append(arr[y][x])
#
#             for dy, dx in [(0,1),(-1,0),(0,-1),(1,0)]:
#                 ny = y + dy
#                 nx = x + dx
#
#                 if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] != -1:
#                     total.append(arr[ny][nx])
#                     total_sum.append(sum(total))
#                     arr[ny][nx] = -1
#                     total.pop()
#
#     print(total)
#     # total_sum = 0
#     #
#     # for num in total:
#     #     if num > 0:
#     #         total_sum += num
#     #     else:
#     #         continue
#     print(total_sum)


# 3번
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# total = []
#
# def miro(y, x):
#     total.append(arr[y][x])
#
#     if y == N-1 and x == N-1:
#         print(total)
#         return
#
#     for dy, dx in [(0,1),(1,0)]:
#         ny = y + dy
#         nx = x + dx
#
#         if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] != -1:
#             total.append(arr[ny][nx])
#             miro(ny, nx)
#             total.pop()
#         else:
#             if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == -1:
#                 continue
#
# miro(0, 0)

def recur(row, col):

    if row == N - 1 and col == N - 1:
        path.append(arr[row][col])
        path_sum.append(sum(path))
        path.pop()
        return

    if row+1 < N:
        path.append(arr[row][col])
        recur(row + 1, col)
        path.pop()

    if col+1 < N :
        path.append(arr[row][col])
        recur(row, col + 1)
        path.pop()

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    path = []
    path_sum = []

    recur(0, 0)
    print(f'# {tc} {min(path_sum)}')



