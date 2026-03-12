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


# 📌 SWEA 5209 (최소 생산 비용) 백트래킹 회고록
# 1. 내가 몰랐던 부분 (개념적 공백)
# 재귀 함수와 반복문의 역할 분리: 백트래킹에서 깊이(Depth)를 파고드는 역할은 while문이 아니라
#                            **'재귀 호출 그 자체'**가 수행한다는 점을 초반에 인지하지 못했습니다.
#                            recur(row + 1)을 호출하는 행위 자체가 다음 단계로 넘어가는 것이므로,
#                            재귀 함수 내부에서 별도의 while 루프로 깊이를 조절할 필요가 없었습니다.
#
# 매개변수를 활용한 상태 복구 생략: 전역 변수 total_sum을 사용할 때는 재귀 전후로 += 와 -= 를 통해 직접 상태를 복구해야 합니다.
#                              하지만 recur(row + 1, total_sum + arr[row][col])처럼 함수 호출의 인자로 값을 넘기면,
#                              해당 단계의 스택 프레임에만 값이 적용되므로 돌아왔을 때
#                              별도의 -= 상태 복구 과정이 필요 없다는 사실을 알게 되었습니다.
#
# 2. 내가 헷갈렸던 부분 (논리적 혼동)
# 가지치기(Pruning)와 종료 조건의 적용 시점: * 가지치기 - 탐색 중간에 total_sum >= min_total 일 경우
#                                         가망이 없으므로 return 하여 가지를 쳐냅니다. (함수 최상단 배치)
#
# 최솟값 갱신: 탐색 중간이 아니라, 반드시 모든 제품을 다 고른 **종료 조건(row == N)**에 도달했을 때만
#            min_total = total_sum으로 갱신해야 합니다. 이 두 가지 타이밍을 혼동하여 조기에 최솟값이 0으로 덮어씌워지는 문제가 있었습니다.
#
# N-Queen 문제와의 유사성 (순열): 이 문제가 본질적으로 행과 열이 겹치지 않게 N개를 뽑는 순열 문제이자
#                              N-Queen의 변형이라는 점을 파악하는 데 시간이 걸렸습니다.
#
# 3. 계속 틀렸던 부분 (코드 구현 오류)
# 2차원 배열 인덱싱 방향 (행 vs 열): check 함수 구현 시, 가장 오랫동안 막혀있던 부분입니다.
#
# 오답: visited[row][i]를 검사했습니다. 이는 '현재 제품(row)이 이전 공장(i)들을 썼는가?'를 수평으로 묻는 것으로, 로직상 맞지 않았습니다.
#
# 정답: visited[i][col]을 검사해야 했습니다. 이는 '내가 고르려는 공장(col)을 이전 제품(i)들이 수직으로 썼는가?'를 묻는 정확한 방향이었습니다.