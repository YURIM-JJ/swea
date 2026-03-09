T = int(input())
for tc in range(1, T+1):
 
    N, M = map(int, input().split())
 
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    max_sum = 0
 
    for y in range(N):
        for x in range(M):
 
            total_sum = arr[y][x]
 
            for dy, dx in [(0, 1),(-1, 0),(0, -1),(1, 0)]:
                ny = dy + y
                nx = dx + x
 
                if 0<= ny <N and 0<= nx <M:
                    total_sum += arr[ny][nx]
 
            if max_sum < total_sum:
                max_sum = total_sum
 
    print(f'#{tc} {max_sum}')
