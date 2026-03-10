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
#
# N = 5
# cnt = 2
# numbers = ['3', '2', '8', '8', '8']
#
# visited = [[] for _ in range(cnt)]
# change(0, numbers)
# # value = int(''.join(numbers))


# =========================================================

def change(k, numbers):
    if k==cnt:
        print(visited)
        return

    for i in range(N-1):
        for j in range(i+1, N):
            numbers[i], numbers[j] = numbers[j], numbers[i]

            if numbers
            # visited[0].append(k)
            # visited[1].append(numbers)
            change(k+1, numbers)
            numbers[i], numbers[j] = numbers[j], numbers[i]

N = 5
cnt = 2
numbers = ['3', '2', '8', '8', '8']
max_value=[]

visited = [[] for _ in range(cnt)]
change(0, numbers)
# value = int(''.join(numbers))
# print(value)