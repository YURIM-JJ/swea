# 깊이 우선, 너비 우선 둘 다 가능함

def dfs(str, stc, no):
    STACK = []
    STACK.append((str, stc))
    arr[str][stc] = no
    #push 하면서 방문표시
    while STACK:
        row, col = STACK.pop()
        for dr, dc in ([1,0],[-1,0], [0,1], [0,-1])
            newr = rowd + dr
            newc = col + dc

            if 0<=newr<=
N = int(input())
arr = [list(input()) for _ in range(N)]

no = 0
for row in range(N):
    for col in range(N)L:
        if arr[row][col] == '1':
            no += 1
            dfs(row, col, no)

# ========================================================

def dfs(str, stc, no):
    STACK = []
    STACK.append((str, stc))
    arr[str][stc] = no # push 하면서 방문표시
    cnt = 0

    while STACK:
        row, col = STACK.pop()
        cnt += 1
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            newr = row+dr
            newc = col+dc

            if 0<=newr<N and 0<=newc<N and arr[newr][newc]=='1':
                arr[newr][newc] = no
                STACK.append((newr, newc))

    # print(arr)
    # pass
    return cnt


N = int(input())
arr = [list(input()) for _ in range(N)]
# print(arr)
no = 0
result = []
for row in range(N):
    for col in range(N):
        if arr[row][col] == '1':
            no += 1
            cnt = dfs(row, col, no)
            result.append(cnt)
print(len(result))
print(result)