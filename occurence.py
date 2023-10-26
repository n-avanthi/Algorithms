lst = eval(input("Enter elements of list : "))

def count(lst):
    count_lst = {}
    for ele in lst:
        if ele not in count_lst:
            count_lst[ele] = 0
        count_lst[ele] += 1
    return count_lst

count_lst = count(lst)
print(count_lst)