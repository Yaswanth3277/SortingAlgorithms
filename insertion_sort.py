def insertion_sort(tobesorted):
    for values in range(1, len(tobesorted)):
        temp = tobesorted[values]
        index = values-1
        while temp < tobesorted[index] and index >= 0:
            tobesorted[index+1] = tobesorted[index]
            index = index-1

        tobesorted[index+1] = temp
    return tobesorted


numbers = input("Enter the numbers to sort")  # Taking the list of numbers from the users to sort
numbers_list = numbers.split(",")  # splitting the numbers with ","
numbers_to_sort = []
for data in numbers_list:  # Converting the list of string to integers to perform sorting on them
    numbers_to_sort.append(int(data))

sorted_list = insertion_sort(numbers_to_sort)
print(sorted_list)