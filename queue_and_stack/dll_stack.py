from doubly_linked_list import DoublyLinkedList
# import sys
# sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        #good insert and remove speeds without having to worry about our space
        self.storage = DoublyLinkedList()

    def push(self, value):
        #adding something goes to the top and gets resolved first 
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        #take away the last value 
        if self.size == 0:
            return None

        else:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size


