# T = int(input())
# for tc in range(1, T+1):

arr = list(input())
stack = []
for i in range(1, len(arr)):
    
    if arr[i-1] == arr[i]:
        stack.append(arr[i])
    elif arr[i-1] != arr[i]:
        stack.pop() 

print(stack)