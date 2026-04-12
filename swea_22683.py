# from collections import deque

# import sys
# sys.stdin = open('swea_22683_input.txt', 'r')     #open('@swea/swea_22683_input.txt', 'r')

# def bfs(st_y, st_x, arr, N):
#     q = deque()
#     q.append((st_y, st_x, arr))

#     arr[st_y][st_x] = 1

#     while q:
#         cy, cx, arr = q.popleft()

#         for dy, dx in [(0,1), (-1,0),(0,-1),(1,0)]:
#             ny = cy + dy
#             nx = cx + dx

#             if 0<=ny<N and 0<=nx<N:
#                 if arr[ny][nx] == 'Y':
#                     return cnt      # 위쪽에서 움직이는 cnt 함수를 선언하고 누적값을 추가해야겠음
                
#                 arr[ny][nx] = 1
#                 q.append((ny, nx, arr))
    
#     return cnt

# T = int(input())
# for tc in range(1, T+1):

#     N, C = map(int, input().split())
#     arr = [list(input()) for _ in range(N)]

#     for y in range(N):
#         for x in range(N):

#             if arr[y][x] == 'X':
#                 st_y = y
#                 st_x = x

#     result = bfs(st_y, st_x, arr, N)

#     print(f'#{tc} {result}')

# ===============================================================================================

from collections import deque

import sys
sys.stdin = open('swea_22683_input.txt', 'r')


def bfs(sy, sx, ey, ex, board, N, C):
    """
    시작점 X에서 도착점 Y까지 가는 최소 조작 횟수를 구하는 BFS 함수

    [매개변수]
    sy, sx : 시작점(X)의 행, 열 좌표
    ey, ex : 도착점(Y)의 행, 열 좌표
    board  : 전체 지도 정보 (2차원 리스트)
    N      : 지도 크기 (N x N)
    C      : 최대 벌목 가능 횟수

    [반환값]
    도착 가능하면 최소 조작 횟수
    도착 불가능하면 -1
    """

    # 방향 인덱스 약속
    # 0: 상, 1: 우, 2: 하, 3: 좌
    #
    # 예를 들어 현재 방향 d가 0이면 "위쪽"을 보고 있다는 뜻
    # 한 칸 전진 좌표는 (y + dy[d], x + dx[d]) 로 계산
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    # visited[y][x][dir][cut]
    #
    # 의미:
    # y, x 위치에
    # dir 방향을 보고 있고
    # cut번 나무를 벤 상태로
    # 이미 방문한 적이 있는지 저장
    #
    # 왜 4차원이 필요한가?
    # 같은 칸 (y, x)에 도착해도
    # 1) 바라보는 방향(dir)이 다르면 다음 행동 결과가 달라지고
    # 2) 지금까지 벤 나무 수(cut)가 다르면 이후 가능한 선택이 달라짐
    #
    # 그래서 단순 visited[y][x] 만으로는 부족함
    visited = [[[[False] * (C + 1) for _ in range(4)] for _ in range(N)] for _ in range(N)]

    # BFS 탐색에 사용할 큐
    q = deque()

    # 큐에 넣는 상태 형식:
    # (현재 y좌표, 현재 x좌표, 현재 방향, 지금까지 벤 나무 수, 지금까지 조작 횟수)
    #
    # 시작 상태:
    # 위치 = 시작점(X)
    # 방향 = 위쪽(0)
    # 벌목 횟수 = 0
    # 조작 횟수 = 0
    q.append((sy, sx, 0, 0, 0))

    # 시작 상태 방문 처리
    visited[sy][sx][0][0] = True

    # BFS 시작
    while q:
        # 현재 탐색할 상태를 큐에서 하나 꺼냄
        y, x, d, cut, cnt = q.popleft()

        # ---------------------------
        # 현재 상태의 각 변수 의미
        # y, x  : 현재 위치
        # d     : 현재 바라보는 방향
        # cut   : 지금까지 사용한 벌목 횟수
        # cnt   : 지금까지 사용한 조작 횟수
        # ---------------------------

        # 현재 위치가 도착점이면
        # BFS 특성상 처음 도달한 cnt가 최소 조작 횟수
        if y == ey and x == ex:
            return cnt

        # ==================================================
        # 1. 좌회전
        # ==================================================
        # 현재 방향 d에서 왼쪽으로 90도 회전한 새 방향
        # 예:
        # d = 0(상) -> nd = 3(좌)
        # d = 1(우) -> nd = 0(상)
        nd = (d - 1) % 4

        # 같은 위치, 같은 벌목 횟수에서
        # "왼쪽으로 회전한 방향" 상태를 아직 방문하지 않았다면
        if not visited[y][x][nd][cut]:
            visited[y][x][nd][cut] = True
            q.append((y, x, nd, cut, cnt + 1))
            # 회전도 조작 1번이므로 cnt + 1

        # ==================================================
        # 2. 우회전
        # ==================================================
        # 현재 방향 d에서 오른쪽으로 90도 회전한 새 방향
        nd = (d + 1) % 4

        # 아직 방문하지 않은 상태면 큐에 추가
        if not visited[y][x][nd][cut]:
            visited[y][x][nd][cut] = True
            q.append((y, x, nd, cut, cnt + 1))
            # 회전도 조작 1번이므로 cnt + 1

        # ==================================================
        # 3. 전진
        # ==================================================
        # 현재 바라보고 있는 방향 d로 한 칸 전진한 좌표 계산
        ny = y + dy[d]
        nx = x + dx[d]

        # 전진한 좌표가 지도 범위 안에 있을 때만 처리
        if 0 <= ny < N and 0 <= nx < N:

            # ----------------------------------------------
            # (1) 이동 가능한 칸인 경우
            # G : 일반 땅
            # X : 시작점
            # Y : 도착점
            # ----------------------------------------------
            if board[ny][nx] in ('G', 'X', 'Y'):

                # 같은 위치, 같은 방향, 같은 벌목 횟수 상태를
                # 아직 방문하지 않았다면 큐에 추가
                if not visited[ny][nx][d][cut]:
                    visited[ny][nx][d][cut] = True
                    q.append((ny, nx, d, cut, cnt + 1))
                    # 전진도 조작 1번이므로 cnt + 1

            # ----------------------------------------------
            # (2) 나무(T)인 경우
            # 아직 더 벨 수 있을 때만 이동 가능
            # ----------------------------------------------
            elif board[ny][nx] == 'T' and cut < C:

                # 나무를 하나 더 베고 들어가는 상태
                # 즉, cut + 1 상태로 이동
                if not visited[ny][nx][d][cut + 1]:
                    visited[ny][nx][d][cut + 1] = True
                    q.append((ny, nx, d, cut + 1, cnt + 1))
                    # 나무를 베고 전진하는 것도 조작 1번으로 처리

    # 큐가 빌 때까지 도착점을 만나지 못했으면 도달 불가능
    return -1


# 테스트케이스 개수 입력
T = int(input())

for tc in range(1, T + 1):
    # N : 지도 크기
    # C : 최대 벌목 가능 횟수
    N, C = map(int, input().split())

    # 지도 입력
    # 각 줄을 문자 리스트로 저장
    board = [list(input().strip()) for _ in range(N)]

    # 시작점(X), 도착점(Y)의 좌표를 저장할 변수
    # 처음에는 아직 못 찾았다는 뜻으로 -1로 초기화
    sy = sx = ey = ex = -1

    # 지도 전체를 돌면서 시작점 X와 도착점 Y 찾기
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'X':
                sy, sx = i, j
            elif board[i][j] == 'Y':
                ey, ex = i, j

    # BFS 실행
    result = bfs(sy, sx, ey, ex, board, N, C)

    # 결과 출력
    print(f'#{tc} {result}')