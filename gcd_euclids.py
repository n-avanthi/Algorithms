import time
start = time.time()

num1 = int(input("Enter the bigger number : "))
num2 = int(input("Enter the smaller number : "))

while(num2!=0):
    rem = num1 % num2
    num1 = num2
    num2 = rem

print("GCD is given by : ", num1)
print("%s seconds" % (time.time() - start))