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
        self.order = DoublyLinkedList()
        self.storage = {}
        
        # a = {"name": "george", "age": 26}
        # a["name"] = george
    """

    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    #hash table and doubly linked list.. this allows us to access, for example, the middle variable by looking it up instead of iterating 
    def get(self, key):
        #get key from dictionary if the key is in self.storage         
        if key in self.storage:
            get_node = self.storage[key]
            #get_node = value
            self.order.move_to_end(get_node)
            # print(get_node.value, get_node.value[key], self.storage["item2"].value)
            return get_node.value[key]

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
        if key in self.storage:
            #self.storage[key]
            node = self.storage[key]
            node.value = {key: value}
            # if the key is a duplicate then override value and move to most recently used  
            self.order.move_to_end(node)    
        
        elif self.order.length >= self.limit:
            value_removed = self.order.remove_from_head() 
            for key1, value1 in value_removed.items():
                
                value_removed_key = key1
            
            self.storage.pop(value_removed_key)        
            self.order.add_to_tail({key: value})
            self.storage[key] = self.order.tail
        
        else: 
            self.order.add_to_tail({key: value})
            self.storage[key] = self.order.tail
            #if overcapacity, then remove from head (oldest)


       

        

        