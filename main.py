from Stack.stack import Stack
from Queue.queue import Queue
from LinkedLists.allLinkedLists import LinkedLists, SinglyLinkedList, SinglyLinkedListWithoutTail, DoublyLinkedList, CircularLinkedList, CircularDoublyLinkedList
from Hashmap.hashmap import HashMap
from Heaps.heaps import minHeap, maxHeap
from Graphs.graphs import Graph, DirectedGraph, UndirectedGraph, WeightedGraph, unweightedGraph
from Trie.trie import Trie
from BinarySearchTree.BinaryTree import BinarySearchTree

def main():
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
    print()

    BST.delete(10)

    print(BST.traverse("postordeR"))

    for k in BST: print(k)
    for k in BST.traverse("preorder"): print(k)

    print()
    print("==" * 30, "\nBinary Search Tree - End\n")

if __name__ == "__main__":
    main()