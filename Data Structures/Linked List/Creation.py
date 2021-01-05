# Creation of Linked List

class Node:
    def __init__(self, data):
        self. data = data
        self. next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.head = Node(int(input("Enter Number: ")))
    second = Node(int(input("Enter Number: ")))
    third = Node(int(input("Enter Number: ")))

    linked_list.head.next = second
    second.next = third
    third.next = None

    linked_list.printLinkedList()