class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        i = 0
        j = 0
        # for i in range(len(nums)-1):
        #     for j in range(0,len(nums)-i-1):
        #         if(int(nums[j]) > int(nums[j+1])):
        #             nums[j+1],nums[j] = nums[j],nums[j+1]
        nums.sort(key=lambda x:int(x))
                    
        # while k > 0:
        #     x = nums.pop()
        #     k = k - 1;
        return nums[-k]