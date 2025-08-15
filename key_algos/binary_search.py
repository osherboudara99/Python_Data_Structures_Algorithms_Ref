def binary_search(l:list[int], val :int) -> int:
    
    low = 0 
    high = len(l)-1


    while low <= high:

        mid = (low + high) // 2 

        if l[mid] == val:
            return mid 
    
        elif l[mid] < val:
            low = mid + 1 
        
        else:
            high = mid - 1 
    return -1 

l = [1,2,3,4,5,6,7,8]
print(binary_search(l, 8))


def binary_search(l:list[int], low:int, high:int, val:int) -> int:

    if low <= high:

        mid = (low + high) // 2 

        if l[mid] == val:
            return mid 
        
        elif l[mid]< val:
            return binary_search(l, mid+1, high, val)

        else:
            return binary_search(l, low, mid-1, val)
    
    return -1

l = [1,2,3,4,5,6,7,8]
print(binary_search(l, 0, len(l), 8))





    
            