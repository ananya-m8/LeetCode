class MedianFinder:

    def __init__(self):
        self.arr=[]

    def addNum(self, num: int) -> None:
        if self.arr==[]:
            self.arr.append(num)
            return
        if(num>=self.arr[-1]):
            self.arr.append(num)
            return
        for i in range(len(self.arr)):
            if num<=(self.arr[i]):
                self.arr.insert(i,num)
                return
        self.arr.append(num)
    def findMedian(self) -> float:
        n=len(self.arr)
        mid=n//2
        if(n%2==0):
            return (self.arr[mid]+self.arr[mid-1])/2
        else:
            return self.arr[mid]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
