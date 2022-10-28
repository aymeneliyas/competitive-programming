class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0;
        right = 0;
        
        for x in nums:
            if x != 0:
                nums[left] , nums[right] = nums[right],nums[left]
                left = left + 1;
                right = right +1;
            else:
                right = right + 1;
        return nums;