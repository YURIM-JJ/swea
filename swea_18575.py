T = int(input())
for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total_list = []

    for y in range(N):
        for x in range(N):

            total_sum = 0

            for i in range(N):
                total_sum += arr[y][i] + arr[i][x]
            
            total_sum -= arr[y][x]
            total_list.append(total_sum)
        
    print(f'#{tc} {max(total_list)-min(total_list)}')
