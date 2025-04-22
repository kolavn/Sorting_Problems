arr = list(map(int,input("Enter elements:\n").split()))
k = int(input("Enter required Sum\n"))
count = 0
for i in range(len(arr)):
    sum  = 0
    for j in range(i, len(arr)):
        sum = sum+arr[j]
        if sum == k:
            count+= 1
print(f"No. of Sub arrays having sum {k} is", count)
