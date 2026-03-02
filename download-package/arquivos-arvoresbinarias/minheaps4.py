class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent_index(self, index):
        return (index-1)//2
    
    def _left_child_index(self, index):
        return 2*index + 1
    
    def _right_child_index(self, index):
        return 2*index + 2
    
    def _swap(self, i,j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def inserir(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap)-1)

    def _heapify_up(self, index):
        parent_idx = self._parent_index(index)
        if index > 0 and self.heap(index) > self.heap[parent_idx]:
            self._swap(index, parent_idx)
            self._heapify_up(parent_idx)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap = self.heap.pop()
        self._heapify_down(0)
        return root
    
    def _heapify_down(self, index):
        smallest = index
        left = self._left_child_index(index)
        right = self._right_child_index(index)
        n = len(self.heap)

        if left < n and self.heap[0] < self.heap(smallest):
            smallest = left
        if right < n and self.heap[0] < self.heap(smallest):
            smallest = right

        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)

    def __str__(self):
        return str(self.heap)