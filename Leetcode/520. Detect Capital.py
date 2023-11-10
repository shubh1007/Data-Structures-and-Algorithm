class Solution:
    def detectCapitalUse(self, word):
        case1, case2, case3 = True, True, True
        # All Capital
        for i in word:
            if not i.isupper():
                case1 = False
                break
        if case1: return True
        # All Small
        for i in word:
            if not i.islower():
                case2 = False
                break
        if case2: return True
        # Capitalize
        for i in word:
            if word[0].isupper():
                if len(word) == 1: return True
                for i in word[1:]:
                    if not i.islower():
                        case3 = False
                        break
            else: return False
        return case3