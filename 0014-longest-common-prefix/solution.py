class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs[0]!='':
            prefix=[strs[0][0]]
            i=0
            j=0
            n=len(strs)
            while i<n:
                if j<len(strs[i]):
                    if strs[i][j]!=prefix[-1]:
                        prefix.pop()
                        return ''.join(prefix)
                    else:
                        i=(i+1)%n
                else:
                    prefix.pop()
                    return ''.join(prefix)
                if i==0:
                    j+=1
                    if j<len(strs[i]):
                        prefix.append(strs[0][j])
                    else:
                        return ''.join(prefix)
        else:
            return ''
