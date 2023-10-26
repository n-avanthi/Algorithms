import time
start = time.time()

# size = int(input("Enter the size of list : "))
size = 10
list = []

for i in range(size):
    list.append(i*2)
    # print(i*2)

# key = int(input("Enter the key : "))
key = 4
pos = -1

for j in range(size):
    if(list[j] == key):
        pos = j
        break

if(pos == -1):
    print("Element not in list")
    print("%s seconds" % (time.time() - start))
else:
    print("Element found at position {}".format(pos + 1))
    print("--- %s milliseconds---" % (time.time() - start))