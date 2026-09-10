class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_pal(sub):
            return sub == sub[::-1]

        def fun(stage,res,path):
            if stage == len(s):
                res.append(path.copy())
                return
            for end in range(stage,len(s)):
                curr = s[stage:end+1]
                if is_pal(curr):
                    path.append(curr)
                    fun(end+1, res, path)
                    path.pop()
        res= []
        fun(0, res, [])
        return res
