"""
Structure of comments:
Function description.
Time complexity O()
"""

class minHeap:
    #Initializes an empty min heap.
    #Time complexity: O(1)
    def __init__(self): self.heap = []

    #Returns the number of elements in the min heap.
    #Time complexity: O(1)
    def __len__(self): return len(self.heap)

    #loops through the min heap and returns an iterator.
    #Time complexity: O(n)
    def __iter__(self): return iter(self.heap)

    #Checks if a value exists in the min heap.
    #Time complexity: O(n), where n is the number of elements in the heap.
    def __contains__(self, item): return any(item == v for _, v in self.heap)
    
    #Returns a string representation of the min heap.
    #Time complexity: O(n), where n is the number of elements in the heap.
    def __repr__(self): return str(self.heap)

    #Inserts a key-value pair into the min heap and maintains min heap property.
    #Time complexity: O(log n), where n is the number of elements in the heap.
    def insert(self, key, value):
        self.heap.append((key, value))
        self._sift_up(len(self.heap) - 1)

    #Returns the minimum (root) element without removing it.
    #Time complexity: O(1)
    def peek_min(self):
        if not self.heap: raise IndexError("Empty Heap")

        return self.heap[0]

    #Removes and returns the minimum (root) element from the min heap.
    #Time complexity: O(log n), where n is the number of elements in the heap.
    def extract_min(self):
        if not self.heap: raise IndexError("Empty Heap")

        min_element = self.heap[0]
        last_element = self.heap.pop()

        if self.heap:
            self.heap[0] = last_element
            self._sift_down(0)

        return min_element

    #Converts a list of elements into a valid min heap.
    #Time complexity: O(n), where n is the number of elements.
    def heapify(self, elements):
        self.heap = list(elements)

        for i in reversed(range(self._parent(len(self.heap) - 1) + 1)): self._sift_down(i)

    #Merges another heap into this heap.
    #Time complexity: O(n + m), where n and m are the sizes of the two heaps.
    def meld(self, other_heap):
        combined_heap = self.heap + other_heap.heap
        self.heapify(combined_heap)

        other_heap.heap = []

    #Returns the parent index of a given index in 0-indexed array.
    #Time complexity: O(1)
    def _parent(self, index): return (index - 1) // 2 if index > 0 else None

    #Returns the left child index of a given index.
    #Time complexity: O(1)
    def _left(self, index):
        left = 2 * index + 1

        return left if left < len(self.heap) else None

    #Returns the right child index of a given index.
    #Time complexity: O(1)
    def _right(self, index):
        right = 2 * index + 2

        return right if right < len(self.heap) else None

    #Moves an element up to maintain min heap property after insertion.
    #Time complexity: O(log n), where n is the number of elements in the heap.
    def _sift_up(self, index):
        parent_index = self._parent(index)

        while parent_index is not None and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = self._parent(index)

    #Moves an element down to maintain min heap property after extraction.
    #Time complexity: O(log n), where n is the number of elements in the heap.
    def _sift_down(self, index):
        while True:
            smallest = index

            left = self._left(index)
            right = self._right(index)

            if left is not None and self.heap[left][0] < self.heap[smallest][0]: smallest = left

            if right is not None and self.heap[right][0] < self.heap[smallest][0]: smallest = right

            if smallest == index: break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

    #Searches for a value in the min heap and returns True if found.
    #Time complexity: O(n), where n is the number of elements in the heap.
    def search(self, value): return self.__contains__(value)

    #Checks if the min heap is empty. Returns True if empty, False otherwise.
    #Time complexity: O(1)
    def is_empty(self): return len(self.heap) == 0




class maxHeap:
    #Initializes an empty max heap.
    #Time complexity: O(1)
    def __init__(self):
        self.heap = []

    #Returns the number of elements in the max heap.
    #Time complexity: O(1)
    def __len__(self): return len(self.heap)

    #loops through the max heap and returns an iterator.
    #Time complexity: O(n)
    def __iter__(self): return iter(self.heap)

    #Checks if a value exists in the max heap.
    #Time complexity: O(n), where n is the number of elements in the heap.
    def __contains__(self, item): return any(item == v for _, v in self.heap)
    
    #Returns a string representation of the max heap.
    #Time complexity: O(n), where n is the number of elements in the heap.
    def __repr__(self): return str(self.heap)

    #Inserts a key-value pair into the max heap and maintains max heap property.
    #Time complexity: O(log n), where n is the number of elements in the heap.
    def insert(self, key, value):
        self.heap.append((key, value))
        self._sift_up(len(self.heap) - 1)

    #Returns the maximum (root) element without removing it.
    #Time complexity: O(1)
    def peek_max(self):
        if not self.heap: raise IndexError("Empty Heap")

        return self.heap[0]

    #Removes and returns the maximum (root) element from the max heap.
    #Time complexity: O(log n), where n is the number of elements in the heap.
    def extract_max(self):
        if not self.heap: raise IndexError("Empty Heap")

        max_element = self.heap[0]
        last_element = self.heap.pop()

        if self.heap:
            self.heap[0] = last_element
            self._sift_down(0)

        return max_element

    #Converts a list of elements into a valid max heap.
    #Time complexity: O(n), where n is the number of elements.
    def heapify(self, elements):
        self.heap = list(elements)

        for i in reversed(range(self._parent(len(self.heap) - 1) + 1)): self._sift_down(i)

    #Merges another heap into this heap.
    #Time complexity: O(n + m), where n and m are the sizes of the two heaps.
    def meld(self, other_heap):
        combined_heap = self.heap + other_heap.heap
        self.heapify(combined_heap)

        other_heap.heap = []

    #Returns the parent index of a given index in 0-indexed array.
    #Time complexity: O(1)
    def _parent(self, index): return (index - 1) // 2 if index > 0 else None

    #Returns the left child index of a given index.
    #Time complexity: O(1)
    def _left(self, index):
        left = 2 * index + 1

        return left if left < len(self.heap) else None

    #Returns the right child index of a given index.
    #Time complexity: O(1)
    def _right(self, index):
        right = 2 * index + 2

        return right if right < len(self.heap) else None

    #Moves an element up to maintain max heap property after insertion.
    #Time complexity: O(log n), where n is the number of elements in the heap.
    def _sift_up(self, index):
        parent_index = self._parent(index)

        while parent_index is not None and self.heap[index][0] > self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = self._parent(index)

    #Moves an element down to maintain max heap property after extraction.
    #Time complexity: O(log n), where n is the number of elements in the heap.
    def _sift_down(self, index):
        while True:
            largest = index

            left = self._left(index)
            right = self._right(index)

            if left is not None and self.heap[left][0] > self.heap[largest][0]: largest = left

            if right is not None and self.heap[right][0] > self.heap[largest][0]: largest = right

            if largest == index: break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

    #Searches for a value in the max heap and returns True if found.
    #Time complexity: O(n), where n is the number of elements in the heap.
    def search(self, value): return self.__contains__(value)

    #Checks if the max heap is empty. Returns True if empty, False otherwise.
    #Time complexity: O(1)
    def is_empty(self): return len(self.heap) == 0




if __name__ == "__main__":
    print("==" * 30, "\nMin Heap:\nBeginning:\n", "__" * 30)
    print()
    mH = minHeap()

    mH.insert("a", 10)
    mH.insert("b", 2)
    mH.insert("c", 0)
    mH.insert("d", 67)
    mH.insert("e", 10)

    print(len(mH))
    print(mH)
    print(10 in mH)
    print(mH.peek_min())
    print(mH.extract_min())
    print(mH.search(67))
    print(mH.is_empty())
    print(mH)

    for i in mH: print(i)

    print("==" * 30, "\nMin Heap - End\n")

    MH = maxHeap()

    MH.insert("f", -1)
    MH.insert("q", 8)
    MH.insert("p", 50)
    MH.insert("x", 3)
    MH.insert("y", 7)

    print(len(MH))
    print(MH)
    print(10 in MH)
    print(MH.peek_max())
    print(MH.extract_max())
    print(MH.search(67))
    print(MH.is_empty())
    print(MH)

    for i in MH: print(i)

    print("==" * 30, "\nMax Heap - End\n")
    print()
