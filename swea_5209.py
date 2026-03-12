# 설계는 depth와 branch 모두 N개
# 세로 col 값을 기준으로 세로 한 곳이 선택되었다면 row값이 바뀌더라도
# 선택된 col 은 그냥 넘어가라 그렇게 하나씩 확인해보자

T = int(input())
for tc in range(1, T+1):

    def check(row, col):

        for i in range(row):
            if visited[i][col]:
                return True

        return False

    def recur(row, total_sum):
        global min_total

        if total_sum >= min_total:
            return

        if row == N:
            if min_total > total_sum:
                min_total = total_sum
            return min_total

        for col in range(N):
            if check(row, col):
                continue

            visited[row][col] = 1
            recur(row + 1, total_sum + arr[row][col])
            visited[row][col] = 0


    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    min_total = 100000

    recur(0, 0)
    print(f'#{tc} {min_total}')