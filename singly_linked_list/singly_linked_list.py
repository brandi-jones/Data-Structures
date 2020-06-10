class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def set_next(self, new_next):
        self.next_node = new_next

    def get_next(self):
        return self.next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value, None)

        #if list is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
        #otherwise
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    
    def remove_head(self):
        #if there is no elements in the list
        if not self.head:
            return None
        
        #if head has no next, then there is a single element in list
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None

            return head.get_value()

        #if none of the above were true, so there are multiple elements in the list
        value = self.head.get_value()
        #set the head reference to the current heads next node in the list
        self.head = self.head.get_next()

        return value

    def remove_tail(self):
        #if list is empty
        if not self.head:
            return None

        #if only 1 item in the list
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value

        #otherwise
        current = self.head
        

        #find item right before tail, which will be the new 'tail' after removal
        while current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        return value

    def contains(self, value):
        #if list is empty
        if not self.head:
            return False

        # Recursive solution
        # def search(node):
        #   if node.get_value() == value:
        #     return True
        #   if not node.get_next():
        #     return False
        #   return search(node.get_next())
        # return search(self.head)

        #get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        #check to see if we're at a valid node
        while current:
            #return True is the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            #update our current node to the current node's next node
            current = current.get_next()
        #if we've gotten here, then the target node isn't in our list
        return False
    

    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.get_value()
        # reference to our current node as we traverse the list
        current = self.head.get_next()
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()
        return max_value

    
    