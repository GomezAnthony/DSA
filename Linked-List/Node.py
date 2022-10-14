class Node:
    def __init__(self,data):
        self.data = data # This is the first node of the linked list
        self.next = None # This the is the empty linked list

class LinkedList:
    def __init__(self):
        self.head = None # This is an empty linked list where head of the list points to None which means its the beginning.

    def printList(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def insertAtBeginning(self, data):
        new_node = Node(data) # Create a new node with the given data
        if self.head == None: # Check if to see if the node is empty
            self.head = new_node # This will assign the new node to the head of the linked list
        else:
            new_node.next = self.head # This will point to the current head of the list(The New node to equal to the head)
            self.head = new_node # This will move the head to the new node of the list

    def appendEnd(self, data):
        new_node = Node(data) # Create a new node
        if self.head == None: # Check if head of the list doesnt have a components or points to anything.
            self.head = new_node # Then set the head pointer to the new node created.
        else:
            last_node = self.head # This will start the node
            while last_node.next != None: # While the node is not None
                last_node = last_node.next # Then point the last_node points to the next
            last_node.next = new_node # Once the head is pointing to None, then insert the node

llist = LinkedList()
llist.appendEnd('A')
llist.appendEnd('B')
llist.appendEnd('C')
llist.appendEnd('D')

llist.insertAtBeginning("E")

llist.printList()
