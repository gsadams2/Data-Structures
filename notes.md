Depth First Traversal - uses a stack 
-create a stack - use dll_stack 
-push start node to stack 
-while stack > 0: #because if stack is empty, it means we visited every item
    pop top item in stack
    "do the thing!"
    if left
        add left
    if right
        add right
    


Breadth First Traversal - uses a queue
    Rules:
        go left and right, find new paths and then go back until you found everything at each layer 
    
    psuedocode:
        make a queue
        add start to queue
        while queue not empty:
            pop front item 
            "do the thing!"
            if left
                add left
            if right 
                add right





