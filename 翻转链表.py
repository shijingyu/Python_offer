class Node(object):
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node




def Reverse(head, last=None):
    
    if head.next is not None:
        rev = Reverse(head.next, head)
        head.next = last
        return rev
        
    head.next = last
    return head