"""
Structure of comments:
Function description.
Time complexity O()
"""

#Stack Node class - Represents a single node in the Stack data structure.
class Node:
    #Initializes the node with data, and a reference to the next node.
    #Time complexity: O(1)
    def __init__(self, data):
        self.data = data
        self.next = None


#Stack class - Implements a stack data structure using a linked list.
#LIFO (Last In First Out) principle: elements are added and removed from the top.
class Stack:
    #Initializes an empty stack with top pointer set to None and size counter set to 0.
    #Time complexity: O(1)
    def __init__(self):
        self.top = None
        self.size = 0

    #Returns the number of elements currently in the stack.
    #Time complexity: O(1)
    def __len__(self): return self.size

     #return an iterator that yields the elements of the stack from top to bottom. note that the items are in string format.
    #Time complexity: O(n)
    def __iter__(self):
        items = []

        curr = self.top
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next

        return reversed(items)

    #Returns a string representation of the stack showing all elements from top to bottom.
    #Time complexity: O(n), where n is the number of elements in the stack.
    def __repr__(self):
        if self.is_empty(): return "[]"
        items = []

        curr = self.top
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next
        items.append("None")

        return "->".join(items)

    #Adds an element to the top of the stack and increases the size counter.
    #Time complexity: O(1)
    def push(self, data):
        new_node = Node(data)

        new_node.next = self.top
        self.top = new_node

        self.size += 1

    #Removes and returns the element at the top of the stack. Raises ValueError if stack is empty.
    #Time complexity: O(1)
    def pop(self):
        if self.is_empty(): raise ValueError("Empty Stack!")

        popped_value = self.top.data

        self.top = self.top.next
        self.size -= 1

        return popped_value

    #Returns the element at the top of the stack without removing it. Raises ValueError if stack is empty.
    #Time complexity: O(1)
    def peek(self):
        if self.is_empty(): raise ValueError("Empty Stack!")

        return self.top.data

    #Checks if the stack is empty. Returns True if empty, False otherwise.
    #Time complexity: O(1)
    def is_empty(self): return self.top is None




#Queue Node class - Represents a single node in the Queue data structure.
class Node:
    #Initializes the node with data and a reference to the next node.
    #Time complexity: O(1)
    def __init__(self, data):
        self.data = data
        self.next = None
        
#Queue class - Implements a queue data structure using a linked list.
#FIFO (First In First Out) principle: elements are added at rear and removed from front.
class Queue:
    #Initializes an empty queue with front and rear pointers set to None and size counter set to 0.
    #Time complexity: O(1)
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    #Returns the number of elements currently in the queue.
    #Time complexity: O(1)
    def __len__(self): return self.size

    #Loops the queue's items and return those items to be used in iteriitions.
    #Time complexity: O(n)
    def __iter__(self):
        items = []

        curr = self.front
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next

        yield from items

    #Returns a string representation of the queue showing all elements from front to rear.
    #Time complexity: O(n), where n is the number of elements in the queue.
    def __repr__(self):
        if self.is_empty(): return "[]"

        items = []

        curr = self.front
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next
        items.append("None")

        return "->".join(items)

    #Adds an element to the rear of the queue.
    #Time complexity: O(1)
    def enqueue(self, data):
        new_node = Node(data)

        if self.is_empty(): self.front = self.rear = new_node

        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    #Removes and returns the element at the front of the queue. Raises IndexError if queue is empty.
    #Time complexity: O(1)
    def dequeue(self):
        if self.is_empty(): raise IndexError("Empty Queue!")

        dequeue_value = self.front.data
        self.front = self.front.next

        if self.is_empty(): self.rear = None

        self.size -= 1

        return dequeue_value

    #Returns the element at the front of the queue without removing it. Raises IndexError if queue is empty.
    #Time complexity: O(1)
    def peek(self):
        if self.is_empty(): raise IndexError("Empty Queue!")
        return self.front.data

    #Checks if the queue is empty. Returns True if empty, False otherwise.
    #Time complexity: O(1)
    def is_empty(self): return self.front is None and self.rear is None




#Singly Linked List Node class - Represents a single node in a singly linked list.
class Node:
    #Initializes the node with data and a reference to the next node.
    #Time complexity: O(1)
    def __init__(self, data):
        self.data = data
        self.next = None

class NodeWithPrev(Node):
    #Creates a node with an extra previous-pointer reference for doubly linked lists.
    #Time complexity: O(1)
    def __init__(self, data):
        self.prev = None
        super().__init__(data)


#LinkedLists parent class - Base class for singly linked list implementations (with and without tail).
class LinkedLists:
    #Initializes an empty linked list with head pointer set to None and size counter set to 0.
    #Time complexity: O(1)
    def __init__(self):
        self.head = None
        self.size = 0


#Singly Linked List with Tail - Efficient implementation with direct access to both head and tail.
class SinglyLinkedList(LinkedLists):
    #Initializes an empty singly linked list with head and tail pointers set to None.
    #Time complexity: O(1)
    def __init__(self):
        self.tail = None
        super().__init__()

    #Returns the number of elements currently in the linked list.
    #Time complexity: O(1)
    def __len__(self): return self.size

    #Loops throgh items of the linked list
    #Time complexity: O(n)
    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr.data
            curr = curr.next


    #Returns a string representation of the linked list showing all elements from head to tail.
    #Time complexity: O(n), where n is the number of elements in the list.
    def __repr__(self):
        if self.is_empty(): return "[]"

        items = []
        curr = self.head
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next
        items.append("None")

        return "->".join(items)

    #Checks if an item exists in the linked list. Raises ValueError if list is empty.
    #Time complexity: O(n), where n is the number of elements in the list.
    def __contains__(self, item):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        while curr is not None:
            if curr.data == item: return True
            curr = curr.next

        return False

    #Adds an element to the end of the linked list.
    #Time complexity: O(1)
    def append(self, data):
        new_node = Node(data)

        if self.is_empty(): self.head = new_node

        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    #Adds an element to the beginning of the linked list.
    #Time complexity: O(1)
    def prepend(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    #Inserts an element at the specified index position. Raises ValueError if index is out of range.
    #Time complexity: O(n), where n is the index position.
    def insert(self, value, index):
        if index < 0: raise ValueError("Index out of range!")

        if index == 0:
            self.prepend(value)
            return
        
        if self.is_empty(): raise ValueError("Empty List!")

        new_node = Node(value)

        curr = self.head
        for _ in range(index - 1):
            if curr.next is None: raise ValueError("Index out of range!")
            curr = curr.next

        new_node.next = curr.next
        curr.next = new_node

        if new_node.next is None: self.tail = new_node
        self.size += 1

    #Removes the first occurrence of an element with the specified value. Raises ValueError if list is empty.
    #Time complexity: O(n), where n is the number of elements in the list.
    def remove(self, value):
        if self.is_empty(): raise ValueError("Empty List!")

        if self.head.data == value:
            self.head = self.head.next

            if self.head is None: self.tail = None
            self.size -= 1

            return

        curr = self.head
        while curr.next is not None:
            if curr.next.data == value:
                if curr.next == self.tail: self.tail = curr
                curr.next = curr.next.next
                self.size -= 1

                return
            
            curr = curr.next

    #Removes and returns the element at the specified index, or the last element if no index is provided.
    #Time complexity: O(n), where n is the index position.
    def pop(self, index=None):
        if self.is_empty(): raise ValueError("Empty List!")

        if index is None: index = self.size - 1

        if index < 0: raise ValueError("Index out of range!")

        if index == 0:
            popped_value = self.head.data
            self.head = self.head.next

            if self.head is None: self.tail = None
            self.size -= 1

            return popped_value

        curr = self.head
        for _ in range(index - 1):
            if curr.next is None: raise ValueError("Index out of range!")
            curr = curr.next

        if curr.next is None: raise ValueError("Index out of range!")

        popped_value = curr.next.data
        if curr.next == self.tail: self.tail = curr

        curr.next = curr.next.next
        self.size -= 1

        return popped_value

    #Searches for a value in the linked list.
    #Time complexity: O(n), where n is the number of elements in the list.
    def search(self, value):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        while curr is not None:
            if curr.data == value: return True
            curr = curr.next
        return False

    #Returns the value at the specified index.
    #Time complexity: O(n), where n is the index position.
    def get(self, index):
        if self.is_empty(): raise ValueError("Empty List!")

        if index < 0: raise ValueError("Index out of range!")

        curr = self.head
        for _ in range(index):
            if curr.next is None: raise ValueError("Index out of range!")
            curr = curr.next
        return curr.data

    #Prints all elements in the linked list from head to tail.
    #Time complexity: O(n), where n is the number of elements in the list.
    def display(self):
        if self.is_empty(): raise ValueError("Empty List!")

        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    #Checks if the linked list is empty. Returns True if empty, False otherwise.
    #Time complexity: O(1)
    def is_empty(self): return self.head is None and self.tail is None


#Singly Linked List without Tail - Simple implementation with head pointer only.
class SinglyLinkedListWithoutTail(LinkedLists):
    #Initializes an empty singly linked list with head pointer set to None.
    #Time complexity: O(1)
    def __init__(self):
        super().__init__()

    #Returns the number of elements currently in the linked list.
    #Time complexity: O(1)
    def __len__(self): return self.size

    #Loops throgh items of the linked list
    #Time complexity: O(n)
    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr.data
            curr = curr.next


    #Returns a string representation of the linked list showing all elements from head to end.
    #Time complexity: O(n), where n is the number of elements in the list.
    def __repr__(self):
        if self.is_empty(): return "[]"

        items = []
        curr = self.head
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next
        items.append("None")
        return "->".join(items)

    #Checks if an item exists in the linked list. Raises ValueError if list is empty.
    #Time complexity: O(n), where n is the number of elements in the list.
    def __contains__(self, item):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        while curr is not None:
            if curr.data == item: return True
            curr = curr.next
        return False

    #Adds an element to the end of the linked list.
    #Time complexity: O(n), where n is the number of elements (must traverse to find tail).
    def append(self, data):
        new_node = Node(data)

        if self.is_empty(): self.head = new_node
        else:
            tail = self.head
            while tail.next is not None: tail = tail.next
            tail.next = new_node
        self.size += 1

    #Adds an element to the beginning of the linked list.
    #Time complexity: O(1)
    def prepend(self, data):
        new_node = Node(data)

        if self.is_empty(): self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    #Inserts an element at the specified index position. Raises ValueError if index is out of range.
    #Time complexity: O(n), where n is the index position.
    def insert(self, value, index):
        if index < 0: raise ValueError("Index out of range!")

        if index == 0:
            self.prepend(value)
            return
        
        if self.is_empty(): raise ValueError("Empty List!")

        new_node = Node(value)

        curr = self.head
        for _ in range(index - 1):
            if curr.next is None: raise ValueError("Index out of range!")
            curr = curr.next

        new_node.next = curr.next
        curr.next = new_node
        self.size += 1

    #Removes the first occurrence of an element with the specified value. Raises ValueError if list is empty.
    #Time complexity: O(n), where n is the number of elements in the list.
    def remove(self, value):
        if self.is_empty(): raise ValueError("Empty List!")

        if self.head.data == value:
            self.head = self.head.next
            self.size -= 1
            return

        curr = self.head
        while curr.next is not None:
            if curr.next.data == value:
                curr.next = curr.next.next
                self.size -= 1
                return
            curr = curr.next

    #Removes and returns the element at the specified index, or the last element if no index is provided.
    #Time complexity: O(n), where n is the index position.
    def pop(self, index=None):
        if self.is_empty(): raise ValueError("Empty List!")

        if index is None: index = self.size - 1

        if index < 0: raise ValueError("Index out of range!")

        if index == 0:
            popped_value = self.head.data
            self.head = self.head.next
            self.size -= 1
            return popped_value

        curr = self.head
        for _ in range(index - 1):
            if curr.next is None: raise ValueError("Index out of range!")
            curr = curr.next

        if curr.next is None: raise ValueError("Index out of range!")

        popped_value = curr.next.data
        curr.next = curr.next.next
        self.size -= 1
        return popped_value

    #Searches for a value in the linked list.
    #Time complexity: O(n), where n is the number of elements in the list.
    def search(self, value):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        while curr is not None:
            if curr.data == value: return True
            curr = curr.next
        return False

    #Returns the value at the specified index.
    #Time complexity: O(n), where n is the index position.
    def get(self, index):
        if self.is_empty(): raise ValueError("Empty List!")

        if index < 0: raise ValueError("Index out of range!")

        curr = self.head
        for _ in range(index):
            if curr.next is None: raise ValueError("Index out of range!")
            curr = curr.next
        return curr.data

    #Prints all elements in the linked list from head to end.
    #Time complexity: O(n), where n is the number of elements in the list.
    def display(self):
        if self.is_empty(): raise ValueError("Empty List!")

        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    #Checks if the linked list is empty. Returns True if empty, False otherwise.
    #Time complexity: O(1)
    def is_empty(self): return self.head is None


class DoublyLinkedList(LinkedLists):
    #Initializes an empty doubly linked list with head and tail pointers set to None.
    #Time complexity: O(1)
    def __init__(self):
        self.tail = None
        super().__init__()

    #Returns the number of elements currently in the doubly linked list.
    #Time complexity: O(1)
    def __len__(self): return self.size

    #Loops throgh items of the linked list
        #Time complexity: O(n)
    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr.data
            curr = curr.next


    #Returns a string representation of the doubly linked list from head to tail.
    #Time complexity: O(n), where n is the number of elements in the list.
    def __repr__(self):
        if self.is_empty(): return "[]"

        items = ["None"]
        curr = self.head
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next
        items.append("None")
        return "<->".join(items)

    #Checks whether a given item exists in the doubly linked list.
    #Time complexity: O(n), where n is the number of elements in the list.
    def __contains__(self, item):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        while curr is not None:
            if curr.data == item: return True
            curr = curr.next
        return False

    #Adds a new node to the end of the doubly linked list.
    #Time complexity: O(1)
    def append(self, data):
        new_node = NodeWithPrev(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    #Adds a new node to the beginning of the doubly linked list.
    #Time complexity: O(1)
    def prepend(self, data):
        new_node = NodeWithPrev(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    #Inserts a value at the specified index in the doubly linked list.
    #Time complexity: O(n), where n is the index position.
    def insert(self, value, index):
        if index < 0: raise ValueError("Index out of range!")

        if index == 0:
            self.prepend(value)
            return
        
        if self.is_empty(): raise ValueError("Empty List!")

        new_node = NodeWithPrev(value)

        curr = self.head
        for _ in range(index - 1):
            if curr.next is None: raise ValueError("Index out of range!")
            curr = curr.next

        new_node.prev = curr
        new_node.next = curr.next

        if curr.next is not None: curr.next.prev = new_node
        curr.next = new_node
        if new_node.next is None: self.tail = new_node
        self.size += 1

    #Removes the first occurrence of a given value from the doubly linked list.
    #Time complexity: O(n), where n is the number of elements in the list.
    def remove(self, value):
        if self.is_empty(): raise ValueError("Empty List!")

        if self.head.data == value:
            self.head = self.head.next

            if self.head is not None: self.head.prev = None
            else: self.tail = None
            self.size -= 1
            return

        curr = self.head
        while curr is not None:
            if curr.data == value:
                if curr.next is not None: curr.next.prev = curr.prev
                if curr.prev is not None: curr.prev.next = curr.next
                if curr == self.tail: self.tail = curr.prev
                self.size -= 1
                return
            curr = curr.next

    #Removes and returns the value at the specified index in the doubly linked list.
    #Time complexity: O(n), where n is the index position.
    def pop(self, index=None):
        if self.is_empty(): raise ValueError("Empty List!")

        if index is None: index = self.size - 1

        if index < 0: raise ValueError("Index out of range!")

        curr = self.head
        for _ in range(index):
            if curr is None: raise ValueError("Index out of range!")
            curr = curr.next

        if curr is None: raise ValueError("Index out of range!")

        popped_value = curr.data
        if curr.prev is not None: curr.prev.next = curr.next
        else: self.head = curr.next
        if curr.next is not None: curr.next.prev = curr.prev
        else: self.tail = curr.prev

        self.size -= 1
        return popped_value

    #Searches for a value in the doubly linked list.
    #Time complexity: O(n), where n is the number of elements in the list.
    def search(self, value):
        if self.is_empty(): raise ValueError("Empty List!")
        curr = self.head
        while curr is not None:
            if curr.data == value: return True
            curr = curr.next
        return False

    #Returns the value stored at the specified index in the doubly linked list.
    #Time complexity: O(n), where n is the index position.
    def get(self, index):
        if self.is_empty(): raise ValueError("Empty List!")

        if index < 0 or index >= self.size: raise ValueError("Index out of range!")

        curr = self.head
        for _ in range(index): curr = curr.next
        return curr.data

    #Prints all elements in the doubly linked list from head to tail.
    #Time complexity: O(n), where n is the number of elements in the list.
    def display(self):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        print("None<->", end="")
        while curr is not None:
            print(curr.data, end="<->")
            curr = curr.next
        print("None")

    #Checks if the doubly linked list is empty. Returns True if empty, False otherwise.
    #Time complexity: O(1)
    def is_empty(self): return self.head is None and self.tail is None


class CircularLinkedList(LinkedLists):
    #Initializes an empty circular linked list with head and tail set to None.
    #Time complexity: O(1)
    def __init__(self):
        self.tail = None
        super().__init__()

    #Returns the number of elements currently in the circular linked list.
    #Time complexity: O(1)
    def __len__(self):
        return self.size

    #Loops throgh items of the linked list
    #Time complexity: O(n)
    def __iter__(self):
        curr = self.head
        for _ in range(self.size):
            yield curr.data
            curr = curr.next


    #Returns a string representation of the circular linked list.
    #Time complexity: O(n), where n is the number of elements in the list.
    def __repr__(self):
        if self.is_empty(): return "[]"
        
        items = ["Tail"]
        curr = self.head
        for _ in range(self.size):
            items.append(str(curr.data))
            curr = curr.next
        return "->".join(items) + "->HEAD"

    #Checks whether a given item exists in the circular linked list.
    #Time complexity: O(n), where n is the number of elements in the list.
    def __contains__(self, item):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        for _ in range(self.size):
            if curr.data == item: return True
            curr = curr.next
        return False

    #Adds an element to the end of the circular linked list.
    #Time complexity: O(1)
    def append(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head

        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    #Adds an element to the beginning of the circular linked list.
    #Time complexity: O(1)
    def prepend(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head

        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.size += 1

    #Inserts a value at the specified index in the circular linked list.
    #Time complexity: O(n), where n is the index position.
    def insert(self, value, index):
        if index < 0: raise ValueError("Index out of range!")

        if index == 0:
            self.prepend(value)
            return
        
        if self.is_empty(): raise ValueError("Empty List!")

        if index > self.size: raise ValueError("Index out of range!")

        new_node = Node(value)

        curr = self.head
        for _ in range(index - 1): curr = curr.next

        new_node.next = curr.next
        curr.next = new_node

        if curr == self.tail: self.tail = new_node
        self.size += 1

    #Removes the first occurrence of a given value from the circular linked list.
    #Time complexity: O(n), where n is the number of elements in the list.
    def remove(self, value):
        if self.is_empty(): raise ValueError("Empty List!")

        if self.size == 1:
            if self.head.data == value:
                self.head = None
                self.tail = None
                self.size = 0
                return

        if self.head.data == value:
            self.head = self.head.next
            self.tail.next = self.head
            self.size -= 1
            return

        prev = self.head
        curr = self.head.next
        while curr is not self.head:
            if curr.data == value:
                prev.next = curr.next

                if curr == self.tail: self.tail = prev
                self.size -= 1
                return
            prev = curr
            curr = curr.next

    #Removes and returns the value at the specified index in the circular linked list.
    #Time complexity: O(n), where n is the index position.
    def pop(self, index=None):
        if self.is_empty(): raise ValueError("Empty List!")

        if index is None: index = self.size - 1

        if index < 0 or index >= self.size: raise ValueError("Index out of range!")

        if self.size == 1:
            popped_value = self.head.data
            self.head = None
            self.tail = None
            self.size = 0
            return popped_value

        if index == 0:
            popped_value = self.head.data
            self.head = self.head.next
            self.tail.next = self.head
            self.size -= 1
            return popped_value

        prev = self.head
        curr = self.head.next
        for _ in range(index - 1):
            prev = curr
            curr = curr.next

        popped_value = curr.data
        prev.next = curr.next

        if curr == self.tail: self.tail = prev
        self.size -= 1
        return popped_value

    #Searches for a value in the circular linked list.
    #Time complexity: O(n), where n is the number of elements in the list.
    def search(self, value):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        for _ in range(self.size):
            if curr.data == value: return True
            curr = curr.next
        return False

    #Returns the value stored at the specified index in the circular linked list.
    #Time complexity: O(n), where n is the index position.
    def get(self, index):
        if self.is_empty(): raise ValueError("Empty List!")

        if index < 0 or index >= self.size: raise ValueError("Index out of range!")

        curr = self.head
        for _ in range(index): curr = curr.next
        return curr.data

    #Prints all elements in the circular linked list.
    #Time complexity: O(n), where n is the number of elements in the list.
    def display(self):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        print("Tail->", end="")
        for _ in range(self.size):
            print(curr.data, end=" -> ")
            curr = curr.next
        print("HEAD")

    #Checks if the circular linked list is empty. Returns True if empty, False otherwise.
    #Time complexity: O(1)
    def is_empty(self): return self.head is None and self.tail is None


class CircularDoublyLinkedList(LinkedLists):
    #Initializes an empty circular doubly linked list with head, tail, and size set to default values.
    #Time complexity O(1)
    def __init__(self):
        self.tail = None
        super().__init__()

    #Returns the number of elements currently in the circular doubly linked list.
    #Time complexity O(1)
    def __len__(self):
        return self.size

    #Loops throgh items of the linked list
    #Time complexity: O(n)
    def __iter__(self):
        curr = self.head
        for _ in range(self.size):
            yield curr.data
            curr = curr.next


    #Returns a string representation of the circular doubly linked list.
    #Time complexity O(n)
    def __repr__(self):
        if self.is_empty(): raise ValueError("Empty List!")

        items = ["Tail"]
        curr = self.head
        while True:
            items.append(str(curr.data))
            curr = curr.next
            if curr == self.head:
                break
        items.append("Head")
        return "<->".join(items)

    #Checks whether a given item exists in the circular doubly linked list.
    #Time complexity O(n)
    def __contains__(self, item):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        while True:
            if curr.data == item: return True
            curr = curr.next
            if curr == self.head: break
        return False

    #Adds a new node to the end of the circular doubly linked list.
    #Time complexity O(1)
    def append(self, data):
        new_node = NodeWithPrev(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node

            new_node.next = new_node
            new_node.prev = new_node

        else:
            new_node.prev = self.tail
            new_node.next = self.head

            self.tail.next = new_node
            self.head.prev = new_node

            self.tail = new_node
        self.size += 1

    #Adds a new node to the beginning of the circular doubly linked list.
    #Time complexity O(1)
    def prepend(self, data):
        new_node = NodeWithPrev(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node

            new_node.next = new_node
            new_node.prev = new_node

        else:
            new_node.next = self.head
            new_node.prev = self.tail

            self.head.prev = new_node
            self.tail.next = new_node

            self.head = new_node
        self.size += 1

    #Inserts a value at the specified index in the circular doubly linked list.
    #Time complexity O(n)
    def insert(self, value, index):
        if index < 0: raise ValueError("Index out of range!")

        if index == 0:
            self.prepend(value)
            return

        if index == self.size:
            self.append(value)
            return

        new_node = NodeWithPrev(value)

        curr = self.head
        for _ in range(index):
            curr = curr.next
        new_node.prev = curr.prev
        new_node.next = curr

        curr.prev.next = new_node
        curr.prev = new_node
        
        self.size += 1

    #Removes the first occurrence of a given value from the circular doubly linked list.
    #Time complexity O(n)
    def remove(self, value):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        for _ in range(self.size):
            if curr.data == value:
                if self.size == 1:
                    self.head = None
                    self.tail = None
                    self.size = 0
                    return

                curr.prev.next = curr.next
                curr.next.prev = curr.prev

                if curr == self.head: self.head = curr.next
                if curr == self.tail: self.tail = curr.prev

                self.size -= 1
                return
            curr = curr.next

    #Removes and returns the value at the specified index in the circular doubly linked list.
    #Time complexity O(n)
    def pop(self, index=None):
        if self.is_empty(): raise ValueError("Empty List!")

        if index is None: index = self.size - 1

        if (index < 0) or (index >= self.size): raise ValueError("Index out of range!")

        curr = self.head
        for _ in range(index):
            curr = curr.next

        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return curr.data

        curr.prev.next = curr.next
        curr.next.prev = curr.prev

        if curr == self.head: self.head = curr.next
        if curr == self.tail: self.tail = curr.prev

        self.size -= 1
        return curr.data

    #Searches for a value in the circular doubly linked list.
    #Time complexity O(n)
    def search(self, value):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        while True:
            if curr.data == value: return True
            curr = curr.next
            if curr == self.head: break
        return False

    #Returns the value stored at the specified index in the circular doubly linked list.
    #Time complexity O(n)
    def get(self, index):
        if self.is_empty(): raise ValueError("Empty List!")
        
        if index < 0 or index >= self.size: raise ValueError("Index out of range!")
        
        curr = self.head
        for _ in range(index): curr = curr.next
        return curr.data
        
    #Prints all elements in the circular doubly linked list.
    #Time complexity O(n)
    def display(self):
        if self.is_empty(): raise ValueError("Empty List!")

        curr = self.head
        print("Tail<->", end="")
        while True:
            print(curr.data, end="<->")
            curr = curr.next
            if curr == self.head:
                break
        print("Head")

    #Checks if the circular doubly linked list is empty.
    #Time complexity O(1)
    def is_empty(self): return self.head is None and self.tail is None


class HashMap:
    # Initializes an empty hash map with specified capacity and bucket array.
    # Time Complexity: O(capacity)
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    # Returns the number of key-value pairs currently in the hash map.
    # Time Complexity: O(1)
    def __len__(self): return self.size

    # Returns an iterator over all key-value pairs in the hash map.
    # Time Complexity: O(n)
    def __iter__(self): 
        for bucket in self.buckets: yield from bucket

    # Checks if a key exists in the hash map. Returns True if key exists, False otherwise.
    # Time Complexity: O(1) average, O(n) worst case (where n is bucket size)
    def __contains__(self, item):
        index = self._hash_function(item)
        bucket = self.buckets[index]
        
        return any(k == item or v == item for k, v in bucket)

    # Returns a string representation of the hash map showing all key-value pairs.
    # Time Complexity: O(n) - where n is the total number of entries
    def __repr__(self): return str(self.items())

    # Inserts or updates a key-value pair in the hash map.
    # Time Complexity: O(1) average, O(n) worst case (where n is bucket size)
    def put(self, key, value):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                break

        else: 
            bucket.append((key, value))  
            self.size += 1

    # Retrieves the value associated with a key. Raises KeyError if key not found.
    # Time Complexity: O(1) average, O(n) worst case (where n is bucket size)
    def get(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key: return v
        raise KeyError("Key not found!")

    # Removes a key-value pair from the hash map. Raises KeyError if key not found.
    # Time Complexity: O(1) average, O(n) worst case (where n is bucket size)
    def remove(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                break

        else: raise KeyError("Key not found!")

    # Returns a list of all keys in the hash map.
    # Time Complexity: O(n) - where n is the total number of entries
    def keys(self): return [k for bucket in self.buckets for k, _ in bucket]

    # Returns a list of all values in the hash map.
    # Time Complexity: O(n) - where n is the total number of entries
    def values(self): return [v for bucket in self.buckets for _, v in bucket]

    # Returns a list of all key-value pairs (tuples) in the hash map.
    # Time Complexity: O(n) - where n is the total number of entries
    def items(self): return [(k, v) for bucket in self.buckets for k, v in bucket]

    # Computes the hash value for a given key to determine bucket index.
    # Time Complexity: O(k) - where k is the length of the key string
    def _hash_function(self, key):
        key_string = str(key)
        hash_result = 0

        for c in key_string: hash_result = ((hash_result * 31) + ord(c)) % self.capacity
        return hash_result

    # Searches for one or multiple keys in the hash map.
    # Time Complexity: O(n) - where n is the number of keys to search
    def search(self, *keys):
        if not keys: return False
        
        results = {}
        results = {key: key in self for key in keys}
        
        return results if len(keys) > 1 else results[keys[0]]

    #Checks if the hash map is empty. Returns True if empty, False otherwise.
    #Time complexity: O(1)
    def is_empty(self): return self.size == 0




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



class Graph:
    # Initialize a graph.
    # Time complexity O(1)
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()

    # returns the length of the graph
    # Time complexity: O(1)
    def __len__(self): return len(self.adj_list)

    # looping throgh the graph to return the items of the graph
    # Time complexity: O(n)
    def __iter__(self): return iter(self.adj_list)

    # represent all the graph items
    # Time comlpexity: O(n)
    def __repr__(self):
        graph_str = ""
        for node, neghbors in self.adj_list.items(): graph_str = f"{node} -> {neghbors}\n"
        return graph_str

    # Check if a node exists in the graph.
    # Time complexity O(1)
    def __contains__(self, item): return item in self.adj_list

    # Add a node to the graph.
    # Time complexity O(1)
    def add_node(self, node):
        if node not in self.adj_list: self.adj_list[node] = set()
        else: raise  ValueError("Node exists already!")

    # Remove a node and all its edges from the graph.
    # Time complexity O(V + E)
    def remove_node(self, node):
        if node not in self.adj_list: raise ValueError("Node does not exist!")

        for nighbors in self.adj_list.values(): nighbors.discard(node)
        del self.adj_list[node]

    # Add an edge between two nodes with optional weight.
    # Time complexity O(1)
    def add_edge(self, from_node, to_node, weight=None):
        if from_node not in self.adj_list: self.add_node(from_node)

        if to_node not in self.adj_list: self.add_node(to_node)

        if weight is None: 
            self.adj_list[from_node].add(to_node)

            if not self.directed: self.adj_list[to_node].add(from_node)

        else: 
            self.adj_list[from_node].add((to_node, weight))

            if not self.directed: self.adj_list[to_node].add((from_node, weight))

    # Remove an edge between two nodes.
    # Time complexity O(1)
    def remove_edge(self, from_node, to_node):
        if from_node in self.adj_list:
            if to_node in self.adj_list[from_node]: self.adj_list[from_node].remove(to_node)
            else: raise ValueError("Edge does not exist!")
            
            if not self.directed and from_node in self.adj_list[to_node]: self.adj_list[to_node].remove(from_node) 
        else: raise ValueError("Edge does not exist!")

    # Get all neighbors of a node.
    # Time complexity O(1)
    def get_nighbors(self, node): return self.adj_list.get(node, set())

    # Check if a node exists in the graph.
    # Time complexity O(1)
    def has_node(self, node): return node in self.adj_list

    # Check if an edge exists between two nodes.
    # Time complexity O(1)
    def has_edge(self, from_node, to_node):
        if from_node in self.adj_list: return to_node in self.adj_list[from_node]
        return False

    # Return a list of all nodes in the graph.
    # Time complexity O(V)
    def get_nodes(self): return list(self.adj_list.keys())

    # Return a list of all edges in the graph.
    # Time complexity O(V + E)
    def get_edges(self):
        edges = []
        for from_node, neighbors in self.adj_list.items():
            edges.extend((from_node, to_node) for to_node in neighbors)
        return edges

    # Breadth-First Search traversal starting from a node.
    # Time complexity O(V + E)
    def bfs(self, start):
        visited = set()
        queue = [start]
        order = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.get_nighbors(node)

                for neighbor in neighbors:
                    if isinstance(neighbor, tuple): neighbor = neighbor[0]

                    if neighbor not in visited: queue.append(neighbor)
        return order


    # Depth-First Search traversal starting from a node.
    # Time complexity O(V + E)
    def dfs(self, start):
        visited = set()
        stack = [start]
        order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.get_nighbors(node)

                for neighbor in sorted(neighbors, reverse=True):
                    if isinstance(neighbor, tuple): neighbor = neighbor[0]

                    if neighbor not in visited: stack.append(neighbor)
        return order

    def is_empty(self): return len(self.adj_list) == 0

    # Find shortest distances from start node to all other nodes using Dijkstra's algorithm.
    # Time complexity O((V + E) log V)
    def dijkstra(self, start):
        import heapq

        distances = {node: float("inf") for node in self.adj_list}

        distances[start] = 0
        heap = [(0, start)]

        while heap:
            curr_distance, curr_node = heapq.heappop(heap)
            if curr_distance > distances[curr_node]: continue

            neighbors = self.adj_list.get(curr_node, set())
            for neighbor in neighbors:
                if isinstance(neighbor, tuple): to, weight = neighbor
                else: to, weight = neighbor, 1
                # to, weight = neighbor if isinstance(neighbor, tuple) else to, weight = neighbor, 1

                distance = curr_distance + weight
                if distance < distances[to]:
                    distances[to] = distance
                    heapq.heappush(heap, (distance, to))
        return distances

    # Find the shortest path between two nodes using Dijkstra's algorithm.
    # Time complexity O((V + E) log V)
    def shortest_path(self, start, end):
        import heapq

        distances = {node: float("inf") for node in self.adj_list}
        prev = {node: None for node in self.adj_list}
        
        distances[start] = 0
        heap = [(0, start)]

        while heap:
            curr_distance, curr_node = heapq.heappop(heap)
            if curr_node == end: break

            if curr_distance > distances[curr_node]: continue

            neighbors = self.adj_list.get(curr_node, set())
            for neighbor in neighbors:
                if isinstance(neighbor, tuple): to, weight = neighbor
                else: to, weight = neighbor, 1
                #to, weight = neighbor if isinstance(neighbor, tuple) else to, weight = neighbor, 1

                distance = curr_distance + weight
                if distance < distances[to]:
                    distances[to] = distance
                    prev[to] = curr_node
                    heapq.heappush(heap, (distance, to))
        
        path = []
        node = end
        while node is not None:
            path.append(node)
            node = prev.get(node)
        path.reverse()
        if path[0] == start: return path
        return []

    # Convert adjacency list representation to adjacency matrix.
    # Time complexity O(V + E)
    def to_adj_matrix(self):
        nodes = self.get_nodes()
        index = {node: i for i, node in enumerate(nodes)}
        size = len(nodes)
        matrix = [[0 for _ in range(size)] for _ in range(size)]
        
        for from_node, neighbors in self.adj_list.items():
            for to_node in neighbors:
                if isinstance(to_node, tuple):
                    to, weight = to_node
                    matrix[index[from_node]][index[to]] = weight

                else: matrix[index[from_node]][index[to_node]] = 1
        return matrix


   

class DirectedGraph:
    # Initialize an empty directed graph.
    # Time complexity O(1)
    def __init__(self): self.graph = {}

    # returns the length of the graph
    # Time complexity: O(1)
    def __len__(self): return len(self.graph)

    # looping throgh the graph to return the items of the graph
    # Time complexity: O(n)
    def __iter__(self): return iter(self.graph)

    # represent all the graph items
    # Time comlpexity: O(n)
    def __repr__(self):
        graph_str = ""
        for node, neghbors in self.graph.items(): graph_str = f"{node} -> {neghbors}\n"
        return graph_str

    # Check if a node exists in the graph.
    # Time complexity O(1)
    def __contains__(self, item): return item in self.graph

    # Add a vertex to the directed graph.
    # Time complexity O(1)
    def add_vertex(self, vertex): 
        if vertex not in self.graph: self.graph[vertex] = []

    # Add a directed edge from start to end vertex.
    # Time complexity O(1)
    def add_edge(self, start, end):
        self.add_vertex(start)
        self.add_vertex(end)
        self.graph[start].append(end)

    # Remove a directed edge from start to end vertex.
    # Time complexity O(n)
    def remove_edge(self, start, end):
        if start in self.graph and end in self.graph[start]: self.graph[start].remove(end)

    # Remove a vertex and all its associated edges.
    # Time complexity O(V + E)
    def remove_vertex(self, vertex):
        if vertex in self.graph: del self.graph[vertex]

        for edges in self.graph.values(): 
            if vertex in edges: edges.remove(vertex)

    # Check if a directed edge exists from start to end.
    # Time complexity O(n)
    def has_edge(self, start, end): return start in self.graph and end in self.graph[start]

    # Return a list of vertices that vertex points to.
    # Time complexity O(1)
    def neighbors(self, vertex):
        if vertex not in self.graph: raise ValueError("Vertex does not exist")
        return self.graph[vertex]

    # Check if the directed graph is empty.
    # Time complexity O(1)
    def is_empty(self): return len(self.graph) == 0

    # Return the number of vertices in the directed graph.
    # Time complexity O(1)
    def __len__(self): return len(self.graph)

    # Return string representation of the directed graph.
    # Time complexity O(V)
    def __repr__(self): return str(self.graph)




class WeightedGraph:
    # Initializes an empty weighted graph.
    def __init__(self): self.graph = {}


    # returns the length of the graph
    # Time complexity: O(1)
    def __len__(self): return len(self.graph)

    # looping throgh the graph to return the items of the graph
    # Time complexity: O(n)
    def __iter__(self): return iter(self.graph)

    # represent all the graph items
    # Time comlpexity: O(n)
    def __repr__(self):
        graph_str = ""
        for node, neghbors in self.graph.items(): graph_str = f"{node} -> {neghbors}\n"
        return graph_str

    # Check if a node exists in the graph.
    # Time complexity O(1)
    def __contains__(self, item): return item in self.graph

    # Adds a vertex to the graph.
    def add_vertex(self, vertex):
        if vertex not in self.graph: self.graph[vertex] = []

    # Adds a directed edge with a weight.
    def add_edge(self, start, end, weight):
        self.add_vertex(start)
        self.add_vertex(end)
        self.graph[start].append((end, weight))

    # Removes an edge.
    def remove_edge(self, start, end):
        if start in self.graph: self.graph[start] = [(vertex, weight) for vertex, weight in self.graph[start] if vertex != end]

    # Checks if an edge exists.
    def has_edge(self, start, end):
        if start not in self.graph: return False

        return any(vertex == end for vertex, _ in self.graph[start])

    # Returns all neighbors and their weights.
    def neighbors(self, vertex):
        if vertex not in self.graph: raise ValueError("Vertex does not exist")

        return self.graph[vertex]

    # Returns the number of vertices.
    def __len__(self): return len(self.graph)

    # Checks if the graph is empty.
    def is_empty(self): return len(self.graph) == 0

    # Returns a string representation.
    def __repr__(self): return str(self.graph)



class UndirectedGraph:
    # Initializes an empty undirected graph.
    # Time complexity: O(1)
    def __init__(self): self.graph = {}

    # returns the length of the graph
    # Time complexity: O(1)
    def __len__(self): return len(self.graph)

    # looping throgh the graph to return the items of the graph
    # Time complexity: O(n)
    def __iter__(self): return iter(self.graph)

    # represent all the graph items
    # Time comlpexity: O(n)
    def __repr__(self):
        graph_str = ""
        for node, neghbors in self.graph.items(): graph_str = f"{node} -> {neghbors}\n"
        return graph_str

    # Check if a node exists in the graph.
    # Time complexity O(1)
    def __contains__(self, item): return item in self.graph

    # Adds a vertex to the graph.
    # Time complexity: O(1)
    def add_vertex(self, vertex):
        if vertex not in self.graph: self.graph[vertex] = []

    # Adds an undirected edge between two vertices.
    # Time complexity: O(1) average
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    # Removes an edge between two vertices.
    # Time complexity: O(n)
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]: self.graph[vertex1].remove(vertex2)

            if vertex1 in self.graph[vertex2]: self.graph[vertex2].remove(vertex1)

    # Removes a vertex and all its edges.
    # Time complexity: O(V + E)
    def remove_vertex(self, vertex):
        if vertex not in self.graph: return

        for neighbor in self.graph[vertex]: self.graph[neighbor].remove(vertex)

        del self.graph[vertex]

    # Checks if an edge exists between two vertices.
    # Time complexity: O(n)
    def has_edge(self, vertex1, vertex2):
        return (
            vertex1 in self.graph
            and vertex2 in self.graph[vertex1]
        )

    # Returns the neighbors of a vertex.
    # Time complexity: O(1)
    def neighbors(self, vertex):
        if vertex not in self.graph: raise ValueError("Vertex does not exist")

        return self.graph[vertex]

    # Returns the number of vertices.
    # Time complexity: O(1)
    def __len__(self): return len(self.graph)

    # Checks if the graph is empty.
    # Time complexity: O(1)
    def is_empty(self): return len(self.graph) == 0

    # Returns a string representation of the graph.
    # Time complexity: O(V)
    def __repr__(self): return str(self.graph)




class unweightedGraph:
    # Initializes an empty unweighted graph.
    # Time complexity: O(1)
    def __init__(self): self.graph = {}

    # returns the length of the graph
    # Time complexity: O(1)
    def __len__(self): return len(self.graph)

    # looping throgh the graph to return the items of the graph
    # Time complexity: O(n)
    def __iter__(self): return iter(self.graph)

    # represent all the graph items
    # Time comlpexity: O(n)
    def __repr__(self):
        graph_str = ""
        for node, neghbors in self.graph.items(): graph_str = f"{node} -> {neghbors}\n"
        return graph_str

    # Check if a node exists in the graph.
    # Time complexity O(1)
    def __contains__(self, item): return item in self.graph

    # Adds a vertex to the graph.
    # Time complexity: O(1) average
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    # Adds an undirected edge between two vertices.
    # Time complexity: O(1) average
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    # Removes an edge between two vertices.
    # Time complexity: O(n)
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]: self.graph[vertex1].remove(vertex2)

            if vertex1 in self.graph[vertex2]: self.graph[vertex2].remove(vertex1)

    # Checks if an edge exists.
    # Time complexity: O(n)
    def has_edge(self, vertex1, vertex2):
        return (
            vertex1 in self.graph
            and vertex2 in self.graph[vertex1]
        )

    # Returns the neighbors of a vertex.
    # Time complexity: O(1)
    def neighbors(self, vertex):
        if vertex not in self.graph:
            raise ValueError("Vertex does not exist")

        return self.graph[vertex]

    # Removes a vertex and all its edges.
    # Time complexity: O(V + E)
    def remove_vertex(self, vertex):
        if vertex not in self.graph:
            return

        for neighbor in self.graph[vertex]: self.graph[neighbor].remove(vertex)

        del self.graph[vertex]

    # Returns the number of vertices.
    # Time complexity: O(1)
    def __len__(self): return len(self.graph)

    # Checks if the graph is empty.
    # Time complexity: O(1)
    def is_empty(self): return len(self.graph) == 0

    # Returns a string representation of the graph.
    # Time complexity: O(V)
    def __repr__(self): return str(self.graph)



class TNode:
    # Initialize a Trie node with empty children dictionary and mark as not end of word.
    # Time complexity O(1)
    def __init__(self):
        self.children = dict()
        self.is_end_of_word = False


class Trie:
    # Initialize the Trie with a root node.
    # Time complexity O(1)
    def __init__(self): self.root = TNode()

    # Return the total number of words stored in the Trie.
    # Time complexity O(N) where N is the total number of nodes
    def __len__(self): return len(self.list_words())

    # iteret over the items of the trie
    # Time complexity: O()
    def __iter__(self): return iter(self.list_words())

    # Return string representation of all words in the Trie separated by spaces.
    # Time complexity O(N) where N is the total number of nodes
    def __repr__(self): return " ".join(self.list_words())

    # Check if a word exists in the Trie using the 'in' operator.
    # Time complexity O(M) where M is the length of the word
    def __contains__(self, item):
        if not item: return False # Empty string validation
        curr_node = self.root
        
        for c in item:
            if c not in curr_node.children: return False
            curr_node = curr_node.children[c]
        return curr_node.is_end_of_word  # FIX: Must check if it's a complete word

    # Insert a word into the Trie by creating nodes for each character if not exist.
    # Time complexity O(M) where M is the length of the word
    def insert(self, word: str) -> bool:
        if not word: return False # Empty string validation
        curr_node = self.root

        for c in word:
            if c not in curr_node.children: curr_node.children[c] = TNode()

            curr_node = curr_node.children[c]
        curr_node.is_end_of_word = True
        return True

    # Search for an exact word in the Trie and return True if found, False otherwise.
    # Time complexity O(M) where M is the length of the word
    def search(self, word: str) -> bool:
        if not word: return False# Empty string validation
        
        curr_node = self.root

        for c in word:
            if c not in curr_node.children: return False
            curr_node = curr_node.children[c]
        return curr_node.is_end_of_word

    # Delete a word from the Trie. Removes nodes that are no longer needed.
    # Time complexity O(M) where M is the length of the word
    def delete(self, word: str) -> bool:
        if not word: return False # Empty string validation
            
        return self._delete(self.root, word, 0)

    # Check if a given prefix exists in the Trie.
    # Time complexity O(M) where M is the length of the prefix
    def has_prefix(self, prefix: str) -> bool:
        if not prefix: return False # Empty prefix validation. Empty prefix is technically valid for all words
        curr_node = self.root
        
        for c in prefix:
            if c not in curr_node.children: return False
            curr_node = curr_node.children[c]
        return True

    # Return all words in the Trie that start with the given prefix.
    # Time complexity O(N) where N is the total number of nodes in the subtree
    def starts_with(self, prefix: str):
        if not prefix: return self.list_words() # Empty prefix returns all words
            
        words = []
        curr_node = self.root

        for c in prefix:
            if c not in curr_node.children: return words

            curr_node = curr_node.children[c]

        def _dfs(curr_node, path):
            if curr_node.is_end_of_word: words.append("".join(path))

            for c, child_node in curr_node.children.items(): _dfs(child_node, path + [c])

        _dfs(curr_node, list(prefix))
        return words
    
    # Deprecated: Use starts_with() instead. Kept for backward compatibility.
    # Time complexity O(N) where N is the total number of nodes in the subtree
    def start_with(self, prefix): return self.starts_with(prefix)

    # Return a list of all words stored in the Trie.
    # Time complexity O(N) where N is the total number of nodes
    def list_words(self):
        words = []

        def _dfs(curr_node, path):
            if curr_node.is_end_of_word: words.append("".join(path))
            
            for c, child_node in curr_node.children.items(): _dfs(child_node, path + [c])

        _dfs(self.root, [])
        return sorted(words)  # ENHANCEMENT: Return sorted list for consistency

    # Helper function for delete that recursively removes a word from the Trie.
    # Time complexity O(M) where M is the length of the word
    def _delete(self, curr_node, word, index):
        if index == len(word):
            if not curr_node.is_end_of_word: return False

            curr_node.is_end_of_word = False
            return len(curr_node.children) == 0
        
        c = word[index]
        node = curr_node.children.get(c)

        if node is None: return False

        if delete_curr_node := self._delete(node, word, index + 1):
            del curr_node.children[c]
            return len(curr_node.children) == 0 and not curr_node.is_end_of_word
        
        return False  # ENHANCEMENT: Explicit return for clarity



class BSTNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.value = None

    def __repr__(self):
        return f"({self.key}, {self.value})"


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __len__(self):
        return len((list(self._in_order_traversal(self.root))))

    def __contains__(self, item):
        curr_node = self.root

        while curr_node is not None:
            if item < curr_node.key: curr_node = curr_node.left
            elif item > curr_node.key: curr_node = curr_node.right
            else: return True
        return False

    def __iter__(self): yield from self._in_order_traversal(self.root)

    def __repr__(self):
        return str(list(self._in_order_traversal(self.root)))

    def insert(self, key, value):
        new_node = BSTNode(key)

        if self.root is None:
            self.root = new_node
            self.root.value = value

        else:
            curr_node = self.root
            while True:
                if key < curr_node.key:
                    if curr_node.left is None:
                        curr_node.left = new_node
                        curr_node.left.value = value
                        curr_node.left.parent = curr_node
                        break

                    else: curr_node = curr_node.left

                elif key > curr_node.key:
                    if curr_node.right is None:
                        curr_node.right = new_node
                        curr_node.right.value = value
                        curr_node.right.parent = curr_node
                        break

                    else: curr_node = curr_node.right

                else: 
                    curr_node.value = value
                    break

    def search(self, key):
        curr_node = self.root

        while True:
            if curr_node is None or curr_node.key == key: return curr_node

            elif key < curr_node.key:
                if curr_node.left is None: return None
                else: curr_node = curr_node.left

            else:
                if curr_node.right is None: return None
                else: curr_node = curr_node.right

    def delete(self, key):
        node = self.search(key)

        if node is None: raise ValueError("Node with this key does not exist!")

        self._delete(node)

    def traverse(self, order):
        if order.lower() == "inorder": yield from self._in_order_traversal(self.root)
        elif order.lower() == "preorder": yield from self._pre_order_traversal(self.root)
        elif order.lower() == "postorder": yield from self._post_order_traversal(self.root)
        else: raise ValueError("Unkown input!")

    def _delete(self, node):
        if node.left is None and node.right is None:
            if node.parent is None: self.root = None
            else:
                if node.parent.right  == node: node.parent.right = None
                else: node.parent.left = None
                node.parent = None

        elif node.left is None or node.right is None:
            child_node = node.left if node.left is not None else node.right

            if node.parent is None:
                child_node.parent = None
                self.root = child_node
            
            else:
                if node.parent.right == node: node.parent.right = child_node
                else: node.parent.left = child_node
                child_node.parent = node.parent
            node.parent = node.left = node.right = None

        else:
            successor = self._successor(node)

            node.key = successor.key
            node.value = successor.value

            self._delete(successor)

    def _successor(self, node):
        if node is None: raise ValueError("Cannot find successor of None!")

        if node.right is None: return None
        else: 
            curr_node = node.right

            while curr_node.left is not None: curr_node = curr_node.left
            return curr_node

    def _predecessor(self, node):
        if node is None: raise ValueError("Cannot find predecessor of None!")
        
        if node.left is None: return None
        else: 
            curr_node = node.left

            while curr_node.right is not None: curr_node = curr_node.right
            return curr_node

    def _in_order_traversal(self, node):
        if node is not None:
            yield from self._in_order_traversal(node.left)
            yield (node.key, node.value)
            yield from self._in_order_traversal(node.right)

    def _post_order_traversal(self, node):
        if node is not None:
            yield from self._post_order_traversal(node.left)
            yield from self._post_order_traversal(node.right)
            yield (node.key, node.value)

    def _pre_order_traversal(self, node):
        if node is not None:
            yield (node.key, node.value)
            yield from self._pre_order_traversal(node.left)
            yield from self._pre_order_traversal(node.right)

    def is_empty(self): return self.root is None




if __name__ == "__main__":
    print("==" * 30, "\nStack data structure:\nBeginning:\n", "__" * 30)
    stack = Stack()

    stack.push(10)
    stack.push(11)
    stack.push(12)
    stack.push(13)
    stack.push(14)

    print()
    print(stack.peek())
    print(repr(stack))
    print(stack.pop())
    print(stack)
    print(len(stack))
    print(stack.is_empty())

    for i in stack: print(i)
    
    print("==" * 30, "\nStack data structure - End\n")

    print("==" * 30, "\nQueue data structure:\nBeginning:\n", "__" * 30)
    print()
    
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(11)
    queue.enqueue(12)
    queue.enqueue(13)
    queue.enqueue(14)

    print()
    print(queue)
    print(len(queue))
    print(queue.peek())

    queue.dequeue()

    print(queue)
    print(queue.is_empty())

    for i in queue: print(i)
    
    print("==" * 30, "\nQueue data structure - End\n")


    print()
    print("==" * 30, "\nSingly Linked List with Tail:\nBeginning:\n", "__" * 30)

    SLL_tail = SinglyLinkedList()
    SLL_tail.append(10)
    SLL_tail.append(11)
    SLL_tail.append(12)
    SLL_tail.append(13)
    SLL_tail.append(14)
    SLL_tail.prepend(90)

    print(SLL_tail)

    SLL_tail.remove(13)

    SLL_tail.display()
          
    print(SLL_tail.pop(2))
    print(SLL_tail)
    print(SLL_tail.search(12))
    print(SLL_tail.get(2))

    SLL_tail.insert(20, 2)

    print(90 in SLL_tail)
    print(SLL_tail)

    for i in SLL_tail: print(i)

    print("==" * 30, "\nSingly Linked List with Tail - End\n")

    print()
    print("==" * 30, "\nSingly Linked List without Tail:\nBeginning:\n", "__" * 30)

    SLL_no_tail = SinglyLinkedListWithoutTail()
    SLL_no_tail.append(10)
    SLL_no_tail.append(11)
    SLL_no_tail.append(12)
    SLL_no_tail.append(13)
    SLL_no_tail.append(14)
    SLL_no_tail.prepend(90)

    print(SLL_no_tail)

    SLL_no_tail.remove(11)

    print(SLL_no_tail)
    print(SLL_no_tail.pop())

    SLL_no_tail.display()

    print(SLL_no_tail.search(12))
    print(SLL_no_tail.get(0))

    SLL_no_tail.insert(20, 2)

    print(90 in SLL_no_tail)
    print(SLL_no_tail)
    print(len(SLL_no_tail))

    for i in SLL_no_tail: print(i)

    print("==" * 30, "\nSingly Linked List without Tail - End\n")

    print()
    print("==" * 30, "\nDoubly Linked List:\nBeginning:\n", "__" * 30)

    DLL = DoublyLinkedList()
    DLL.append(10)
    DLL.append(11)
    DLL.append(12)
    DLL.append(13)
    DLL.append(14)
    DLL.prepend(90)

    DLL.display()

    DLL.remove(13)

    print(DLL)
    print(DLL.pop())
    print(DLL)
    print(DLL.search(12))
    print(DLL.get(0))

    DLL.insert(20, 2)

    print(90 in DLL)
    print(DLL)
    print(len(DLL))

    for i in DLL: print(i)

    print("==" * 30, "\nDoubly Linked List - End\n")

    print()
    print("==" * 30, "\nCircular Linked List:\nBeginning:\n", "__" * 30)

    CLL = CircularLinkedList()
    CLL.append(10)
    CLL.append(11)
    CLL.append(12)
    CLL.append(13)
    CLL.append(14)
    CLL.prepend(90)

    CLL.display()

    CLL.remove(14)

    print(CLL)
    print(CLL.pop())

    CLL.display()

    print(CLL.search(12))
    print(CLL.get(0))

    CLL.insert(20, 2)

    print(90 in CLL)
    print(CLL)
    print(len(CLL))

    for i in CLL: print(i)

    print("==" * 30, "\nCircular Linked List - End\n")


    print("==" * 30, "\nCirculy Doubly Linked List:\nBeginning:\n", "__" * 30)

    CDLL = CircularDoublyLinkedList()

    CDLL.append(10)
    CDLL.append(11)
    CDLL.append(12)
    CDLL.append(13)
    CDLL.append(14)
    CDLL.prepend(90)

    CDLL.display()

    CDLL.remove(14)

    print(CDLL)
    print(CDLL.pop())

    CDLL.display()

    print(CDLL.search(12))
    print(CDLL.get(0))

    CDLL.insert(20, 2)

    print(90 in CDLL)
    print(CDLL)
    print(len(CDLL))

    for i in CDLL: print(i)

    print("==" * 30, "\nCirculy Doubly Linked List - End\n")
    print()

    print("==" * 30, "\nHash Map:\nBeginning:\n", "__" * 30)
    print()
    
    import uuid

    try:
        from importlib import import_module

        plt = import_module("matplotlib.pyplot")
    except ImportError: plt = None

    HM = HashMap(100)

    for _ in range(100): HM.put(uuid.uuid4(), "some_value")

    x = []
    y = []

    for i, bucket in enumerate(HM.buckets):
        x.append(i)
        y.append(len(bucket))

    if plt is not None:
        plt.bar(x, y)
        plt.show()

    HM.put("name", ["Ismail", "Ishaq", "Mohmed", "Farida"])
    HM.put("age", [20, 19, 70, 55])
    HM.put("email", ["example@gmail.com", "example@gmail.com", "example@gmail.com", "example@gmail.com"])
    HM.put("degree", ["CyberSecurty", "null", "null", "null"])
    HM.put("ID", [155715, 155716, 155717, 155718])

    print(len(HM))
    print("Ismail" in HM)
    print(HM)
    print(HM.get("ID"))

    HM.remove("ID")

    print(HM.keys())
    print(HM.values())
    print(HM.items())
    print(HM.search("name", "age", "degree"))
    print(HM.is_empty())

    print(HM.buckets)

    for i in HM: print(i)

    print("==" * 30, "\nHash Map - End\n")
    print()

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

    print("==" * 30, "\nGraph:\nBeginning:\n", "__" * 30)
    print()

    import numpy as np

    G = Graph()

    G.add_node("A")
    G.add_node("B")
    G.add_node("C")
    G.add_node("D")
    G.add_node("E")
    G.add_node("F")
    G.add_node("G")
    G.add_node("H")
    G.add_node("I")

    G.add_edge("A", "B", 1)
    G.add_edge("A", "C", 10)
    G.add_edge("B", "C", 1)
    G.add_edge("B", "D", 1)
    G.add_edge("D", "C", 1)
    G.add_edge("A", "E", 1)
    G.add_edge("E", "F", 1)
    G.add_edge("G", "F", 1)
    G.add_edge("F", "H", 1)
    G.add_edge("H", "I", 1)
    G.add_edge("I", "G", 100)

    print(G)


    
    print(np.array(G.to_adj_matrix()))

    print("\nBFS from A: ", G.bfs("A"))
    print("DFS from A: ", G.dfs("A"))
    print("Dijkstra from A: ", G.dijkstra("A"))
    print("Shortest Path From A to C: ", G.shortest_path("A", "C"))

    print()
    print(G.get_edges())
    print()
    print(G.get_nodes())
    print()
    print(G.get_nighbors("D"))

    print(G.has_node("F"))
    print(G.has_edge("A", "B"))

    print(len(G))

    G.remove_node("A")
    print(G.get_nodes())

    # G.remove_edge("A", "B")
    print(G.get_edges())

    print("==" * 30, "\nGraph - End\n")
    print()

    

    print("==" * 30, "\nDirected Graph:\nBeginning:\n", "__" * 30)
    print()

    graph = DirectedGraph()

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "D")

    print(graph)
    print(graph.has_edge("A", "B"))
    print(graph.neighbors("A"))
    print(len(graph))

    graph.remove_edge("A", "B")
    print(graph)

    print("==" * 30, "\nDirected Graph - End\n")
    print()



    print("==" * 30, "\nunDirected Graph:\nBeginning:\n", "__" * 30)
    print()

    
    graph = UndirectedGraph()

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "D")

    print(graph)
    print(graph.has_edge("A", "B"))
    print(graph.neighbors("A"))
    print(len(graph))

    graph.remove_edge("A", "B")
    print(graph)

    print("==" * 30, "\nunDirected Graph - End\n")
    print()


    print("==" * 30, "\nWeighted Graph:\nBeginning:\n", "__" * 30)
    print()
    
    graph = WeightedGraph()

    graph.add_edge("A", "B", 5)
    graph.add_edge("A", "C", 10)
    graph.add_edge("B", "D", 3)
    graph.add_edge("C", "D", 2)

    print(graph)
    print(graph.has_edge("A", "B"))
    print(graph.neighbors("A"))
    print(len(graph))


    print("==" * 30, "\nWeighted Graph - End\n")
    print()


    print("==" * 30, "\nunWeighted Graph:\nBeginning:\n", "__" * 30)
    print()

    graph = unweightedGraph()

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "D")

    print(graph)
    print(graph.has_edge("A", "B"))
    print(graph.neighbors("A"))
    print(len(graph))

    graph.remove_edge("A", "B")
    print(graph)

    print("==" * 30, "\nunWeighted Graph - End\n")
    print()

    print("==" * 30, "\nTrie:\nBeginning:\n", "__" * 30)
    print()

    T = Trie()

    T.insert("hello")
    T.insert("henry")
    T.insert("mike")
    T.insert("minimal")
    T.insert("minimun")

    print("All words:", T.list_words())
    print("Has prefix 'mi':", T.has_prefix("mi"))
    print("Words starting with 'mi':", T.starts_with("mi"))
    print("Prefix 'hell' exists:", T.has_prefix("hell"))
    print("Word 'hell' in Trie:", "hell" in T)  # Bug fix test: should be False

    deleted = T.delete("minimal")
    print("Deleted 'minimal':", deleted)

    print("Search 'mini':", T.search("mini"))

    T.insert("mini")

    print("Total words:", len(T))
    print("Trie contents:", T)
    print("'henry' in Trie:", "henry" in T)

    for i in T: print(i)

    print("==" * 30, "\nTrie - End\n")
    print()

    print("==" * 30, "\nBinary Search Tree:\nBeginning:\n", "__" * 30)
    print()

    BST = BinarySearchTree()

    BST.insert(10, "Ismail")
    BST.insert(5, "hamada")
    BST.insert(22, "sam")
    BST.insert(12, "mo")
    BST.insert(2, "salah")
    BST.insert(9, "abdo")
    BST.insert(12, "sara")
    BST.insert(30, "isra'a")
    BST.insert(11, "widad")
    BST.insert(15, "ishaq")
    BST.insert(30, "ishaq")
    BST.insert(23, "ishaq")
    BST.insert(35, "ishaq")

    print(len(BST))
    print(BST)
    print(35 in BST)
    print(BST.search(30))

    BST.delete(23)

    print(BST.traverse("postordeR"))

    for k in BST: print(k)
    for k in BST.traverse("preorder"): print(k)