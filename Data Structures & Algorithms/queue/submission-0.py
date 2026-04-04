class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prv = None



class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0


    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        else:
            return False     
        

    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.prv = self.tail
            self.tail.next = new_node
            self.tail = new_node
            new_node.next=None

        self.count += 1    

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prv=new_node
            self.head = new_node

        self.count += 1
       

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        else:
            if self.head == self.tail:
                node = self.head
                self.head = self.tail = None
            else:
                node = self.tail
                prv_node = self.tail.prv
                self.tail = prv_node
            self.count -= 1
            return node.value
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        else:
            if self.head == self.tail:
                node = self.head
                self.head=self.tail= None
            else:
                node = self.head
                next_node=self.head.next
                self.head = next_node
                self.head.prv = None
            
            self.count -=1
            return node.value

        
