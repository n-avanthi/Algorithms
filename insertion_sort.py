#hackerrank implementation
def insertionSort(num,arr):
    swap = 0
    comp = 0
    for i in range(1,num):
        j = i-1
        temp = arr[i]
        comp+=1
        while(j >= 0 and arr[j] > temp):
            if j == 0:
                comp-=1
            comp+=1
            arr[j+1] = arr[j]
            swap+=1
            j-=1
        arr[j+1] = temp
    print(comp)
    print(swap)
    for i in arr:
        print(i, end=' ')
num = int(input("Enter the size: "))
if num==1:
    arr = list(map(int, input("").split()))
    print("0")
    print("0")
    print(arr[0])
elif num==0:
    print("-1")
else:
    arr = list(map(int, input("").split()))
    insertionSort(num, arr)