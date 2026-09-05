from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr=list(map(str,nums))
        def cmp(a,b):
            ab=a+b
            ba=b+a
            if ab>ba:
                return -1
            else:
                return 1
        arr.sort(key=cmp_to_key(cmp))
        res=''.join(arr)
        if res[0]=='0':
            return '0'
        return res
