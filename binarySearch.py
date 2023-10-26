#implementing binary search with hackerrank test cases
def binarySearch(arr, size, key):
    left = 0
    right = size-1
    comp = 0
    mid = math.floor((left+right)/2)
    while(left<=right):
        mid = math.floor((left+right)/2)
        comp+=1
        if(arr[mid] == key):
            break
        elif(arr[mid] < key):
            left = mid + 1
        elif(arr[mid] > key):
            right = mid - 1
        else:
            print("-1")
            exit(0)
    print(comp)
    print(mid)
#main
import math
size = int(input())
if(size == 0):
    print("-1")
else: 
    arr = list(map(int, input("").split()))
    key = int(input())
    binarySearch(arr, size, key)