class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        o=''
        s=strs[0]
        e=strs[-1]
        d=min(len(s),len(e))
        i=0
        while i<d:
            if s[i]==e[i]:
                o+=s[i]
                i+=1
            else:
                break
        return o
