class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def freqCount(n):
            digitFreq = [0 for i in range(10)]
            while n>0:
                digitFreq[n%10] += 1
                n = n/10
            return digitFreq
        def compareArray(freqCount, freqCount2):
            match = True
            for i in range(10):
                if freqCount[i] != freqCount2[i]:
                    return False
            return True
        inputDigitFreq = freqCount(n)
        for i in range(31):
            powerOf2 = pow(2, i)
            powerOf2FreqCount = freqCount(powerOf2)
            if compareArray(powerOf2FreqCount, inputDigitFreq): return True
        return False
        