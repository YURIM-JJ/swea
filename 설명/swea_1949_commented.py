import sys
sys.stdin = open('input_1949.txt')


def recur(row, col, cut_cnt, path_len):
    global result

    # 현재 칸을 등산로 경로에 포함했다고 표시한다.
    # visited를 사용하는 이유는 같은 경로 안에서 같은 칸을 다시 방문하면
    # 순환이 생겨 잘못된 탐색이 되기 때문이다.
    visited[row][col] = True

    # 지금까지 만든 등산로 길이(path_len)로 정답을 갱신한다.
    result = max(result, path_len)

    # 현재 위치에서 상하좌우 네 방향으로 이동을 시도한다.
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        newr, newc = row + dr, col + dc

        # 1. 배열 범위를 벗어나지 않아야 하고
        # 2. 아직 현재 경로에서 방문하지 않은 칸이어야 한다.
        if 0 <= newr < N and 0 <= newc < N and not visited[newr][newc]:

            # 다음 칸의 높이가 현재 칸보다 낮다면
            # 규칙에 맞게 바로 이동할 수 있다.
            if arr[row][col] > arr[newr][newc]:
                recur(newr, newc, cut_cnt, path_len + 1)

            # 아직 한 번도 땅을 깎지 않았고(cut_cnt == 0),
            # 다음 칸을 최대 K만큼 깎았을 때 현재 칸보다 낮게 만들 수 있다면
            # 이번 기회에 그 칸을 깎고 이동한다.
            elif cut_cnt == 0 and arr[newr][newc] - K < arr[row][col]:

                # 원래 높이를 저장해둔 뒤,
                # "현재 칸보다 정확히 1 낮은 높이"로 만들어 이동한다.
                # 가장 높게 유지한 채 이동하는 것이 이후 탐색에 유리하다.
                temp = arr[newr][newc]
                arr[newr][newc] = arr[row][col] - 1

                # 깎기 기회를 사용했으므로 cut_cnt를 1로 바꿔 재귀 호출한다.
                recur(newr, newc, 1, path_len + 1)

                # 다른 경로 탐색에 영향을 주면 안 되므로
                # 재귀가 끝나면 원래 높이로 반드시 복구한다.
                arr[newr][newc] = temp

    # 현재 칸에서 출발하는 모든 경우를 다 탐색했으니
    # 백트래킹을 위해 방문 표시를 해제한다.
    visited[row][col] = False


T = int(input())
for tc in range(1, T + 1):
    # N: 지도 크기
    # K: 최대 깎을 수 있는 높이
    N, K = map(int, input().split())

    # 등산 지도의 높이 정보
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가장 높은 봉우리의 높이를 찾는다.
    # 문제 조건상 등산로는 가장 높은 봉우리에서 시작해야 한다.
    maxv = max(map(max, arr))

    # 만들 수 있는 가장 긴 등산로 길이
    result = 0

    # DFS 방문 체크 배열
    visited = [[False] * N for _ in range(N)]

    # 최고 높이 봉우리가 여러 개일 수 있으므로
    # 최고점인 모든 칸을 시작점으로 DFS를 수행한다.
    for row in range(N):
        for col in range(N):
            if arr[row][col] == maxv:

                # 시작점이므로
                # cut_cnt = 0 : 아직 안 깎음
                # path_len = 1 : 시작 칸 포함
                recur(row, col, 0, 1)

    # SWEA 형식에 맞춰 각 테스트케이스의 정답 출력
    print(result)
