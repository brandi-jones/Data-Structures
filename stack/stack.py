"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0

#         #for array as storage structure
#         self.storage = []

#     def __len__(self):
#         #for array as storage structure
#         return len(self.storage)

#     def push(self, value):
#         #for array as storage 
#         self.storage.append(value)
#         return

#     def pop(self):
#         #for array as storage structure
#         #check that array is not empty
#         if self.storage: 
#             removedItem = self.storage.pop(len(self.storage) - 1)
#             return removedItem
#         #otherwise, if array is empty
#         return





import sys
#sys.path.insert(1, '../singly_linked_list')
sys.path.append('./singly_linked_list')
from singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        self.size = 0

        #for LL as storage structure
        self.storage = LinkedList()

    def __len__(self):
        #for LL as storage structure
        return self.size
      

    def push(self, value):
        #for LL as storage 
        self.storage.add_to_tail(value)
        self.size = self.size +1
        return

    def pop(self):
        #for LL as storage structure
        if self.size > 0:
            self.size = self.size - 1

        removedItem = self.storage.remove_tail()
        return removedItem

    def __iter__(self):
        return self

    def __next__(self):
        #every next iteration, return self.pop, which in turn iterates in the order of what nodes would be in line to be popped off the stack, not in order from head to tail. 
        #in this case, it also removes items from the stack itself since we are calling self.pop. We normally probably wouldn't want this behavior, however since this is implemented
        #solely for stretch goals in implementing a queue from stack data structures, this works perfectly.
        if self.size > 0:
           return self.pop()
        else:
            raise StopIteration

        