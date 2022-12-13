class Node:
    def __init__(self,data):
        self.data = data
        self.next_node = None
    def __repr__(self):
        value = "Data stored is {}".format(self.data)
        return value
         
class Linked_List:
 #    linked_list = []

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0 


    def add_first_node(self, value):
        node = Node(value)
        self.head =  node
        self.tail = node
        self.length += 1
    
    def pre_append(self, value):
        if self.is_empty():
            self.add_first_node(value)
        else:
            node = Node(value)
            node.next_node = self.head
            self.head = node
            self.length += 1
    
    # 
    def insert(self, index, value):
        if index > self.length -1:
            return "Index not in list"
        if index > 0:
            node = Node(value)
            op_node = self.find_index(index-1)
            node.next_node = op_node.next_node
            op_node.next_node = node
            self.length += 1
        else:
            self.pre_append(value)

    def append(self, value):
        if self.is_empty():
            self.add_first_node(value)
        else:
            node = Node(value)
            self.tail.next_node = node
            self.tail = node
            self.length += 1
     
    def is_empty(self):
        return self.length == 0
     
    def list_len(self):
        return self.length
     
    def get_values(self):
        current = self.head
        linked_list = []
        while current:
            linked_list.append(current.data)
            current = current.next_node
        return linked_list

    # Iteration O(n)
    def find_index(self, index):
        current = self.head
        if index > self.length -1:
            return "Index not in list"
        else:
            for count in range(index+1):
                op_index = current
                current = current.next_node
        return op_index
     
    # Iteration O(n)
    def del_index(self, index):
        if index > self.length -1:
            return "Index not in list"
        if index > 0:
            op_node = self.find_index(index-1)
            op_node.next_node = op_node.next_node.next_node
        else:
            self.head = self.head.next_node
    
    # Iteration O(n)
    def reverse(self):
        new_list = Linked_List()
        current = self.head
        while current:
            value = current.data
            new_list.add_head(value)
            current = current.next_node
        return new_list

    # Find index O(n)
    def slice(self, startIndex, endIndex):
        if startIndex < 0 or startIndex > self.length -1 or endIndex > self.length:
            raise Exception("Index out of range")
        resultList = Linked_List()
        currentNode = self.find_index(startIndex)
        for i in range(startIndex,endIndex):
            resultList.append(currentNode.data)
            currentNode = currentNode.next_node
        return resultList
            
    """
    Components
        Iterate O(log(n))
        Split O(n)^2
        Merge O(n)
        O(log(n) n^3)
    """
    def merge_sort_descending(self):
        result_list = Linked_List()
        if self.length <= 1:
            return self
        left_half, right_half = split(self)
        left = left_half.merge_sort_descending()
        right = right_half.merge_sort_descending()
        return merge_descending(left, right)
    
    """
    Components
        Iterate O(log(n))
        Split O(n)^2
        Merge O(n)
        O(log(n) n^3)
    """
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
    Slice O(n)
    Slice O(n)
    O(n)^2
"""
def split(sourceList):
    midpoint = sourceList.length//2
    left = sourceList.slice(0,midpoint)
    right = sourceList.slice(midpoint,sourceList.length)
    return (left, right)

"""
Components
    Iterate O(n)
    Append O(1) - Does not contribute
    O(n)
"""
def merge_descending(left, right):
    result = Linked_List()
    currentL = left.head
    currentR = right.head
    while currentL and currentR:
        valueL = currentL.data
        valueR = currentR.data
        if valueL > valueR:
            result.append(valueL)
            currentL = currentL.next_node  
        else:
            result.append(valueR)
            currentR = currentR.next_node
    while currentL and not currentR:
        valueL = currentL.data
        result.append(valueL)
        currentL = currentL.next_node
    while currentR and not currentL:
        valueR = currentR.data
        result.append(valueR)
        currentR = currentR.next_node
    return result

"""
Components
    Iterate O(n)
    Append O(1) - Does not contribute
    O(n)
"""

def merge_ascending(left, right):
    result = Linked_List()
    currentL = left.head
    currentR = right.head
    while currentL and currentR:
        valueL = currentL.data
        valueR = currentR.data
        if valueL < valueR:
            result.append(valueL)
            currentL = currentL.next_node  
        else:
            result.append(valueR)
            currentR = currentR.next_node
    while currentL and not currentR:
        valueL = currentL.data
        result.append(valueL)
        currentL = currentL.next_node
    while currentR and not currentL:
        valueR = currentR.data
        result.append(valueR)
        currentR = currentR.next_node
    return result

def create_sample(data):
    result = Linked_List()
    for element in data:
        result.append(element)
    return result



"""


if __name__ == "__main__":
    array = utilities.generate_list(10)
    list = create_sample(array)
    begining = time.perf_counter_ns()
    test = list.merge_sort_ascending()
    end = time.perf_counter_ns()
    print(test.get_values())
    print((end - begining)/1e6)

"""