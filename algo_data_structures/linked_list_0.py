import time
import utilities

class Node:
    def __init__(self,data):
        self.data = data
        self.next_node = None
    def __repr__(self):
        value = "Data stored is {}".format(self.data)
        return value
         
class Linked_List:
 #    linked_list = []
    length = 0 
    def __init__(self):
        self.head = None
     
    def add_head(self, value):
        node = Node(value)
        node.next_node = self.head
        self.head = node
        self.length += 1
    
    # linear due to search index
    def add_index(self, index, value):
        if index > self.length -1:
            return "Index not in list"
        if index > 0:
            op_node = self.find_index(index-1)
            node = Node(value)
            node.next_node = op_node.next_node
            op_node.next_node = node
            self.length += 1
        else:
            self.add_head(value)


    #linear due to find tail
    def add_tail(self, value):
        node = Node(value)
        if self.is_empty():
            self.add_head(value)
        else:
            op_node = self.find_tail()
            op_node.next_node = node
            self.length += 1
     
     #linear
    def find_tail(self):
        current = self.head
        if self.is_empty():
            return None
        while current:
            result = current
            current = current.next_node
        return result
     
    def is_empty(self):
        return self.head == None
     
    def list_len(self):
        return self.length
     
    # Linear
    def get_values(self):
        current = self.head
        linked_list = []
        while current:
            linked_list.append(current.data)
            current = current.next_node
        return linked_list
    
    #Linear due to iteration
    def find_index(self, index):
        current = self.head
        if index > self.length -1:
            return "Index not in list"
        else:
            for count in range(index+1):
                op_index = current
                current = current.next_node
        return op_index
    
    # linear due to find index
    def del_index(self, index):
        if index > self.length -1:
            return "Index not in list"
        if index > 0:
            op_node = self.find_index(index-1)
            op_node.next_node = op_node.next_node.next_node
        else:
            self.head = self.head.next_node
    
    # linear due to traversing
    def reverse(self):
        new_list = Linked_List()
        current = self.head
        while current:
            value = current.data
            new_list.add_head(value)
            current = current.next_node
        return new_list
    
    """
    Components 
    - Find Index O(n)
    - Add Tail O(n)
    O(n)^2
    """
    def slice(self, startIndex, endIndex):
        if startIndex < 0 or startIndex > self.length -1 or endIndex > self.length:
            raise Exception("Index out of range")
        resultList = Linked_List()
        currentNode = self.find_index(startIndex)
        for i in range(startIndex,endIndex):
            resultList.add_tail(currentNode.data)
            currentNode = currentNode.next_node
        return resultList

    
    """
    Components 
    - Iterate Log O(log(n))
    - Split O(n)^4
    - Merge O(n)^2
    O(log(n) (n)^6)
    """  
    def merge_sort_descending(self):
        result_list = Linked_List()
        if self.length <= 1:
            return self
        left_half, right_half = split(self)
        left = left_half.merge_sort_descending()
        right = right_half.merge_sort_descending()
        return merge_descending(left, right)
    
    def merge_sort_ascending(self):
        result_list = Linked_List()
        if self.length <= 1:
            return self
        left_half, right_half = split(self)
        left = left_half.merge_sort_ascending()
        right = right_half.merge_sort_ascending()
        return merge_ascending(left, right)

## Utility functions

"""
Components
    Slice O(n)^2
    Slice O(n)^2
    O(n)^4
"""
def split(sourceList):
    midpoint = sourceList.length//2
    left = sourceList.slice(0,midpoint)
    right = sourceList.slice(midpoint,sourceList.length)
    return (left, right)



"""
Components
    Iterate O(n)
    Add Tail O(n)
    O(n)^2
"""

def merge_descending(left, right):
    result = Linked_List()
    currentL = left.head
    currentR = right.head
    while currentL and currentR:
        valueL = currentL.data
        valueR = currentR.data
        if valueL > valueR:
            result.add_tail(valueL)
            currentL = currentL.next_node  
        else:
            result.add_tail(valueR)
            currentR = currentR.next_node
    while currentL and not currentR:
        valueL = currentL.data
        result.add_tail(valueL)
        currentL = currentL.next_node
    while currentR and not currentL:
        valueR = currentR.data
        result.add_tail(valueR)
        currentR = currentR.next_node
    return result

"""
Components
    Iterate O(n)
    Add Tail O(n)
    O(n)^2
"""
def merge_ascending(left, right):
    result = Linked_List()
    currentL = left.head
    currentR = right.head
    while currentL and currentR:
        valueL = currentL.data
        valueR = currentR.data
        if valueL < valueR:
            result.add_tail(valueL)
            currentL = currentL.next_node  
        else:
            result.add_tail(valueR)
            currentR = currentR.next_node
    while currentL and not currentR:
        valueL = currentL.data
        result.add_tail(valueL)
        currentL = currentL.next_node
    while currentR and not currentL:
        valueR = currentR.data
        result.add_tail(valueR)
        currentR = currentR.next_node
    return result

def create_sample(data):
    result = Linked_List()
    for element in data:
        result.add_tail(element)
    return result



"""
-- Refactor functions with quadratic runtime. // Done
-- Understand if the reverse algorithm works with any single linked lists
-- implement merge sort
"""

if __name__ == "__main__":
    list = create_sample(utilities.generate_list(10000))
    begining = time.perf_counter_ns()
    test = list.merge_sort_ascending()
    end = time.perf_counter_ns()
    #print(test.get_values())
    print((end - begining)/1e6)
    
