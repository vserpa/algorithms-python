# Declarations

def binary_search(arrList, item):
  
  start = 0
  end = len(arrList) - 1
  
  while start <= end:
    middle = (start + end) / 2
    element = arrList[middle]
    
    if element == item:
      return middle
    
    if element > item:
      end = middle - 1
    else:
      start = middle + 1
      
  return None
  
# Program

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print binary_search(my_list, 8)