# Find the number that is not there from 1 to N
#lets say for size 5, if in arr there are 1, 2, 3, 5 - so missing is 4 - print 4

n = int(input("enter the size\n"))
nums = list(map(int,input("Enter the elements\n").split())) #nums should be n-1

for i in range(1, n+1):
    if i in nums:
        continue
    else:
        print("Number not present in nums is", i)

