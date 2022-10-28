class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        postfix = []
        prefix = []
        output = []
        for x in range(len(nums)):
            
            if(x == 0):
                prefix.append(nums[x])
            else:
                prefix.append(nums[x] * prefix[x-1])
                
        for x in reversed(range(len(nums))):

            if(x == len(nums)-1):
                postfix.append(nums[x]) 
            else:
                postfix.append(nums[x] * postfix[len(nums)-2-x])
        postfix.reverse()
        for x in range(len(nums)):
            if x == 0:
                output.append(postfix[x+1])
            elif x == len(nums)-1:
                output.append(prefix[x-1])
            else:
                output.append(prefix[x-1] * postfix[x+1])
        return output