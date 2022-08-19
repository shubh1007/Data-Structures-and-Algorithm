class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        """
        Attribute a number to a existing consecutive subsequences
        future numbers depend on this number to form the subsequence can also
        attribtue to this existing subsequence

        If no existing one to attribtue, form a consecutive (l >= 3) by use the
        subsequent numbers by looking forward

        Let F[i] be the number of consecutive subsequence at A[i]
        """
        counter = defaultdict(int)
        for e in nums:
            counter[e] += 1

        F = defaultdict(int)
        for e in nums:
            if counter[e] == 0:
                continue
            counter[e] -= 1

            if F[e - 1] > 0:
                F[e - 1] -= 1
                F[e] += 1
            elif counter[e + 1] > 0 and counter[e + 2] > 0:
                F[e + 2] += 1
                counter[e + 1] -= 1
                counter[e + 2] -= 1
            else:
                return False

        return True

            
