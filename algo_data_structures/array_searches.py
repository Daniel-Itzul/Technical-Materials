import utilities

def merge_sort_ascending(sortSpace):
    print("sort space is {}".format(sortSpace))
    if len(sortSpace) <= 1:
        return sortSpace
    left, right = split(sortSpace)
    left = merge_sort_ascending(left)
    right = merge_sort_ascending(right)
    print("left is {}, right is {}".format(left,right))
    return merge_ascending(left, right)

def merge_sort_ascending_alt(sortSpace):
    print("sort space is {}".format(sortSpace))
    if len(sortSpace) <= 1:
        return sortSpace
    left, right = split(sortSpace)
    left = merge_sort_ascending_alt(left)
    right = merge_sort_ascending_alt(right)
    print("left is {}, right is {}".format(left,right))
    return merge_ascending_alt(left, right)

def merge_sort_descending(sortSpace):
    print("sort space is {}".format(sortSpace))
    if len(sortSpace) <= 1:
        return sortSpace
    left, right = split(sortSpace)
    left = merge_sort_descending(left)
    right = merge_sort_descending(right)
    print("left is {}, right is {}".format(left,right))
    return merge_descending(left, right)

def split(stringToParse):
    midpoint = len(stringToParse)//2
    left = stringToParse[:midpoint]
    right = stringToParse[midpoint:]
    return left, right

def preappend(list, element):
    return [element] + list


def merge_ascending(left, right):
    result = []
    i = 0
    j = 0 
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    print("merge result is {}".format(result))
    return result

def merge_descending(left, right):
    result = []
    i = 0
    j = 0 
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    print("merge result is {}".format(result))
    return result

def merge_ascending_alt(left, right):
    result = []
    i = len(left) - 1
    j = len(right) - 1
    while i >= 0 and j >= 0:
        #print("values on i and j are {}, {}".format(i,j))
        if left[i]  > right[j]:
            result = preappend(result, left[i])
            i -= 1
        else:
            result = preappend(result, right[j])
            j -= 1
    while i >= 0:
        result = preappend(result, left[i])
        i -= 1
    while j >= 0:
        result = preappend(result, right[j])
        j -= 1
    print("merge result is {}".format(result))
    return result

def binary_search (searchSpace, target):
     startIndex = 0
     endIndex = len(searchSpace) - 1
     while startIndex <= endIndex :
         midpoint = (startIndex + endIndex)//2
         if searchSpace[midpoint] == target:
             return midpoint
         else:
             if target < searchSpace[midpoint]:
                 endIndex = midpoint - 1
             else:
                 startIndex = midpoint + 1
     return "value is not in the list"

def recursive_binary_search(searchSpace, target, start, end):
     midpoint = (start + end)//2
     print(searchSpace[start:])
     print(midpoint)
     if start == end:
         return False
     if searchSpace[midpoint] == target:
         return midpoint
     elif target < searchSpace[midpoint]:
         end = midpoint - 1
         return recursive_binary_search(searchSpace,target,start,end)
     else:
         start = midpoint + 1
         return recursive_binary_search(searchSpace,target,start,end)

def recursive_binary_search_alt(searchSpace, target):
    midpoint = (len(searchSpace))//2
    if len(searchSpace) == 0:
        return False
    if searchSpace[midpoint] == target:
        return True
    elif target < searchSpace[midpoint]:
        return recursive_binary_search_alt(searchSpace[0:midpoint],target)
    else:
        return recursive_binary_search_alt(searchSpace[midpoint+1:len(searchSpace)+1],target)


if __name__=="__main__":
    merge_sort_ascending([2, 3, 4, 5, 6, 7, 9])