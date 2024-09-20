class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        # O(n)
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
    
    def insert(self,index,data):
        # O(n)
        node = Node(data)
        if index<0:
            raise ValueError("index cannot be negative!!")
        if index == 0:
            node.next = self.head
            self.head = node
            return
        current = self.head
        for _ in range(index -1):
            if not current.next:
                raise IndexError("Index out of bound!!")
            current = current.next
        node.next = current.next
        current.next = node
    
    def delete(self,index):
        # O(n)
        if index<0:
            raise ValueError("index cannot be negative!!")
        if index ==0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index-1):
            if not current.next:
                raise IndexError("Index out of Range!!")
            current = current.next
        current.next = current.next.next        
    
    def search(self,data):
        # O(n)
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def reverse(self):
        def reverse_func(head):
            # recursive
            if not head or not head.next:
                return head
            
            x = reverse_func(head.next) # pointer at last node

            # update the link between two pointers
            head.next.next = head
            head.next = None

            return x
        self.head = reverse_func(self.head)
        
    
    def print_list():
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
    
    def func(self):
        pass