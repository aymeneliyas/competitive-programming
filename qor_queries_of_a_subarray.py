class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        prefix,ans = [0],[]
        temp = 0
        for i in range(len(arr)):
            temp ^= arr[i]
            prefix.append(temp)
        for l,r in queries:
            ans.append(prefix[r+1] ^ prefix[l])
        return ans