def quick_sort_3(tobesorted, low, high):
    if low < high:
        partition_index = partition(tobesorted, low, high)

        quick_sort_3(tobesorted, low, partition_index - 1)
        quick_sort_3(tobesorted, partition_index + 1, high)
        return tobesorted


def partition(tobesorted, low, high):
    mid = (len(tobesorted)-1) // 2
    medians = [low, mid, high]
    for value in range(len(tobesorted)):
        for values in range(len(medians) - 1):
            if tobesorted[medians[values]] > tobesorted[medians[values + 1]]:
                temp = medians[values]
                medians[values] = medians[values + 1]
                medians[values + 1] = temp
    pivot = tobesorted[medians[1]]
    temp = tobesorted[medians[1]]
    tobesorted[medians[1]] = tobesorted[high]
    tobesorted[high] = temp
    print(medians, tobesorted, pivot)
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

sorted_array = quick_sort_3(numbers_to_sort, 0, len(numbers_to_sort)-1)
print(sorted_array)