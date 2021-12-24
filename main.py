class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = nums.copy()
        
        for i in range(0, len(nums)):
            # print (i)
            needed = target - nums[i]
            num1 = nums[i]
            temp.pop(0)
            if needed in temp and ((needed + num1) == target):
                # print(needed, num1)
                num2 = nums.index(needed)
                break
                
        
        if num1 == needed:
            num2 = nums.index(needed, (nums.index(num1) + 1))
        
        return nums.index(num1), num2
            
