class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        l=defaultdict(int)
        start=0
        max_len=0
        for i in range(n):
            l[fruits[i]]+=1
            while len(l)>2:
                l[fruits[start]]-=1
                if l[fruits[start]]==0:
                    del l[fruits[start]]
                start+=1
            max_len=max(max_len,i-start+1)
        return max_len
