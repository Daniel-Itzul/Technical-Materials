def merge_sort(sortSpace):
    print("sort space is {}".format(sortSpace))
    if len(sortSpace) <= 1:
        return sortSpace
    left, right = split(sortSpace)
    #print("left is {}, right is {}".format(left,right))
    left = merge_sort(left)
    right = merge_sort(right)
    print("left is {}, right is {}".format(left,right))
    return merge(left, right)

def split(stringToParse):
    midpoint = len(stringToParse)//2
    left = stringToParse[:midpoint]
    right = stringToParse[midpoint:]
    return left, right

def merge(left, right):
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


