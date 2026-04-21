# 코드트리 등산로 문제
# --조건--

# 등산로는 가장 높은 봉우리에서 시작해야 합니다.
# 등산로는 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로만 연결되어야 합니다. 
# 즉, 다음 칸의 높이는 현재 칸의 높이보다 반드시 낮아야 하며, 대각선 방향의 이동은 불가능합니다.
# 긴 등산로를 만들기 위해 여러 칸의 지형을 깎는 공사를 할 수 있습니다. 이때 깎는 양의 총합이 K 이하여야 합니다. 
# 깎은 칸의 높이는 깎은 양만큼 줄어듭니다.
# 1 이상의 정수 칸 만큼만 깎을 수 있습니다.
# -지형을 깎아 높이를 1 미만으로 만들 수는 없습니다.
# -지형을 깎을 때, 가장 높은 봉우리는 깎을 수 없습니다. 가장 높은 봉우리가 여러 개인 경우, 모두 깎을 수 없습니다.
# -이때 만들 수 있는 가장 긴 등산로의 길이를 구합니다. 등산로의 길이는 등산로를 구성하는 칸의 수입니다.


N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

highest = -1
for i in range(N):
    highest = max(highest, max(grid[i]))

dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]

def in_range(y, x):
    return 0 <= y < N and 0 <= x < N

def get_movable_directions(y, x, grid, moved_cnt, remain, visited):
    movable = []
    for d in range(4):
        ny = y + dys[d]
        nx = x + dxs[d]
        
        # 0. Out of range
        if not in_range(ny, nx):
            continue

        # 1. all already visited
        if visited[ny][nx]:
            continue
        
        current_height = grid[y][x]
        next_height = grid[ny][nx]

        # 2. current_height is the lowest
        if grid[y][x] == 1:
            continue

        # 3. next_height is the highest
        if grid[ny][nx] == highest:
            continue
    
        if current_height > next_height:
            movable.append(d)
        elif (next_height - remain) < current_height:
            movable.append(d)
            
    return movable

def move(y, x, grid, moved_cnt, remain, visited):
    movable_directions = get_movable_directions(y, x, grid, moved_cnt, remain, visited)

    if len(movable_directions) == 0:
        return moved_cnt

    return_value = moved_cnt

    for d in movable_directions:
        ny = y + dys[d]
        nx = x + dxs[d]

        if not in_range(ny, nx):
            continue

        current_height = grid[y][x]
        next_height = grid[ny][nx]

        visited[ny][nx] = True
        if current_height > next_height:
            return_value = max(return_value, move(ny, nx, grid, moved_cnt + 1, remain, visited))
        else:
            cut = next_height - current_height + 1
            grid[ny][nx] = next_height - cut
            return_value = max(return_value, move(ny, nx, grid, moved_cnt + 1, remain - cut, visited))
            grid[ny][nx] = next_height

        visited[ny][nx] = False

    return return_value

res = -1

for y in range(N):
    for x in range(N):
        if grid[y][x] == highest:
            visited[y][x] = True
            res = max(res, move(y, x, grid, 1, K, visited))
            visited[y][x] = False

print(res)
