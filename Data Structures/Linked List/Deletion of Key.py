# Deletion of Key in Singly Linked List
# Here Key means a particular value to delete


class Node:
    # Constructor for Node Creation
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    # Method/Function for adding new Element/Data in the beginning
    def push(self, num_to_add):
        new_node = Node(num_to_add)
        new_node.next = self.head
        self.head = new_node

    
    # Method/Function for the deletion of a Key/Data/Element
    def delete(self, num_to_delete):
        temp = self.head

        # If the Key is Present in starting i.e the first element
        if(temp.data == num_to_delete):
            self.head = temp.next
            temp = None
            print("Number deletion SUCCESSFUL!")
            return
        
        # If the Key is Present Linked List in other then starting position
        while(temp is not None):
            if(temp.data == num_to_delete):
                prev.next = temp.next
                temp = None
                print("Number deletion SUCCESSFUL!")
                return

            prev = temp
            temp = temp.next
        
        # If Key is not present in Linked List... Checking via upper while loop...
        # After the loop if temp becomes None that means all the numbers are checked
        # and key is not found
        if(temp is None):
            print("Number to be deleted not present in this Linked List!")
            return


    # Method/Function to print the Linked List
    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next



linked_list_length = int(input("Enter Linked List Length: "))
llist = LinkedList()

for i in range(linked_list_length):
    llist.push(int(input("Enter Number: ")))

num_to_delete = int(input("Enter Number to Delete: "))

llist.delete(num_to_delete)

llist.printLinkedList()