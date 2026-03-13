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
