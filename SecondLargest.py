nums = list(map(int,input("Enter the elements\n").split()))
largest = nums[0]
for i in range(1,len(nums)):
    if nums[i] > largest:
        largest = nums[i]
    for i in range(len(nums)-2
        second_largest = nums[i-1]
print("Largest Number is:",largest)
print("Second Largest is:", second_largest)
    


# nums = list(map(int, input("Enter the elements:\n").split()))

# # Ensure the list has at least two unique elements
# unique_nums = list(set(nums))  # Remove duplicates
# if len(unique_nums) < 2:
#     print("No second largest number found (all elements might be the same).")
# else:
#     unique_nums.sort(reverse=True)  # Sort in descending order
#     print("Largest Number is:", unique_nums[0])
#     print("Second Largest is:", unique_nums[1])