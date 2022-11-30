class Node:
     def __init__(self,data):
         self.data = data
         self.next_node = None
     def __repr__(self):
         values = "Data stored is {}".format(self.data)
         return values
         
class Linked_List:
 #    linked_list = []
     def __init__(self):
         self.head = None
     def add_head(self, value):
         node = Node(value)
         node.next_node = self.head
         self.head = node
     # Ineficient quadratic time make linear
     def add_index(self, index, value):
         if index > self.list_len() -1:
             return "Index not in list"
         if index > 0:
             op_node = self.find_index(index-1)
             node = Node(value)
             node.next_node = op_node.next_node
             op_node.next_node = node
         else:
             self.add_head(value)
     def add_tail(self, value):
         node = Node(value)
         if self.is_empty():
             self.add_head(value)
         else:
             op_node = self.find_tail()
             op_node.next_node = node
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
         current = self.head
         count = 0
         while current:
             count += 1
             current = current.next_node
         return count
     def get_values(self):
         current = self.head
         linked_list = []
         while current:
             linked_list.append(current.data)
             current = current.next_node
         return linked_list
     #ineficient quadratic time
     def find_index(self, index):
         current = self.head
         if index > self.list_len() -1:
             return "Index not in list"
         else:
             for count in range(index+1):
                 op_index = current
                 current = current.next_node
         return op_index
     #Ineficient quadratic time
     def del_index(self, index):
         if index > self.list_len() -1:
             return "Index not in list"
         if index > 0:
             op_node = self.find_index(index-1)
             op_node.next_node = op_node.next_node.next_node
         else:
             self.head = self.head.next_node
     def reverse(self):
         new_list = Linked_List()
         current = self.head
         while current:
             value = current.data
             new_list.add_head(value)
             current = current.next_node
         return new_list

