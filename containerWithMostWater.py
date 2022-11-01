class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        output=0
        while(r > l):
            if height[r] > height[l]:
                val = height[l] * (r-l)
                output = max(output,val)
                l = l+1
            elif height[r] < height[l]:
                val = height[r] * (r-l)
                output = max(output,val)
                r = r-1
            else:
                val = height[r] *(r-l)
                output=max(output,val)
                r=r-1
                l=l+1
        return output
                