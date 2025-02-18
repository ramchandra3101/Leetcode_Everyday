class Solution:
    def Wordbreak(self,s:str, wordDict:dict)->bool:
        n = len(s)
        dp = [False]*(n+1) # we are taking on extra space because we need to copy this to dp[n-x] if word[x:n+1] matches
        dp[n]= True
        for i in range(n-1,-1,-1):
            for w in wordDict:
                if (i+len(w))<=n and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]
    
if __name__ == "__main__":    
    wordDict = ["leet","code"]
    s = "leetcode"
    sol = Solution()
    res = sol.Wordbreak(s,wordDict)
    print(res)



