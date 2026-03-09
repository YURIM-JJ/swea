# T = int(input())
for tc in range(1, 11):

    N = int(input())
    b_lst = list(map(int, input().split()))

    total_sum = 0

    for n in range(2, N-2):
        max_around = 0
        for m in range(n-2, n+3):
            if m == n:
                continue
            elif max_around < b_lst[m]:
                max_around = b_lst[m]

        if b_lst[n] > max_around:
            current_view = b_lst[n] - max_around
            total_sum += current_view

    print(f'#{tc} {total_sum}')
