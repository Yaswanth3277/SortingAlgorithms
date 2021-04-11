def bubble_sort(tobesorted):
    for value in range(len(tobesorted)):  # for loop for running the inner code for the length of array times
        for values in range(len(tobesorted)-1):  # for loop to traverse the array till the n-1 element
            if tobesorted[values] > tobesorted[values+1]:  # Comparing the first element with the next element
                temp = tobesorted[values]                  # If next element is small we swap the elements using a
                tobesorted[values] = tobesorted[values+1]  # temporary variable
                tobesorted[values+1] = temp

    return tobesorted  # Return the sorted array


numbers = input("Enter the numbers to sort")  # Taking the list of numbers from the users to sort
numbers_list = numbers.split(",")  # splitting the numbers with ","
numbers_to_sort = []
for data in numbers_list:  # Converting the list of string to integers to perform sorting on them
    numbers_to_sort.append(int(data))

sorted_list = bubble_sort(numbers_to_sort)  # Calling the bubble_sort function and
print(sorted_list)                          # passing the array that is to be sorted it then returns a sorted array


