class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        l,r = 0,len(cardPoints)-k
        total = sum(cardPoints[r:])
        res = total
        
        while r<len(cardPoints):
            total += (cardPoints[l] - cardPoints[r])
            res = max(res,total)
            r = r+1
            l = l+1
        return res