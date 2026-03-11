T = int(input())
for tc in range(1, T+1):

    def partition(arr, s, e):
        p = s
        l = s
        r = e

        while l <= r:
            while l <= r and arr[l] <= arr[p]:
                l += 1
            while l <= r and arr[r] >= arr[p]:
                r -= 1

            if l < r :
                arr[l], arr[r] = arr[r], arr[l]

        arr[r], arr[p] = arr[p], arr[r]
        return r

    def quick_sort(arr, s, e):
        if s < e:
            p = partition(arr, s, e)
            quick_sort(arr, s, p-1)
            quick_sort(arr, p+1, e)

    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, N-1)
    num = N // 2
    print(f'#{tc} {arr[num]}')
