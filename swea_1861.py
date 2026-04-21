import sys
sys.stdin = open('swea_1861_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    answer = 999999
    for y in range(N):
        for x in range(N):

            start = arr[y][x]
            cnt = 1

            cy, cx = y, x

            while True:
                moved = False

                for dy, dx in [(0,1), (-1,0), (0,-1), (1,0)]:
                    ny = cy + dy
                    nx = cx + dx

                    if 0<=ny<N and 0<=nx<N and arr[cy][cx]+1 == arr[ny][nx]:
                        cnt += 1
                        cy, cx = ny, nx
                        moved = True
                        break

                if moved == False:
                    break


            if max_cnt < cnt:
                max_cnt = cnt
                answer = start

            elif cnt == max_cnt:
                if answer > start:
                    answer = start
        

    print(f'#{tc} {answer} {max_cnt}')