
#  Question 3 


   # First sorting method : Using the Selection sort
def selection_sort(unsorted_list):
  

  for i in range(len(unsorted_list) - 1):
    min_index = i
    for j in range(i + 1, len(unsorted_list)):
      if unsorted_list[j] < unsorted_list[min_index]:
        min_index = j

    unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]

  return unsorted_list


# Example 

unsorted_list = [14, 27, 8, 42, 11, 35, -9, 56, 23]
sorted_list = selection_sort(unsorted_list)

print(sorted_list)

#The complexity class of selection sort is O(n^2)

# OUTPUT : "The numbers will be arranged in ascending order from -9 to 56"





# Second sorting method: Using the insertion sort.


def insertion_sort(unsorted_list):
  

  for i in range(1, len(unsorted_list)):
    current_element = unsorted_list[i]
    j = i - 1
    while j >= 0 and unsorted_list[j] > current_element:
      unsorted_list[j + 1] = unsorted_list[j]
      j -= 1

    unsorted_list[j + 1] = current_element

  return unsorted_list


# Example 

unsorted_list = [14, 27, 8, 42, 11, 35, -9, 56, 23]
sorted_list = insertion_sort(unsorted_list)

print(sorted_list)


# The complexity class of insertion sort is O(n^2)


# OUTPUT : "The numbers will be arranged in ascending order from -9 to 56"