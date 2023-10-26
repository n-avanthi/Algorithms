size = int(input("Enter size : "))

def min_ele(lst):
    min = lst[0]
    pos = 0
    for i in range(len(lst)):
        if(lst[i] < min):
            min = lst[i]
            pos = i
    print(pos)
    print(min)

if (size == 0):
    print("-1")
else:
    lst = list(map(int, input("Enter array : ").split()))
    min_ele(lst)