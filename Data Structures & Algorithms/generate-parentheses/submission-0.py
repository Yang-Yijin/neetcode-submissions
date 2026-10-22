class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def dfs(l,r,path):
            if l == 0 and r == 0:
                result.append(path)
                return
            if r < l:
                return
            if l > 0:
                dfs(l-1,r,path+'(')
            if r > 0:
                dfs(l,r-1,path+')')
            
        dfs(n,n,"")
        return result
