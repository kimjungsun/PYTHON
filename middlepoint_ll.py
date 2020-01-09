
def findMid(head):
    val1 = Linked_List()
    val2 = Linked_List()
    val1.head = head
    val2.head = head
    if val1.head is None :
        return head
    while val1.head.next is not None :
        val1.head = val1.head.next
        val2.head = val2.head.next
        if val1.head.next is not None :
            val1.head = val1.head.next
            
    return val2.head
    
    
