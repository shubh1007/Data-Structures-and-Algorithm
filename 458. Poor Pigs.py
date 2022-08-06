class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        test = (minutesToTest / minutesToDie) + 1
        count = 0
        total = 1
        while total < buckets:
            total *= test
            count += 1
        return count