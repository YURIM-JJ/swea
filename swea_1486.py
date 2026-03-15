# import sys
# sys.stdin = open('swea_1486_input.txt', 'r')

import sys
sys.stdin = open('@swea/swea_1486_input.txt', 'r')

def recur(depth, top_sum):
    global min_top

    if top_sum >= B: 
        if min_top > top_sum:
            min_top = top_sum
        return

    if depth == N:
        return
    
    recur(depth+1, top_sum + arr[depth])
    recur(depth+1, top_sum)


T = int(input())
for tc in range(1, T+1):

    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    min_top = 987654321

    recur(0,0)

    print(f'#{tc} {min_top-B}')
