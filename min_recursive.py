def min_ele(lst, min, pos, i):
    if(i < len(lst)):
        if(lst[i]<min):
            min = lst[i]
            pos = i
        i = i+1
        min_ele(lst, min, pos, i)
    else:
        print(pos)
        print(min)
    
size = int(input("Enter size : "))
if (size == 0):
    print("-1")
else:
    lst = list(map(int, input("Enter array : ").split()))
    min = lst[0]
    pos = 0
    i = 0
    min_ele(lst, min, pos, i)