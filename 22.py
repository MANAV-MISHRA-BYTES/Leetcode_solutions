'''
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

'''

#solution:

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openP, closeP, s):
            if openP == closeP and openP + closeP == n * 2:
                res.append(s)
                return
            
            if openP < n:
                dfs(openP + 1, closeP, s + "(")
            
            if closeP < openP:
                dfs(openP, closeP + 1, s + ")")

        dfs(0, 0, "")

        return res
