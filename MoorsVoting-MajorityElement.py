arr = list(map(int,input("Enter the elements\n").split()))
count = 0
num = None

for i in range(len(arr)):
    if count == 0:
        count=1
        num = arr[i]
    elif num == arr[i]:
        count+=1
    else:
        count-=1
    
if arr.count(num) > (len(arr) // 2):  # very imp and new step
    print(num)



    
    