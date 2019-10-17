from doubly_linked_list import DoublyLinkedList

#combination of hash table and queue



class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        
        self.limit = limit
        self.size = 0        
        self.order = DoublyLinkedList()
        self.storage = dict()
        
    """


    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    #hash table and doubly linked list.. this allows us to access, for example, the middle variable by looking it up instead of iterating 
    def get(self, key):
        #get the item or handle none
        #move to front 
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_end(node)
            return node.value[1] 
            #[1] because node.value returns a tuple.. and [1] is the secodn item in tuple, which is value
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    #So it should make a node, add it to the linked list, 
    # then add a key/value pair to your dict for O(1) lookup time. 
    # the node only needs the value to be created, the key is simply for look up

    #linkedlist  ..... 
    #dictionary .... every value of a dictionary is a node... 
    #value of the node is a tuple ()
    # node.value = ("Bob", 88)
    # node.value = (Key, Value)
    # node.value[1] = value
    # dictionary = {"bob" : node}

    def set(self, key, value):
        #check if key already exists in the cache
        if key in self.storage:
            node = self.storage[key] #looking in dictionary for what we stored under key
            node.value = (key, value)
            self.order.move_to_end(node)
            return

        #check if we're at max capacity.... then remove oldest entry in the cache 
        if self.size == self.limit:
            del self.storage[self.order.head.value[0]] #delete oldest item in cahce from Dictionary
            self.order.remove_from_head() #delete oldest item in cahce from DLL
            self.size -= 1
        
        #add a given key-value pair to the cache
        #add to DLL at the tail
        self.order.add_to_tail((key, value))
        #add to dictionary 
        self.storage[key] = self.order.tail
        self.size += 1


        #whatever we add or change should be most recently used 


       

        

        