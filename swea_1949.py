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

# ==========================================================================

# row, col   : 현재 내 위치
# cut_cnt    : 공사를 이미 했는지 여부
#              0 = 아직 안함
#              1 = 이미 한번 사용함
# path_len   : 현재까지 만든 등산로 길이
def recur(row, col, cut_cnt, path_len):
    global result

    # 현재 위치 방문 처리
    visited[row][col] = True

    # 지금까지 만든 길이와 최대 길이 비교해서 갱신
    result = max(result, path_len)

    # 상하좌우 4방향 탐색
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

        # 다음 위치 좌표
        newr = row + dr
        newc = col + dc

        # 범위 안에 있고, 아직 방문 안한 곳이면 진행
        if 0 <= newr < N and 0 <= newc < N and not visited[newr][newc]:

            # -------------------------------------------------
            # 1. 다음 칸이 더 낮으면 그냥 이동 가능
            # 현재 높이 > 다음 높이
            # -------------------------------------------------
            if arr[row][col] > arr[newr][newc]:

                recur(newr, newc, cut_cnt, path_len + 1)

            # -------------------------------------------------
            # 2. 다음 칸이 낮지 않다면 공사 가능한지 확인
            #
            # cut_cnt == 0
            #   -> 아직 공사를 안 썼을 때만 가능
            #
            # arr[newr][newc] - K < arr[row][col]
            #   -> 최대 K만큼 깎았을 때
            #      현재 칸보다 낮아질 수 있으면 가능
            # -------------------------------------------------
            elif cut_cnt == 0 and arr[newr][newc] - K < arr[row][col]:

                # 원래 높이 저장
                temp = arr[newr][newc]

                # 딱 이동 가능할 만큼만 깎기
                # 현재 높이보다 1 낮게 만들기
                arr[newr][newc] = arr[row][col] - 1

                # 공사 사용했다고 표시하고 이동
                recur(newr, newc, 1, path_len + 1)

                # 탐색 끝났으면 원래 높이 복구
                # (백트래킹 핵심)
                arr[newr][newc] = temp

    # 현재 위치 탐색 끝났으니 방문 해제
    # 다른 시작점/다른 경로에서 다시 올 수 있게 풀어줌
    visited[row][col] = False


# 테스트케이스 개수
T = int(input())

for tc in range(1, T + 1):

    # N = 지도 크기
    # K = 최대 공사 깊이
    N, K = map(int, input().split())

    # 지도 입력
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가장 높은 봉우리 찾기
    maxv = max(map(max, arr))

    # 정답(가장 긴 등산로 길이)
    result = 0

    # 방문 체크 배열
    visited = [[False] * N for _ in range(N)]

    # 가장 높은 위치들은 모두 시작점 후보
    for row in range(N):
        for col in range(N):

            # 최고 높이인 곳에서 DFS 시작
            if arr[row][col] == maxv:
                recur(row, col, 0, 1)
                # 시작점이므로 길이 1부터 시작
                # 공사 아직 안씀 -> 0

    print(result)