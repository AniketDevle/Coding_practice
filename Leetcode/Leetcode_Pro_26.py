"""


the most important thing to notice is that we dont need to save the duplicates
ie we can override them

Algo :

1. set a counter where we are suppose to enter next value  
2. Set Length to total length
3. if current is equal to the previous value => we have one duplicate => subtract one from Length
4. If current not equal to the previous => place it at proper position using counter => increment counter


"""

nums = [0,0,1,1,1,2,2,3,3,4]

counter = 1
Length = len(nums)
for i in range(1,Length):
    if nums[i] == nums[i-1]:
        Length = Length-1
    else:
        nums[counter] = nums[i]
        counter = counter + 1

print(nums)
print(Length)
