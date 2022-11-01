class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        lastIndex = {}
        for i,c in enumerate(s):
            lastIndex[c] = i
        
        res = []
        end,size = 0,0
        for i,c in enumerate(s):
            size = size+1
            end = max(lastIndex[c],end)
            if i == end:
                res.append(size)
                size = 0
        return res