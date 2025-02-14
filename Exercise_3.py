# Node class  
class Node:  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data
        self.next = None
class LinkedList: 
    def __init__(self):
        self.head = None
    def push(self, new_data): 
        temp = self.head
        if self.head == None:
            self.head = Node(new_data)
        else:
            while temp.next:
                temp = temp.next
            temp.next = Node(new_data)
            
    def printMiddle(self): 
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)
        
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 