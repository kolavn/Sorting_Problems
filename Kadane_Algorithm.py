# for maximum subarray sum, need only +ve sum


arr = list(map(int,input("Enter the elements\n").split()))
sum = 0
maxi = float('-inf') # Assiging integer minimum value

for i in range(len(arr)):
    sum = sum + arr[i]
    if sum>maxi:
        maxi = sum
    if sum<0:
        sum = 0
    if maxi < 0:
        maxi = 0
print(maxi)





