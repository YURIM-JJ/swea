from collections import deque

def bfs(str, stc):

    visited = [[0]*M for _ in range(N)]
    Q = deque((str,stc))
    Q.append((str,stc))
    visited[str][stc] = 1

    while Q:
        row, col = Q.popleft()

        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            newr = row + dr
            newc = col + dc
            if 0<=newr<N and 0<=newc<M:
                if arr[newr][newc] == 'L' and visited[row][col]==0:
                    visited[newr][newc] = visited[row][col]
                    Q.append((newr, newc))
                    maxv = max(maxv, visited[newr][newc])

    return maxv


N, M = map(int, input().split())
arr = [input() for_in range(N)]

result = 0
for row in range(N):
    for col in range(M):
        if arr[row][col] =='L':
            result