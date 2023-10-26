def partition(arr, size, pivot_index):
    low = 0
    high = size - 1
    swap = 0
    i = low - 1
    for j in range(low, high):
        if(arr[j] <= arr[pivot_index]):
            i+=1
            if(arr[j] != arr[i]):
                swap+=1
                arr[j], arr[i] = arr[i], arr[j]
    arr[pivot_index], arr[i+1] = arr[i+1], arr[pivot_index]
    swap+=1
    print(swap)
    print(' '.join(map(str, arr)))
    print(i+1)

#main
size = int(input())
if(size == 0):
    print("-1")
else:
    arr = list(map(int, input("").split()))
    pivot_index = int(input())
    partition(arr, size, pivot_index)