def merge(left_array, right_array):
    final_array = []
    while len(left_array)>0 and len(right_array)>0:
        if left_array[0] > right_array[0]:
            final_array.append(right_array[0])
            right_array.remove(right_array[0])
        else:
            final_array.append(left_array[0])
            left_array.remove(left_array[0])

    while len(left_array)>0:
        final_array.append(left_array[0])
        left_array.remove(left_array[0])

    while len(right_array)>0:
        final_array.append(right_array[0])
        right_array.remove(right_array[0])

    return final_array


def merge_sort(tobesorted):
    array_length = len(tobesorted)
    if array_length == 1:
        return tobesorted

    left_list = tobesorted[:int(array_length/2)]
    right_list = tobesorted[int(array_length/2):]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return merge(left_list, right_list)


numbers = input("Enter the numbers to sort")  # Taking the list of numbers from the users to sort
numbers_list = numbers.split(",")  # splitting the numbers with ","
numbers_to_sort = []
for data in numbers_list:  # Converting the list of string to integers to perform sorting on them
    numbers_to_sort.append(int(data))

sorted_list = merge_sort(numbers_to_sort)
print(sorted_list)