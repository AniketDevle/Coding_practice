"""
Algo:

iterate over the array :
  if current value is 0 then append the index of current  value in queue
  if the current value is non zero:
      1. If the queue is empty then there is no zero that occured before that index so we dont need to make any changes
      2. If the queue is not empty that mean there were zeroes that occured before
          1. Pop the first element of the queue (The first element of queue will point to the first occurance of zero)
          2. Swap the current value to the value of poped index from queue
          3. Add current index to the queue ( cause once we swap both values the current index will be 0)
          
example : arr = [0 , 1 , 0 , 3 , 12 , 0]

iterating over the range (6):

iteration 0 : arr [0] == 0   => add to q ,    arr = [0 , 1 , 0 , 3 , 12 , 0] , queue after itr 0 : q = [0]
iteration 1 : arr [1] == 1   => pop 0 ,       arr = [1 , 0 , 0 , 3 , 12 , 0] , queue after itr 1 : q = [1] 
iteration 2 : arr [2] == 0   => add to q ,    arr = [1 , 0 , 0 , 3 , 12 , 0] , queue after itr 2 : q = [1,2]
iteration 3 : arr [3] == 3   => pop 1 ,       arr = [1 , 3 , 0 , 0 , 12 , 0] , queue after itr 3 : q = [2,3]
iteration 4 : arr [4] == 12  => pop 2 ,       arr = [1 , 3 , 12 , 0 , 0 , 0] , queue after itr 4 : q = [3,4]
iteration 5 : arr [5] == 0   => add to q ,    arr = [1 , 3 , 12 , 0 , 0 , 0] , queue after itr 5 : q = [3,4,5]

"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        q  = []
        for i in range (len(nums)):
            if nums[i] == 0:
                q.append(i)
            elif (nums[i] != 0 and len(q) != 0):
                index = q.pop(0)
                nums[index] , nums[i] = nums[i] , 0
                q.append(i)
        
        return nums
