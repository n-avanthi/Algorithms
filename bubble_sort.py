size = int(input("Enter size : "))
lst = list(map(int, input("Enter unsorted array : ").split()))

def bubble_sort(lst):
    compare = 0
    swap = 0
    for i in range(len(lst)):
        for j in range(0, len(lst)-i-1):
            compare += 1
            # print("compare : ", compare)
            if(lst[j] > lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swap += 1
                # print("swap : ", swap)
    print("Number of comparisons are: ", compare)
    print("Number of swappings are : ", swap)
    print("Sorted array : ")
    for k in range(len(lst)):
        print(lst[k], end = ' ')

#main
if(size == 0):
    print("-1")
    print("-1")
    print("-1")
else:
    bubble_sort(lst)
