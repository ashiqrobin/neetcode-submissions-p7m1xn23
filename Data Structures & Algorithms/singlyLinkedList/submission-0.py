class Node:
    def __init__(self, data, next_node=None):
        self.value = data
        self.next = next_node


class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        count = 0
        current = self.head
        while current:
            if count == index:
                return current.value
            count +=1
            current = current.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        if not self.head.next:
            self.tail = new_node
        

    def insertTail(self, val: int) -> None:
        new_node = Node(val)

        if not self.head:
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node
        

    def remove(self, index: int) -> bool:
        if not self.head:
            return False

        prev = None
        count = 0
        current = self.head

        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return True

        while current:
            if count == index:
                if current.next:
                    prev.next = current.next
                else:
                    self.tail = prev
                    prev.next = None
                return True

            prev = current
            current = current.next
            count += 1

        return False
        


    def getValues(self) -> List[int]:
        val = []
        current = self.head
        while current:
            val.append(current.value)
            current = current.next
        return val
        
