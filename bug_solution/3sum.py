class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution = []
        nums.sort ()
        for i in range (len (nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            partial_sol = self.twoSum (nums[i+1:], -nums[i])
            if len(partial_sol) > 0:
                solution += partial_sol
        
        return solution

    def twoSum(self, nums, target):
        solution = []
        left = 0
        right = len (nums) - 1
        while (left < right):
            if left > 0 and nums[left] == nums[left-1]:
                left += 1
            elif right < len (nums) - 2 and nums[right] == nums[right+1]:
                right -= 1
    
            elif nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                solution.append ([-target, nums[left], nums[right]])
                left += 1
                right -= 1

        return solution
