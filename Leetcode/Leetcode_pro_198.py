class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0] , nums[1])
        elif len(nums) == 3:
            return max(nums[0]+nums[2] , nums[1])
        else:
            arr = [nums[0] , nums[1] , nums[0]+nums[2]]
            for i in range(3,len(nums)):
                val = max(arr[i-2] , arr[i-3])
                arr.append(val + nums[i])
            return max(arr)    
            
