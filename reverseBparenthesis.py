class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        while s.find("(") != -1:
            startIndex = s.rfind("(")
            lastIndex = s.find(")",startIndex)
            word = s[startIndex+1:lastIndex]
            reverse = word[::-1]
            s = s.replace("("+word+")",reverse)
        
        return s