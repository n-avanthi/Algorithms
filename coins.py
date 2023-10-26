size = int(input("Enter number of coins : "))
values = list(map(int, input("Enter values of coins: ").split()))
total = int(input("Enter the total value : "))
max = total + 1
def calcMin(pending, values):
    if pending == 0:
        # print("pending is: ", pending)
        return 0
    if pending < 0:
        # print("pending is: ", pending)
        return max
    min_count = max
    # print("pending is: ", pending)
    for i in range(len(values)):
        count = 1+ calcMin(pending - values[i], values)
        min_count = min(min_count, count)
        # print("min count is: ", min_count)
    return min_count

#main
min_count = calcMin(total, values)
if(min_count != max):
    print("Min number of coins required are:", min_count)