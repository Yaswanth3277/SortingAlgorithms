def bubble_sort(tobesorted):
    for value in range(len(tobesorted)):
        for values in range(len(tobesorted)-1):
            if tobesorted[values] > tobesorted[values+1]:
                temp = tobesorted[values]
                tobesorted[values] = tobesorted[values+1]
                tobesorted[values+1] = temp

    return tobesorted


numbers = input("Enter the numbers to sort")  # Taking the list of numbers from the users to sort
numbers_list = numbers.split(",")  # splitting the numbers with ","
numbers_to_sort = []
for data in numbers_list:  # Converting the list of string to integers to perform sorting on them
    numbers_to_sort.append(int(data))

sorted_list = bubble_sort(numbers_to_sort)
print(sorted_list)


