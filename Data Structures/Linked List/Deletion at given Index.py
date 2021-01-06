# Deletion of a Number at given Index in a Singly Linked List

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0
    
    # I'm adding new elements in the back keeping the head pointer in front and 
    # tail pointer with the newly added element
    def push(self, data):
        new_node = Node(data)

        if(self.counter == 0):
            self.head = new_node
            self.tail = self.head
            self.counter += 1
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, index):
        self.counter = 0
        temp = self.head

        # If entered index is 0
        if(index == 0):
            print("Number removed from Index", index,"!")
            self.head = temp.next
            temp = None
            return

        # If entered index is in middle
        while(temp):
            if(self.counter == index):
                print("Number removed from Index", index,"!")
                prev.next = temp.next
                temp = None
                return

            self.counter += 1
            prev = temp
            temp = temp.next
        
        # If Entered Index is greater then the length of linked list
        if(self.counter < index):
            print("Oops! Linked List is of Smaller Size...")

    
    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.val)
            temp = temp.next


linked_list_length = int(input("Enter Linked List Length: "))

llist = LinkedList()

for i in range(linked_list_length):
    llist.push(int(input("Enter Number: ")))

index = int(input("Enter Index for which you want to delete the value: "))
llist.delete(index)

llist.printLinkedList()