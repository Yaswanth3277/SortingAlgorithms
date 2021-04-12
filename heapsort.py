def heapify(tobesorted, n, value):
    largest = value
    left = 2 * value + 1
    right = 2 * value + 2

    if left < n and tobesorted[largest] < tobesorted[left]:
        largest = left

    if right < n and tobesorted[largest] < tobesorted[right]:
        largest = right

    if largest != value:
        tobesorted[value], tobesorted[largest] = tobesorted[largest], tobesorted[value]
        heapify(tobesorted, n, largest)


def heap_sort(tobesorted):
    n = len(tobesorted)

    for value in range(n//2 - 1, -1, -1):
        heapify(tobesorted, n, value)

    for values in range(n-1, 0, -1):
        tobesorted[0], tobesorted[values] = tobesorted[values], tobesorted[0]
        heapify(tobesorted, values, 0)

    return tobesorted


numbers = input("Enter the numbers to sort")  # Taking the list of numbers from the users to sort
numbers_list = numbers.split(",")  # splitting the numbers with ","
numbers_to_sort = []
for data in numbers_list:  # Converting the list of string to integers to perform sorting on them
    numbers_to_sort.append(int(data))

sorted_array = heap_sort(numbers_to_sort)
print(sorted_array)