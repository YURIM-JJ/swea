import sys
sys.stdin = open('input_1949.txt')

def recur(row, col, cut_cnt, path_len):
    global result
    visited[row][col] = True
    result = max(result, path_len)

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        newr, newc = row+dr, col+dc
        if 0<=newr<N and 0<=newc<N and not visited[newr][newc]:
            if arr[row][col] > arr[newr][newc]:
                recur(newr, newc, cut_cnt, path_len+1)
            elif cut_cnt==0 and arr[newr][newc]-K<arr[row][col]:
                temp = arr[newr][newc]
                arr[newr][newc] = arr[row][col]-1
                recur(newr, newc, 1, path_len+1)
                arr[newr][newc] = temp 

    visited[row][col] = False

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxv = max(map(max, arr))
    # print(maxv)
    # print(arr)
    result = 0
    visited = [[False]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if arr[row][col] == maxv:
                recur(row, col, 0, 1)

    print(result)