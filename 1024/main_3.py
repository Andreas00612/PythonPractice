###102403####
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        return

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_list_item(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
            self.tail = item
        else:
            self.tail.next = item
            item.prev = self.tail
            self.tail = item
        return
    def reverse(self,current):
        while current:
            print(current.data," ")
            current = current.prev
    def traverse(self):
        current = self.head
        while current:
            while current.data % 2 != 0:
                current = current.next
                if current.next is None and current.data % 2 != 0:
                    self.reverse(current)
                    return
            out = current.prev
            current.prev = None
            while out:
                print(out.data," ")
                out = out.prev
            print(current.data, " ")
            if current.next:
                current = current.next
                current.prev = None
            else:
                return

with open('input.pkl','rb') as inp:
    linkedlist = pickle.load(inp)
    linkedlist.traverse()
