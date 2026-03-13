import sys
sys.stdin = open('swea_5203_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):

    arr = list(map(int, input().split()))

    p1 = []
    p2 = []
    winner = 0

    for i in range(len(arr)):
        if i % 2 == 0:
            if len(p1) < 3:
                p1.append(arr[i])
            elif len(p1) >= 3:
                p1.sort()
                p1.append(arr[i])

                for idx in range(len(p1)-2):
                    if p1[idx] == p1[idx + 1] == p1[idx + 2]:
                        winner = 1
                        break

                    elif p1[idx + 1] == p1[idx] + 1 and p1[idx+2] == p1[idx] + 2:
                        winner = 1
                        break


        else:
            if len(p2) < 3:
                p2.append(arr[i])
            elif len(p2) >= 3:
                p2.sort()
                p2.append(arr[i])

                for idx in range(len(p2)-2):
                    if p2[idx] == p2[idx + 1] == p2[idx + 2]:
                        winner = 2
                        break

                    elif p2[idx + 1] == p2[idx] + 1 and p2[idx+2] == p2[idx] + 2:
                        winner = 2
                        break

    print(winner)


