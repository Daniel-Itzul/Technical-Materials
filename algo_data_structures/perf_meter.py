import time
import utilities
import linked_list_0 as linked_0
import linked_list_1 as linked_1
import linked_list_2 as linked_2

def perf_0_ascending(originArray):
    list = linked_0.create_sample(originArray)
    begining = time.perf_counter_ns()
    test = list.merge_sort_ascending()
    end = time.perf_counter_ns()
    return (end - begining)/1e6

def perf_0_descending(originArray):
    list = linked_0.create_sample(originArray)
    begining = time.perf_counter_ns()
    test = list.merge_sort_descending()
    end = time.perf_counter_ns()
    return (end - begining)/1e6

def perf_1_ascending(originArray):
    list = linked_1.create_sample(originArray)
    begining = time.perf_counter_ns()
    test = list.merge_sort_ascending()
    end = time.perf_counter_ns()
    return (end - begining)/1e6

def perf_1_descending(originArray):
    list = linked_1.create_sample(originArray)
    begining = time.perf_counter_ns()
    test = list.merge_sort_descending()
    end = time.perf_counter_ns()
    return (end - begining)/1e6

def perf_2_ascending(originArray):
    list = linked_2.create_sample(originArray)
    begining = time.perf_counter_ns()
    test = list.merge_sort_ascending()
    end = time.perf_counter_ns()
    return (end - begining)/1e6

def perf_2_descending(originArray):
    list = linked_2.create_sample(originArray)
    begining = time.perf_counter_ns()
    test = list.merge_sort_descending()
    end = time.perf_counter_ns()
    return (end - begining)/1e6

def measure_class(option, array):
    match option:
        case 0:
            return perf_0_ascending(array), perf_0_descending(array)
        case 1:
            return perf_1_ascending(array), perf_1_descending(array)
        case 2:
            return perf_2_ascending(array), perf_2_descending(array)

def measure(n):
    elements = utilities.generate_list(n)
    #print(measure_class(0, elements))
    print(measure_class(1, elements))
    print(measure_class(2, elements))






if __name__ == "__main__":
    measure(100000)