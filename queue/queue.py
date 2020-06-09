"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

#for array
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size+=1

#     def dequeue(self):
#         if self.storage:
#             removedValue = self.storage.pop(0)
#             self.size-=1
#             return removedValue
#         return
        



import sys
sys.path.append('./singly_linked_list')
from singly_linked_list import LinkedList

#for LL
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.add_to_tail(value)
#         self.size = self.size +1

#     def dequeue(self):
#         if self.size > 0:
#             self.size = self.size - 1

#         removedItem = self.storage.remove_head()
#         return removedItem
        



import sys
sys.path.append('./stack')
from stack import Stack


#using stack as storage structure
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = Stack()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.push(value)
        self.size = self.size +1

    # method 1 - implementing changes to __iter__ and __next__ of the stack class
    # def dequeue(self):
    #     if self.storage:

    #         #make temp stack to reverse items in main stack in self.storage
    #         #see notes in the stack.py about the implementation of the __next__() method and how this code below inturn creates a reversed stack of the original we iterate through
    #         reversedStack = Stack()
    #         for i in self.storage:
    #             reversedStack.push(i)

    #         #pop last item off the reversedstack (first original item in the queue in self.storage)
    #         removedItem = reversedStack.pop()

    #         #reverse the stack back, to original order
    #         newStack = Stack()
    #         for i in reversedStack:
    #             newStack.push(i)
            
    #         #set self.storage to newStack with proper ordering and removed first node
    #         self.storage = newStack

    #         #update size
    #         self.size = self.size - 1

    #         return removedItem
        
    #     return
        

    # method 2 - 2 stacks
    def dequeue(self):
        if self.storage:
            stack1 = self.storage
            stack2 = Stack()

            while stack1:
                stack2.push(stack1.pop()) #pop items from stack1 (copy of original stack), and then push the items popped into stack2, therefore reversing the original stack
            
            removedValue = stack2.pop() #pop from stack2, to remove the correct node (that was in the first place of the queue to begin with)

            while stack2:
                stack1.push(stack2.pop()) #pop items from stack2, which now holds the reversed queue we desire

            self.storage = stack1 #reset self.storage to the proper stack

            #update size
            self.size-=1

            return removedValue
            
        return