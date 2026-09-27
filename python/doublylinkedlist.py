class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def add_rear(self, data):

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def add_top(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def peek_top(self):
        if self.head is None:
            self.display('stack empty')
            return
        current = self.head
        self.display(current.data)

    def peek_rear(self):
        if self.head is None:
            self.display('stack empty')
            return
        current = self.tail
        self.display(current.data)


    def display(self, default=None):

        if default is not None:
            print(default)
            return

        current = self.head
        while current is not None:
            print(f"{current.data}->", end='')
            current = current.next
        print()

    def reverse(self):
        if self.head is None:
            self.display('stack empty')
            return
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def pop_top(self):
        if self.head is None:
            self.display('stack empty')
            return
        current = self.head
        next_node = current.next
        self.head = next_node

    def pop_rear(self):
        if self.head is None:
            self.display('stack empty')
            return

        if self.head.next is None:
            self.head = None
            self.tail = None
            return

        self.tail = self.tail.prev
        self.tail.next = None

    def update(self, index, data):
        pass

    def delete(self, index, data):
        pass

stack = DoublyLinkedList()
stack.add_top(1)
stack.add_top(2)
stack.add_top(3)
stack.add_top(4)
stack.display()
stack.pop_rear()
stack.display()
stack.peek_rear()
stack.pop_rear()
stack.display()
stack.peek_rear()
stack.pop_rear()
stack.display()
#stack.display("STACK-START")
#stack.add_rear(1)
#stack.add_rear(2)
#stack.add_rear(3)
#stack.add_rear(4)
#stack.add_rear(5)
#stack.display()
#stack.peek_top()
#stack.pop_top()
#stack.display()
#stack.add_top(10)
#stack.add_top(20)
#stack.add_top(30)
#stack.display()
#stack.display("STACK-END")
#
#queue = LinkedList()
#
#deque = LinkedList()
#
#ll = LinkedList()
#ll.add_top(1)
#ll.add_top(2)
#ll.add_top(3)
#ll.add_top(4)
#ll.add_top(5)
#ll.display()
#ll.peek_top()
#ll.peek_rear()
#ll.reverse()
#ll.display()
#ll.peek_top()
#ll.peek_rear()
#ll.add_top(100)
#ll.display()
#ll.pop_top()
#ll.display()
#ll.peek_rear()
#ll.display()
#ll.pop_rear()
#ll.display()
