from typing import List
class Solution:
    def tournamentWinner(self, competitions: List[List[int]], results: List[int]) -> str:
        scores = {}
        for idx, match in enumerate(competitions):
            if results[idx] == 0:
                # away team won the match, idx 1 won the game
                if match[1] in scores:
                    scores[match[1]] += 3
                else:
                    scores[match[1]] = 3
            else:
                # home team won the match, idx 0 won the game
                if match[0] in scores:
                    scores[match[0]] += 3
                else:
                    scores[match[0]] = 3
        res = -float("inf")
        output = ""
        for key, val in scores.items():
            if val > res:
                res = val
                output = key
        return output

competitions = [["HTML", "C#"],
                ["C#", "Python"],
                ["Python", "HTML"],]
results = [0, 0, 1]
sol = Solution()
res = sol.tournamentWinner(competitions, results)
print(res)


