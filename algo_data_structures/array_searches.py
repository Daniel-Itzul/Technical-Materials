def binary_search (searchSpace, target):
     startIndex = 0
     endIndex = len(searchSpace) - 1
     while startIndex <= endIndex :
         midpoint = (startIndex + endIndex)//2
         print(searchSpace[startIndex:endIndex+1])
         print(midpoint)
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
    print(midpoint)
    if len(searchSpace) == 0:
        return False
    if searchSpace[midpoint] == target:
        return True
    elif target < searchSpace[midpoint]:
        return recursive_binary_search_alt(searchSpace[0:midpoint],target)
    else:
        return recursive_binary_search_alt(searchSpace[midpoint+1:len(searchSpace)+1],target)