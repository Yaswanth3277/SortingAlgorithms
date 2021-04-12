def quick_sort(tobesorted, low, high):
    if low < high:
        partition_index = partition(tobesorted, low, high)

        quick_sort(tobesorted, low, partition_index-1)
        quick_sort(tobesorted, partition_index+1, high)
        return tobesorted


def partition(tobesorted, low, high):
    pivot = tobesorted[high]

    i = low-1

    for j in range(low, high):
        if tobesorted[j] < pivot:
            i = i+1
            temp = tobesorted[i]
            tobesorted[i] = tobesorted[j]
            tobesorted[j] = temp

    temp = tobesorted[i+1]
    tobesorted[i+1] = tobesorted[high]
    tobesorted[high] = temp

    return (i+1)


numbers = input("Enter the numbers to sort")  # Taking the list of numbers from the users to sort
numbers_list = numbers.split(",")  # splitting the numbers with ","
numbers_to_sort = []
for data in numbers_list:  # Converting the list of string to integers to perform sorting on them
    numbers_to_sort.append(int(data))

sorted_array = quick_sort(numbers_to_sort, 0, len(numbers_to_sort)-1)
print(sorted_array)