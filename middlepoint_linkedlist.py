# Finding the Middle of Linked List

def findMid(head):
    fastPtr = Linked_List()    # Take two different pointer.
    slowPtr = Linked_List()    # fastPtr will move double the slowPtr each time till it reaches end.
    fastPtr.head = head        # As soon as fastPtr reaches end, slowPtr will be on the middle element.
    slowPtr.head = head
    if fastPtr.head is None :
        return head
    while fastPtr.head.next is not None :
        fastPtr.head = fastPtr.head.next
        slowPtr.head = slowPtr.head.next
        if fastPtr.head.next is not None :
            fastPtr.head = fastPtr.head.next
            
    return slowPtr.head
    
    
#  Node Class 
class node : 
  def __init__(self,val) :
    self.data = val
    self. next = None
#  Linked List Class
class Linked_List:
  def __init__(self):
    self.head = None
    
   def insert(self,val):
    if self.head == None :
      self.head = node(val)
    else :
      new_node = node(val)
      temp = self.head
      while(temp.next):
        temp = temp.next
       temp.next = new_node
      
def createList(arr,n) :
  lis = Linked_List()
  for i in range(n):
    lis.insert(arr[i])
    return lis.head 

if __name__ =='__main__':
  t =int(input())
  for i in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    head = createList(arr,n)
    print(findMid(head).data)
