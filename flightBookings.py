class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        result = [0] * (n+1)
        
        for booking in bookings:
            
            result[booking[0]-1] += booking[2]
            
            result[booking[1]] -= booking[2]
        
        tmp = 0
        for i in range(n):
            tmp += result[i]
            result[i] = tmp
        return result[:n]