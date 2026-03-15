#십진수를 입력받아 2진수, 8진수, 16진수로 변환하기
s = int(input())
bin_s = bin(s)
oct_s = oct(s)
hex_s = hex(s)
print(bin_s, oct_s, hex_s)

#16진수를 입력받아 10진수, 2진수, 8진수로 변환하기
s = int(input(), 16)
bin_s = bin(s)
oct_s = oct(s)
print(s, bin_s, oct_s)
print(s, bin_s[2:], oct_s[2:])

#2진수를 입력받아 10진수, 8진수, 16진수로 변환하기
s = int(input(), 2)
oct_s = oct(s)
hex_s = hex(s)
print(s, oct_s, hex_s)
change = {'a':'A', 'b':'B', 'c':'C', 'd':'D', 'e':'E', 'f':'F'}
hex_s = hex_s[2:]
if s>=10:
    # hex_s = change[hex_s]
    hex_s = hex_s.upper()
print(s, oct_s, hex_s)



# ===============================================

'''
1. 2진수 -> 10진수, 16진수 바꾸기
2진수 문자열을 먼저 int() 함수를 써서 10진수로 바꾼 뒤, 원하는 형태로 가공합니다.
2진수 -> 10진수: int(문자열, 2)
2진수 -> 16진수: 10진수로 바꾼 후 hex() 또는 f-string 사용
'''
bin_str = '1010'

# 1. 2진수 -> 10진수 (정수)
dec_num = int(bin_str, 2)  
print(dec_num)             # 출력: 10

# 2. 2진수 -> 16진수 (문자열)
# 10진수로 변환한 dec_num을 다시 16진수로 변환
hex_str1 = hex(dec_num)       # 출력: '0xa' (접두사 포함)
hex_str2 = f"{dec_num:x}"     # 출력: 'a' (접두사 제외, 소문자)
hex_str3 = f"{dec_num:X}"     # 출력: 'A' (접두사 제외, 대문자)

'''
2. 10진수 -> 2진수, 16진수 바꾸기
10진수는 이미 정수형(int)이므로, 바로 변환 함수나 f-string을 적용하면 됩니다.
10진수 -> 2진수: bin() 또는 f-string b
10진수 -> 16진수: hex() 또는 f-string x, X
'''
num = 10

# 1. 10진수 -> 2진수 (문자열)
bin_str1 = bin(num)        # 출력: '0b1010' (접두사 포함)
bin_str2 = f"{num:b}"      # 출력: '1010' (접두사 제외)

# 2. 10진수 -> 16진수 (문자열)
hex_str1 = hex(num)        # 출력: '0xa' (접두사 포함)
hex_str2 = f"{num:x}"      # 출력: 'a' (접두사 제외, 소문자)
hex_str3 = f"{num:X}"      # 출력: 'A' (접두사 제외, 대문자)

'''
3. 16진수 -> 2진수, 10진수 바꾸기
앞서 본 문제와 같은 케이스입니다. 16진수 문자열을 int()로 10진수로 먼저 바꿉니다.
16진수 -> 10진수: int(문자열, 16)
16진수 -> 2진수: 10진수로 바꾼 후 bin() 또는 f-string 사용
'''
hex_str = 'A'

# 1. 16진수 -> 10진수 (정수)
dec_num = int(hex_str, 16)  
print(dec_num)              # 출력: 10

# 2. 16진수 -> 2진수 (문자열)
# 10진수로 변환한 dec_num을 다시 2진수로 변환
bin_str1 = bin(dec_num)         # 출력: '0b1010'
bin_str2 = f"{dec_num:b}"       # 출력: '1010'
bin_str3 = f"{dec_num:04b}"     # 출력: '1010' (4자리 맞춤, 앞자리 0 채움)
