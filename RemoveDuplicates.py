# To find no. of unique elements in a list/array
nums = sorted(list(map(int,input("Enter the elements\n").split())))
count = 0
i =0
while i<(len(nums)-1):
    if nums[i] == nums[i+1]:
        nums.pop(i)
        count+=1
    else:
        i+=1
print(nums, count)
