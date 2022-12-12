#import algo_data_structures.linked_list_0 as linked_0
import algo_data_structures.linked_list_1 as linked_1
import algo_data_structures.linked_list_2 as linked_2
import algo_data_structures.utilities as utilities

def check_ascending(linkedList):
    result = True
    if linkedList.length <= 1:
        return result
    else:
        current = linkedList.head
        for x in range(0,linkedList.length - 1):
            if current.data > current.next_node.data:
                result = False
            current = current.next_node
    return result

def check_descending(linkedList):
    result = True
    if linkedList.length <= 1:
        return result
    else:
        current = linkedList.head
        for x in range(0,linkedList.length - 1):
            if current.data < current.next_node.data:
                result = False
            current = current.next_node
    return result


def test_1():      
    array = utilities.generate_list(10)
    list = linked_1.create_sample(array)
    ascending_test = list.merge_sort_ascending()
    descending_test = list.merge_sort_descending()
    assert list.length == ascending_test.length 
    assert list.length == descending_test.length
    assert check_ascending(ascending_test) == True
    assert check_descending(descending_test)


def test_2():      
    array = utilities.generate_list(100)
    list_a = linked_2.create_sample(array)
    list_d = linked_2.create_sample(array)
    list_length = list_a.length
    ascending_test = list_a.merge_sort_ascending()
    descending_test = list_d.merge_sort_descending()
    assert list_length == ascending_test.length 
    assert list_length == descending_test.length
    assert check_ascending(ascending_test) 
    assert check_descending(descending_test)


