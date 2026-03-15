# 1번
num = int(input())

n_bin = bin(num)
n_oct = oct(num)
n_hex = hex(num)

n_bin = n_bin[2:]
n_oct = n_oct[2:]
n_hex = n_hex[2:].upper()

print(n_bin, n_oct, n_hex)

# ===============================
# 2번

num2 = int(input(), 16)
print(num2)

# ===============================
# 3번

num3 = int(input(), 2)
num3_hex = hex(num3)
num3_hex = num3_hex[2:].upper()
print(num3, num3_hex)

# ===============================
# 4번

num4 = int(input())
print(f"{num4:08b}")

# ===============================
# 5번

num5 = int(input(), 16)
num5_bin = bin(num5)[2:]
print(num5_bin)

for i in num5_bin:
    print(f"{i:04b}", end='')

num5 = input()

for i in num5:
    print(f"{int(i, 16):04b}", end='')


# ===============================
# 6번

N, num6 = input().split()

N = int(N)

num6 = int(num6, 16)
print(f"{num6:0{N*4}b}")

# ===============================
# 7번

num7 = int(input())

num7_hex = hex(num7)
print(str(num7_hex)[2:].upper())

# ===============================
# 8번

num8 = int(input(), 2)

num8_oct = oct(num8)[2:]
num8_hex = str(hex(num8))[2:].upper()

print(num8, num8_oct, num8_hex)

