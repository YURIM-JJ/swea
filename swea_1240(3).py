import sys
sys.stdin = open("input_1240.txt", "r")

T = int(input())
# 1. 테스트 케이스 반복 범위 수정 (1부터 T까지)
for tc in range(1, T + 1):

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

    # 2. 뒤집혀서 들어간 암호 조각들의 순서를 원본(왼쪽->오른쪽)으로 복구
    pw_list = pw_list[::-1]

    pw_dict = {
        '0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4,
        '0110001' : 5, '0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9
    }

    # 기존의 final_pw = [0]은 인덱스를 밀리게 하므로 빈 배열로 수정
    final_pw = []

    for key in pw_list:
        num = pw_dict[key]
        final_pw.append(num)

    num_2 = 0
    num_3 = 0

    for i in range(len(final_pw)):
        # 인덱스 0, 2, 4, 6은 실제 홀수 자리(1, 3, 5, 7번째)를 의미함
        if i % 2 == 0:
            num_3 += final_pw[i] # 홀수 자리의 합
        # 인덱스 1, 3, 5, 7은 실제 짝수 자리(2, 4, 6, 8번째)를 의미함
        else:
            num_2 += final_pw[i] # 짝수 자리의 합

    # 3. 들여쓰기 수정 (for문 밖으로 빼냄)
    # 4. 공식 수정: (홀수 자리 합 * 3) + 짝수 자리 합
    final_pw_num = (num_3 * 3) + num_2
    final_num = 0

    if final_pw_num % 10 == 0:
        for i in range(len(final_pw)):
            final_num += final_pw[i]
        print(f'#{tc} {final_num}')
    else:
        print(f'#{tc} 0')