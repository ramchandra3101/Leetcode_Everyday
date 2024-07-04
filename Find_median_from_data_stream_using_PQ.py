from heapq import heappush, heappushpop

class MedianFinder:

    def __init__(self):
        self.small = [] # store -ve value to access the largest
        self.large = []
        self.balanced = True
        self.empty = True

    def addNum(self, num: int) -> None:
        self.empty = False
        
        if self.balanced:
            # push value to small, pop smallest, and push that value to large
            heappush(self.large, -heappushpop(self.small, -num))
            self.balanced = False
            
            # large will have one more than small
        else:
            # push to small
            heappush(self.small, -heappushpop(self.large, num))
            self.balanced = True
        

    def findMedian(self) -> float:
        if self.empty:
            return
        if self.balanced:
            return (self.large[0] - self.small[0])/2
        else:
            return self.large[0]