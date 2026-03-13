import sys
sys.stdin = open("swea_5189_input.txt", "r")

# 1번 사무실
# 2번 관리구역 
# 1-2-3-4-1
# 1-2-4-3-1
# 1-3-2-4-1 등등등

# 일단 순열을 구하고 생각을 해보자 ~~

# 지금 이렇게 되어있는건 가로로 N 개 깊이는 K개
# 5개 중에 3개 뽑을꺼야 ~ 이런 의미의 코드
# def permu(k):
#     if k==K:
#         print(result)
#         return
#
#     for i in range(N):
#         result[k] = i
#         permu(k+1)
#
# N = 5
# k = 3
# result = [-1] * N
# 가로로 방문표시를 하는거니까 N개가 들어가야한다.
# 즉 5개 중 3개 선택이니까 어디에 방문할 줄 모르고
# 또 3개가 꽉 차서 나머지를 선택을 안하기 때문에 5개로 방문표시를 해야함
# visited = [False] * N
# permu(0)

# ================================================================
# def permu(k):
#     if k == K:
#         # print(result)
#         for i in result(1,N):
#         #     정리하기
#         return
#
#     for i in range(N):
#         if visited[i]:
#             continue
#
#         result[k] = i
#         visited[i] = True
#         permu(k + 1)
#         visited[i] = False
#
# N = 3
# K = 3
# result = [-1] * K
# visited = [False] * N
#
# # 문제에서 첫번째는 고정이니까 0으로 고정하고 아래쪽은 1번부터 하자
# result[0] = 0
# # 0은 고정이니까 무조건 확인 안해도 되는걸로 하자
# visited[0] = True
# permu(1)

# ================================================================
# 문풀문풀풀
def permu(k, s):
    global min_v

    # for i in result[1:N]:
    #     s += arr[i-1][i]
    # if s >= min_v:
    #     return

    if k == N:
        total = s + arr[result[N - 1]][0]
        if min_v > total:
            min_v = total
        return


    for i in range(N):
        if visited[i]:
            continue

        result[k] = i
        visited[i] = True
        permu(k + 1, s + arr[result[k-1]][i])
        visited[i] = False

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = [-1] * N
    visited = [False] * N
    min_v = 987654321

    # 문제에서 첫번째는 고정이니까 0으로 고정하고 아래쪽은 1번부터 하자
    result[0] = 0
    # 0은 고정이니까 무조건 확인 안해도 되는걸로 하자
    visited[0] = True
    permu(1, 0)

    print(f'#{tc} {min_v}')
