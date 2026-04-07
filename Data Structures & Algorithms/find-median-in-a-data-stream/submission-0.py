class MedianFinder:

    def __init__(self):
        self.l = []

    def addNum(self, num: int) -> None:
        self.l.append(num)
        self.l.sort()

    def findMedian(self) -> float:
        n = len(self.l)
        mid = (n - 1) // 2
        if n % 2 == 0:
            print(mid)
            return (self.l[mid] + self.l[mid + 1]) / 2
        else:
            return self.l[mid]