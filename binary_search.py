#implementing binary search with time
import time
start = time.time()
import math

size = int(input("Enter size of list : "))
arr = []

for i in range(size):
    arr.append(i * 2)
    # print(i * 2)

key = int(input("Enter the key : "))
pos = -1
low = 0
high = size - 1

while (low <= high):
    mid = math.floor((low + high) / 2)
    if(arr[mid] == key):
        pos = mid
        break
    elif(arr[mid] < key):
        low = mid + 1
    elif(arr[mid] > key):
        high = mid - 1

if(pos == -1):
    print("Element not in list")
    print("%s seconds" % (time.time() - start))
else:
    print("Element found at position {}".format(pos + 1))
    print("%s seconds" % (time.time() - start))