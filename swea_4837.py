# def dfs1(arr):
#     global total_cnt

#     for i in range(1<<len(arr)):
#         num_cnt = 0
#         num_sum = 0
        

#         for j in range(len(arr)):
#             if i & (1<<j):
#                 num_cnt += 1
#                 num_sum += arr[j]
        
#         if num_cnt == N and num_sum == M:
#             total_cnt += 1

#     return

# =============================================
def dfs2(start, bit, depth, sum_v):
    global total_cnt

    if depth == N:
        if sum_v == M:
            total_cnt += 1
        return
        
    for i in range(start, len(arr)):
        if bit & (1<<i):
            continue
        dfs2(i+1, bit | (1<<i), depth+1, sum_v + arr[i])


T = int(input())
for tc in range(1, T + 1):

    N, M = map(int, input().split())
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    total_cnt = 0

    # dfs1(arr)
    dfs2(0, 0, 0, 0)
    
    print(f'#{tc} {total_cnt}')