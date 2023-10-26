def ele_check(lst):
    for i in range(len(lst)):
        count = 0
        # print(i)
        for j in range(len(lst)):
            # print(lst[i], lst[j])
            if lst[i] == lst[j]:
                count+=1
                 # print(count)
        if count > 1:
            print(-1)
            exit()
    return count

#main
size = int(input(""))
if(size!=0):
    lst = list(map(int, input("").split()))
    count = 0
    count = ele_check(lst)
    # print(count)
    print(1)
else:
    print(0)