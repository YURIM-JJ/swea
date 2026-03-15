# import sys
# sys.stdin = open('@swea/swea_5185_input.txt', 'r')

# T = int(input())
# for tc in range(1, T+1):

#     N, arr = input().split()

#     N = int(N)
    
#     arr = int(arr, 16)
#     print(f'#{tc}', f"{arr:0{N*4}b}")


'''
#1 0100011111111110
#2 01111001111000010010
#3 01000001110110100001011011001101
'''

s = int(input(), 2)
oct_s = oct(s)
hex_s = hex(s)
hex_s = hex_s.upper()
print(s, oct_s, hex_s)
# change = {'a':'A', 'b':'B', 'c':'C', 'd':'D', 'e':'E', 'f':'F'}
hex_s = hex_s[2:]
# if s>=10:
    # hex_s = change[hex_s]
hex_s = hex_s.upper()
print(s, oct_s, hex_s)
