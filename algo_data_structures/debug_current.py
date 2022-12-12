import time
import utilities
import linked_list_2 as linked_2

def debug_2_ascending(n):
    array = utilities.generate_list(n)
    list = linked_2.create_sample(array)
    begining = time.perf_counter_ns()
    test = list.merge_sort_ascending()
    end = time.perf_counter_ns()
    #print(test.get_values())
    #print(test.length)
    print((end - begining)/1e6)


def debug_2_descending(n):
    array = utilities.generate_list(n)
    list = linked_2.create_sample(array)
    begining = time.perf_counter_ns()
    test = list.merge_sort_descending()
    end = time.perf_counter_ns()
    #print(test.get_values())
    #print(test.length)
    print((end - begining)/1e6)

if __name__ == "__main__":
    debug_2_ascending(1000)