class Node:
    def __init__(self, val=None):
        self.value = val
        self.next = None

class LinkedList:

    def __init__( self ):
        self.length = 0
        self.head = None

    # adding node to beginning of linkedlist.
    def ll_add( self , val ):
        new_node = Node( val )

        if( self.length == 0 ):
            self.head = new_node
            new_node.next = None
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

   # checks if node with specified value is in linkedlist.

    def ll_contains( self , val ):
       temp = self.head

       while( temp != None):
           if(temp.val == val):
               return True
           temp = temp.next

       return False

   # removes the head of the linkedlist and assigns the next node as head.
    def ll_remove_first( self ):
       if( self.length == 0):
           return False
       else:
           temp = self.head
           self.head = temp.next
           self.length -= 1
           return True

   # removes node in linkedlist at specific index.
    def ll_remove_at( self , index ):
       if(index<=self.length):
           counter = 0
           temp = self.head
           for i in range(index-1):
               temp = temp.next
           if(self.length>1):
               temp.next = temp.next.next
           else:
               temp = None
           self.length -= 1
           return True
       return False

   # gets length of linkedlist.
    def ll_length( self ):
       return self.length;
