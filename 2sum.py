arr = list(map(int,input("Enter the elements\n").split()))
req_sum = int(input("enter the required sum\n"))

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == req_sum:
            print(f"The elements are at {i}, {j} indexes\n")

