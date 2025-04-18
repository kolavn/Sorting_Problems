# Here we need to find the longest sub array of having sum 'K'

# Definitely the length of the sub array will be less than or equal to sum value

arr = list(map(int,input("Enter the elements\n").split()))
given_sum = int(input("Enter the sum you require:\n"))
length_of_subarr = 0 # lenght of longest subarray

for i in range(len(arr)):
    sum = 0
    for j in range(i, len(arr)):
        sum = sum + arr[j]
        
        if sum==given_sum:
            length_of_subarr = max(length_of_subarr, j-i+1)
            
print(f"Length of longest subarray having sum {given_sum} is", length_of_subarr)

