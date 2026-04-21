import sys
sys.stdin = open('swea_1767_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for y in range(N):
        for x in range(N):
            arr[y][x] == 1
            ㄴ