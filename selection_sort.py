def selection_sort(tobesorted):
    for values in range(len(tobesorted)):
        initial_value = values
        min = values
        for values in range(values, len(tobesorted)):
            if tobesorted[values] < tobesorted[min]:
                min = values

        temp = tobesorted[initial_value]
        tobesorted[initial_value] = tobesorted[min]
        tobesorted[min] = temp
        print(tobesorted)

    return tobesorted


numbers = input("Enter the numbers to sort")  # Taking the list of numbers from the users to sort
numbers_list = numbers.split(",")  # splitting the numbers with ","
numbers_to_sort = []
for data in numbers_list:  # Converting the list of string to integers to perform sorting on them
    numbers_to_sort.append(int(data))

sorted_list = selection_sort(numbers_to_sort)
print(sorted_list)