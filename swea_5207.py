T = int(input())
for tc in range(1, T+1):
    
    cnt = 0

    def binary_search_while(target):
        global cnt

        left = 0
        right = len(arr) - 1
        dir = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                cnt += 1
                return
            else:
                if arr[mid] > target:
                    if dir == 1:
                        return
                    dir = 1
                    right = mid -1
                else:
                    if dir == 2:
                        return
                    dir = 2
                    left = mid + 1
        return

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    targets = list(map(int, input().split()))

    for target in targets:
        result = binary_search_while(target)
    

    print(f'#{tc} {cnt}')