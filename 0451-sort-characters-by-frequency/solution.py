class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
        s_ch=sorted(count,key=count.get,reverse=True)
        result=''
        for char in s_ch:
            result+=char*count[char]
        return result
        
