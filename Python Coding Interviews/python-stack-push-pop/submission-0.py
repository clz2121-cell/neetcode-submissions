from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    reverse = [] 
    copy = arr.copy() 
    for element in arr: 
        ele = copy.pop() 
        reverse.append(ele) 
    return reverse 


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
