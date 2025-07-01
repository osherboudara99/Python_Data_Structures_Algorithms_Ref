# Given two lists, create a function that lets user know (true/false) whether these two arrays contain any common items
# Example 
# l1 = ['a', 'b', 'c']
# l2 = ['z', 'x']
# Should return False
# --------
# l1 = ['a', 'b', 'c', 'x']
# l2 = ['z', 'x']
# Should return True



def item_in_common(list1, list2):
    # O(n^2)

    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

def item_in_common(list1, list2):
    # O(n)

    common_dict = {}

    for i in list1:
        common_dict[i] = True 
    
    for j in list2:
        if j in common_dict.keys():
            return True 
    return False




print(item_in_common([1,2,3,4] , [3,4,5,6,7,4])) ## Should return True

print(item_in_common([1,2] , [3,4,5,6,7,4])) ## Should return False

