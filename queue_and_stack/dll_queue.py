# import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList



class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        #very good for DLL because in queue, we're removing and adding from opposite sides 
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # should add an item to the back of the queue
        self.storage.add_to_tail(value)
        self.size += 1
    

    def dequeue(self):
        # should remove and return an item from the front of the queue.
        if self.size == 0:
            return None

        else:
            self.size -= 1
            return self.storage.remove_from_head()
          
    def len(self):
        # returns the number of items in the queue.
        return self.size
