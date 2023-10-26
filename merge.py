#Given two arrays, write a program to merge those two arrays such that the resultant array has sorted elements.
#hackerrank implementation
def merge(left, right, arr):
    i = j = k = 0
    comp = 0
    while((i < len(left)) and (j < len(right))):
        if(left[i] <= right[j]):
            arr[k] = left[i]
            i+=1
            comp+=1
            k+=1
        else:
            arr[k] = right[j]
            j+=1
            comp+=1
            k+=1
    while(i < len(left)):
        arr[k] = left[i]
        i+=1
        k+=1
    while(j < len(right)):
        arr[k] = right[j]
        j+=1
        k+=1
    print(comp)
    for i in arr:
        print(i, end=' ')
#main
size1 = int(input("Enter size1: "))
if size1 != 0:
    arr1 = list(map(int, input("Enter arr1: ").split()))
else:
    arr1 = []
size2 = int(input("Enter size2: "))
if size2 != 0:
    arr2 = list(map(int, input("Enter arr2: ").split()))
else:
    arr2 = []

arr = arr1 + arr2
size = size1 + size2

if(size == 0):
    print("-1")
else:
    merge(arr1, arr2, arr)