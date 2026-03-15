import sys
sys.stdin = open("@swea/swea_1244_input.txt", "r")


# def change(k, numbers):
#     if k==cnt:
#         print(numbers)
#         return
#
#     for i in range(N-1):
#         for j in range(i+1, N):
#             numbers[i], numbers[j] = numbers[j], numbers[i]
#             change(k+1, numbers)
#             numbers[i], numbers[j] = numbers[j], numbers[i]
# #
# N = 5
# cnt = 2
# numbers = ['3', '2', '8', '8', '8']
#
# visited = [[] for _ in range(cnt)]
# change(0, numbers)
# # value = int(''.join(numbers))


# =========================================================
#
# def change(k, numbers):
#     if k==cnt:
#         print(visited)
#         return
#
#     for i in range(N-1):
#         for j in range(i+1, N):
#             numbers[i], numbers[j] = numbers[j], numbers[i]
#
#             if numbers[k]:
#             # visited[0].append(k)
#             # visited[1].append(numbers)
#             change(k+1, numbers)
#             numbers[i], numbers[j] = numbers[j], numbers[i]

# =========================================================
#
# '''
# 2
# 123 1
# 2737 1
# '''

def change(k, numbers):
    global max_value

    if k==cnt:
        value = int(''.join(numbers))
        if max_value < value:
            max_value = value
        return

    for i in range(N-1):
        for j in range(i+1, N):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            value = int(''.join(numbers))

            if value not in visited[k]:
                visited[0].append(k)
                visited[1].append(numbers)
            change(k+1, numbers)
            numbers[i], numbers[j] = numbers[j], numbers[i]


T = int(input())
for tc in range(1, T + 1):

    numbers, cnt = input().split()
    cnt = int(cnt)
    numbers = list(numbers)
    N = len(numbers)
    max_value = 0

    # print(numbers)

    visited = [[] for _ in range(cnt)]
    change(0, numbers)
    # value = int(''.join(numbers))
    print(f'#{tc} {max_value}')