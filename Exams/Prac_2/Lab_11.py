
MIN_CAPACITY = 10

class PriorityQueue():      # max heap: from largest to smallest
    def __init__(self, capacity = MIN_CAPACITY, compare = lambda x,y:x > y):
        self._data = [None] * capacity  # data list
        self._length = 0  # actual data length
        self.compare = compare

    def __len__(self):
        return self._length

    def is_empty(self):
        return self._length == 0

    def insert(self, element):
        if self._length + 1 == len(self._data):
            self._resize(2 * len(self._data))
        self._length += 1
        self._data[self._length] = element
        self._bubble_up(self._length)

    def delete_top_priority(self):  # delete max element
        max_element = self._data[1]  # self._data[0] = None
        self._data[1], self._data[self._length] = self._data[self._length], self._data[1] #swap with last element
        self._length -= 1
        if MIN_CAPACITY // 2 <= self._length <= len(self._data) // 4:
            self._resize(len(self._data) // 2)
        self._bubble_down(1)
        return max_element

    def _bubble_up(self, i):  # i is self_length
        if i > 1 and self.compare (self._data[i], self._data[i // 2]):
            self._data[i // 2], self._data[i] = self._data[i], self._data[i // 2]
            self._bubble_up(i // 2)

    def _bubble_down(self, i):
        child = 2 * i
        if child < self._length and self.compare(self._data[child + 1], self._data[child]):
            child += 1 # child is now the biggest child
        if child <= self._length:
            if self.compare(self._data[child], self._data[i]):
                self._data[child], self._data[i] = self._data[i], self._data[child]
                self._bubble_down(child)

    def _resize(self, new_size):
        self._data = list(self._data[ : self._length + 1]) + [None] * (new_size - self._length - 1)


class MaxPriorityQueue(PriorityQueue):
    def __init__(self):
        super().__init__()


class MinPriorityQueue(PriorityQueue):
    def __init__(self):
        super().__init__(compare = lambda x,y:x < y)


class Median():
    def __init__(self):
        self.max_pq = MaxPriorityQueue()  # half smallest [4 3 2 1]
        self.min_pq = MinPriorityQueue()  # half biggest [7 8 9 10]

    def insert(self, element):
        if self.max_pq._data[1] == None:
            self.min_pq.insert(element)
            self.rebalance()
        elif self.min_pq._data[1] == None:
            self.max_pq.insert(element)
            self.rebalance()
        elif element > self.min_pq._data[1]:
            self.min_pq.insert(element)
            self.rebalance()
        elif element < self.max_pq._data[1]:
            self.max_pq.insert(element)
            self.rebalance()
        elif len(self.max_pq) > len(self.min_pq):
             self.min_pq.insert(element)
        else:
             self.max_pq.insert(element)

    def rebalance(self):
        if len(self.max_pq) > len(self.min_pq) + 1:
             self.min_pq.insert(self.max_pq.delete_top_priority())
        elif len(self.min_pq) > len(self.max_pq) + 1:
             self.max_pq.insert(self.min_pq.delete_top_priority())

    def median(self):
        if len(self.max_pq) == len(self.min_pq):
            return (self.min_pq._data[1] + self.max_pq._data[1])/2
        elif len(self.max_pq) > len(self.min_pq):
             return self.max_pq._data[1]
        else:
             return self.min_pq._data[1]


L = [2, 1, 7, 5, 4, 8, 0, 6, 3, 9]
values = Median()
for e in L:
    values.insert(e)
    print(values.median(), end = " ")
print()




