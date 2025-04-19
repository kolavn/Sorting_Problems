arr = list(map(int,input("Enter the elements\n").split()))
count = 0
new = []
for i in range(len(arr)):
    if arr[i] == 1:
        count+=1
    else:
        count = 0
    new.append(count)

    # if arr[i] != 1:
    #     count = 0

print(max(new))

     