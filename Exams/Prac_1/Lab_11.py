from priority_queue import *



class MinPriorityQueue(PriorityQueue):
    def __init__(self):
        super().__init__(function = lambda x, y: x <y)

class MaxPriorityQueue(PriorityQueue):
    def __init__(self):
        super().__init__()

class Median():
    def __init__(self):
        self.max_pq = MaxPriorityQueue()
        self.min_pq = MinPriorityQueue()

    def median(self):
        if self.max_pq._length == self.min_pq._length:
            return (self.max_pq._data[1] + self.min_pq._data[1])/2
        elif self.max_pq._length > self.min_pq._length:
            return self.max_pq._data[1]
        else:
            return self.min_pq._data[1]

    def insert(self, value):
        if self.max_pq._length == 0:
            self.min_pq.insert(value)
            self.rebalance()
        elif self.min_pq._length == 0:
            self.max_pq.insert(value)
            self.rebalance()
        elif value< self.max_pq._data[1]:
            self.max_pq.insert(value)
            self.rebalance()
        elif value> self.max_pq._data[1] :
            self.min_pq.insert(value)
            self.rebalance()
        elif self.max_pq._length > self.min_pq._length:
             self.min_pq.insert(value)
        else:
             self.max_pq.insert(value)
        print(self.max_pq._data, self.min_pq._data)


    def rebalance(self):
        if self.max_pq._length > self.min_pq._length + 1:
            self.min_pq.insert(self.max_pq.delete())
        elif self.min_pq._length > self.max_pq._length + 1:
            self.max_pq.insert(self.min_pq.delete())


if __name__ == '__main__':
    L = [2, 1, 7, 5, 4, 8, 0, 6, 3, 9]
    values = Median()
    for e in L:
        values.insert(e)
        print(values.median(), end = '  ')
    print()