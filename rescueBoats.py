class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort();
        l, r =0,len(people) - 1
        count = 0;

        while l<=r:
            if people[r] +people[l] <= limit:
                count = count + 1
                l = l +1
                r = r-1
            else:
                count += 1
                r = r - 1
        return count        