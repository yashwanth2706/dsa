class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def add_node(self, data):
        self.add_rear(data)

    def add_rear(self, data):

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current:
            prev = current
            current = current.next
        prev.next = new_node

    def add_top(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        next_node = current.next
        self.head = new_node
        new_node.next = next_node

    def peek_top(self):
        current = self.head
        self.display(current.data)

    def peek_rear(self):
        current = self.head
        while current:
            prev = current
            current = current.next
        self.display(prev.data)


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
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def pop_top(self):
        current = self.head
        next_node = current.next
        self.head = next_node

    def pop_rear(self):
        prev = None
        current = self.head
        while current:
            if current.next is None:
                prev.next = None
                return
            prev = current
            current = current.next

    def update(self, index, data):
        pass

    def delete(self, index, data):
        pass

stack = LinkedList()

queue = LinkedList()

deque = LinkedList()

ll = LinkedList()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.add_node(4)
ll.add_node(5)
ll.display()
ll.peek_top()
ll.peek_rear()
ll.reverse()
ll.display()
ll.peek_top()
ll.peek_rear()
ll.add_top(100)
ll.display()
ll.pop_top()
ll.display()
ll.peek_rear()
ll.display()
ll.pop_rear()
ll.display()
