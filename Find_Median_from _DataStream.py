#Heap Datastructure

# A Heap is a tree based data structure i which Tree is complete Binary Tree.Heap with N nodes has logN height.
#Min-heap-> The children nodes are maximum or equal to the root node.(The root node value is less in the Tree)
#Max-heap-> The children nodes are minimum or equal to the root node.(The root node value is maximum in the Tree)
from heapq import *

class MedianFinder:
    def __init__(self):
        self.small = [] # smaller half of the list, max heap
        self.large = [] # larger half of the list, min heap
        

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))
        

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])
        

print("Enter operations to execute, separated by commas (e.g., MedianFinder,addNum,findMedian): ")
ops = input().split(',')

# Input data values for "addNum" operations


# Execute operations
medianFinder = None
results = []

for op, num in zip(ops, data):
    if op == "MedianFinder":
        medianFinder = MedianFinder()
        results.append(None)
    elif op == "addNum":
        medianFinder.addNum(num)
        results.append(None)
    elif op == "findMedian":
        median = medianFinder.findMedian()
        results.append(median)

print(results)

