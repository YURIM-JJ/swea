import sys
sys.stdin = open("input_1240.txt", "r")

T = int(input())
for tc in range(T, T+1) :

    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    temp = []
    for i in range(N):
        if '1' in arr[i]:
            temp = arr[i][::-1]
            idx = temp.index('1')
            break

    temp_2 = temp[int(idx):int(idx)+56]

    pw_list = []

    for i in range(0, 56, 7):
        pw = temp_2[i: i + 7]
        pw_list.append("".join(pw[::-1]))

    pw_dict = {
        '0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4,
        '0110001' : 5, '0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9
    }

    final_pw = [0]

    for key in pw_list:
        num = pw_dict[key]
        final_pw.append(num)


    num_2 = 0
    num_3 = 0

    for i in range(len(final_pw)):
        if i % 2 != 0:
            num_2 += final_pw[i]
        else:
            num_3 += final_pw[i]

    final_pw_num = (num_3*3)+num_2
    final_num = 0

    if final_pw_num % 10 == 0:
        for i in range(len(final_pw)):
            final_num += final_pw[i]
        print(f'#{tc} {final_num}')
    else:
        print(f'#{tc} 0')