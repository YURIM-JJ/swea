def recur(row, col, current_sum):
    global min_sum

    # [핵심] 가지치기: 현재까지의 합이 이미 찾은 최소합 이상이면 더 이상 탐색하지 않고 되돌아감
    if current_sum >= min_sum:
        return

    # 목적지 도착 시 최소합 갱신
    if row == N - 1 and col == N - 1:
        if current_sum < min_sum:
            min_sum = current_sum
        return

    # 아래쪽으로 이동
    if row + 1 < N:
        recur(row + 1, col, current_sum + arr[row + 1][col])

    # 오른쪽으로 이동
    if col + 1 < N:
        recur(row, col + 1, current_sum + arr[row][col + 1])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최소합을 비교하기 위해 초기값을 무한대(float('inf'))로 설정
    min_sum = 100000000

    # 시작점 (0, 0)의 값을 누적합 초기값으로 전달
    recur(0, 0, 0)

    print(f'#{tc} {min_sum}')