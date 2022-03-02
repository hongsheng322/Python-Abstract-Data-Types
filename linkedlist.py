class node():
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList():
    def __init__(self):
        self.head = None
    def InsertAtHead(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    def Search(self, value):
        temp= self.head
        while temp is not None:
            if temp.data is value:
                print("value found")
                return temp
            else:
                temp = temp.next
        print("value not found")
    def delete(self, value):
        temp = self.head
        prev = None
        while temp is not None:
            if temp.data is not value:
                prev = temp
                temp = temp.next
            else:
                if prev is None:
                    self.head = temp.next
                    del temp
                else:
                    prev.next = temp.next
                    del temp
                return
    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

def MergeList(list1, list2):
    dummynode = node(0)
    tail = dummynode

    while True:
        if list1 is None:
            tail.next = list2
            break
        if list2 is None:
            tail.next = list1
            break
        
        if list1.data > list2.data:
            tail.next = list2
            list2 = list2.next
        else:
            tail.next = list1
            list1 = list1.next

        tail = tail.next
    return dummynode.next
        


test = SingleLinkedList()
test.InsertAtHead(node(8))
test.InsertAtHead(node(7))
test.InsertAtHead(node(5))
test2 = SingleLinkedList()
test2.InsertAtHead(node(10))
test2.InsertAtHead(node(6))
test2.InsertAtHead(node(4))
temp = SingleLinkedList()
temp.head = MergeList(test.head, test2.head)
temp.printlist()

