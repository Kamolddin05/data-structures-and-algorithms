''' 06/10/2025 '''

# # m1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.hade = None

    def append(self, data):
        new_Node = Node(data)
        if not self.hade:
            self.hade = new_Node
            return
        cur = self.hade
        while cur.next:
            cur = cur.next
        cur.next = new_Node

    def display(self):
        cur = self.hade
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

ll = LinkedList()
ll.append(5)       
ll.display()



