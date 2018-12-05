# A priority queue abstract data type.
#
# Written by Eric Martin for COMP9021


MIN_CAPACITY = 10

class PriorityQueue():      # max heap: from largest to smallest
    def __init__(self, capacity = MIN_CAPACITY, compare = lambda x , y: x > y):
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

    def delete(self):  # delete max element
        max_element = self._data[1]  # self._data[0] = None
        self._data[1], self._data[self._length] = self._data[self._length], self._data[1] #swap with last element
        self._length -= 1
        if MIN_CAPACITY // 2 <= self._length <= len(self._data) // 4:
            self._resize(len(self._data) // 2)
        self._bubble_down(1)
        return max_element

    def _bubble_up(self, i):  # i is self_length
        if i > 1 and self.compare(self._data[i], self._data[i // 2]):
            self._data[i // 2], self._data[i] = self._data[i], self._data[i // 2]
            self._bubble_up(i // 2)

    def _bubble_down(self, i):
        child = 2 * i
        if child < self._length and self.compare(self._data[child + 1],  self._data[child]):
            child += 1 # child is now the biggest child
        if child <= self._length:
            if  self.compare(self._data[child], self._data[i]):
                self._data[child], self._data[i] = self._data[i], self._data[child]
                self._bubble_down(child)

    def _resize(self, new_size):
        self._data = list(self._data[ : self._length + 1]) + [None] * (new_size - self._length - 1)

    def top_priority(self):
        if not self._length:
            return None
        return self._data[1]

    # def delete_top_priority(self):
    #     top_element = self._data[1]
    #     self._data[1], self._data[self._length] = self._data[self._length], self._data[1]
    #     self._length -= 1
    #     if MIN_CAPACITY * 2 <= self._length <= len(self._data) // 4:
    #         self._resize(len(self._data) // 2)
    #     self._bubble_down(1)
    #     return top_element

class MaxPriorityQueue(PriorityQueue):
    def __init__(self):
        super().__init__()   # inherit from super class


class MinPriorityQueue(PriorityQueue):
    def __init__(self):
        super().__init__(compare = lambda x, y: x < y)


class Median():
    def __init__(self):
        self.max_pq = MaxPriorityQueue()
        self.min_pq = MinPriorityQueue()

    def insert(self, element):
        if self.max_pq.top_priority() == None:
            self.min_pq.insert(element)
            self._rebalance()
        elif self.min_pq.top_priority() == None:
            self.max_pq.insert(element)
            self._rebalance()
        elif element < self.max_pq.top_priority():
            self.max_pq.insert(element)
            self._rebalance()
        elif element> self.min_pq.top_priority():
            self.min_pq.insert(element)
            self._rebalance()
        elif len(self.max_pq) <= len(self.min_pq): # in case of equal
            self.max_pq.insert(element)
        else:
            self.min_pq.insert(element)

    def _rebalance(self):
        if len(self.max_pq) > len(self.min_pq) + 1:
            self.min_pq.insert(self.max_pq.delete())
        elif len(self.min_pq) > len(self.max_pq) + 1:
            self.max_pq.insert(self.min_pq.delete())

    def median(self):
       # print(self.max_pq._data, self.min_pq._data)
        if  len(self.max_pq) > len(self.min_pq):
            return self.max_pq.top_priority()
        elif  len(self.max_pq) < len(self.min_pq):
            return self.min_pq.top_priority()
        elif  len(self.max_pq) == len(self.min_pq):
            return (self.max_pq.top_priority() + self.min_pq.top_priority())/2


if __name__ == '__main__':
    L = [2, 1, 7, 5, 4, 8, 0, 6, 3, 9]
    values = Median()
    for e in L:
        values.insert(e)
        print(values.median(), end=' ')
    print()

