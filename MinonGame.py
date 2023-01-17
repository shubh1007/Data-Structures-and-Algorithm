class Solution:
    def minionGame(self, string):
        Stuart = 0
        Kevin = 0
        n = len(string)
        vowels = ["A","E","I","O","U"]
        string.lower()
        for i in range(n):
            remaining = n - i
            if string[i] in vowels:
                Kevin += remaining
            else:
                Stuart += remaining
        if Stuart > Kevin:
            print(f"Stuart {Stuart}")
        elif Stuart < Kevin:
            print(f"Kevin {Kevin}")
        else:
            print("Draw")
    

        # Stuart = 0
        # Kevin = 0
        # vowels = ['A', 'E', 'I', 'O', 'U']
        # n = len(S)
        # for i in range(n):
        #     remaining = n - i
        #     if S[i] in vowels:
        #         Kevin += remaining
        #     else:
        #         Stuart += remaining
        # print(f"Staurt {Stuart}" if Stuart >= Kevin else f"Kevin {Kevin}")
    
S = "BANANA"
sol = Solution()
sol.minionGame(S)