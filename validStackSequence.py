class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        arr = []
        i=0
        for x in pushed:
            arr.append(x)
            while arr and i<len(pushed) and popped[i] == arr[-1]:
                arr.pop()
                i += 1
        return arr == []