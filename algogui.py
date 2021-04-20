import tkinter
from tkinter import *


def bubblesort():
    inparray = textfield_label.get()
    numbers_list = inparray.split(",")  # splitting the numbers with ","
    tobesorted = []
    min_index = 0
    next_index = 0
    for data in numbers_list:  # Converting the list of string to integers to perform sorting on them
        tobesorted.append(int(data))

    x = 250
    y = 50
    for num in range(len(tobesorted)):

        actual_array.create_text(x, y, text=tobesorted[num], font='Arial 20')
        x = x + 20
        actual_array.update()
        actual_array.after(500)

    for value in range(len(tobesorted)):  # for loop for running the inner code for the length of array times
        for values in range(len(tobesorted)-1):  # for loop to traverse the array till the n-1 element
            if tobesorted[values] > tobesorted[values+1]:
                min_index = values
                next_index = values+1
                # Comparing the first element with the next element
                temp = tobesorted[values]                  # If next element is small we swap the elements using a
                tobesorted[values] = tobesorted[values+1]  # temporary variable
                tobesorted[values+1] = temp
            x = 250
            y = 80
            results.delete('all')
            for data in range(len(tobesorted)):
                if data == min_index or data == next_index:
                    results.create_text(x, y, text=tobesorted[data], font='Arial 20', fill='red')
                else:
                    results.create_text(x, y, text=tobesorted[data], font='Arial 20')
                x = x+20
            results.update()
            results.after(1000)
    result.config(text=tobesorted)
    return tobesorted  # Return the sorted array


def insertionsort():
    inparray = textfield_label.get()
    numbers_list = inparray.split(",")  # splitting the numbers with ","
    tobesorted = []
    min_index = 0
    next_index = 0
    for data in numbers_list:  # Converting the list of string to integers to perform sorting on them
        tobesorted.append(int(data))

    x = 250
    y = 50
    for num in range(len(tobesorted)):

        actual_array.create_text(x, y, text=tobesorted[num], font='Arial 20')
        x = x + 20
        actual_array.update()
        actual_array.after(500)

    for values in range(1, len(tobesorted)):
        temp = tobesorted[values]
        index = values-1
        min_index = values
        while temp < tobesorted[index] and index >= 0:
            tobesorted[index+1] = tobesorted[index]
            index = index-1

            x = 250
            y = 80
            results.delete('all')
            for data in range(len(tobesorted)):
                if data == min_index or data == index:
                    results.create_text(x, y, text=tobesorted[data], font='Arial 20', fill='red')
                else:
                    results.create_text(x, y, text=tobesorted[data], font='Arial 20')
                x = x+20
            results.update()
            results.after(1000)

        tobesorted[index+1] = temp
    result.config(text=tobesorted)
    return tobesorted  # Return the sorted array


def selectionsort():
    inparray = textfield_label.get()
    numbers_list = inparray.split(",")  # splitting the numbers with ","
    tobesorted = []
    min_index = 0
    next_index = 0
    for data in numbers_list:  # Converting the list of string to integers to perform sorting on them
        tobesorted.append(int(data))

    x = 250
    y = 50
    for num in range(len(tobesorted)):

        actual_array.create_text(x, y, text=tobesorted[num], font='Arial 20')
        x = x + 20
        actual_array.update()
        actual_array.after(500)

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

        x = 250
        y = 80
        results.delete('all')
        for data in range(len(tobesorted)):
            if data == min or data == initial_value:
                results.create_text(x, y, text=tobesorted[data], font='Arial 20', fill='red')
            else:
                results.create_text(x, y, text=tobesorted[data], font='Arial 20')
            x = x+20
        results.update()
        results.after(1000)

    result.config(text=tobesorted)
    return tobesorted  # Return the sorted array


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
    result.config(text=final_array)
    return final_array


def mergesort(tobesorted):
    array_length = len(tobesorted)
    if array_length == 1:
        return tobesorted

    left_list = tobesorted[:int(array_length/2)]
    right_list = tobesorted[int(array_length/2):]

    x = 50
    y = 50
    for y in range(len(left_list)):
        results.create_text(x, y, text=left_list, font='Arial 20')
        y = y + 30
    x = x+250
    for y in range(len(right_list)):
        results.create_text(x, y, text=right_list, font='Arial 20')
        y


    left_list = mergesort(left_list)
    right_list = mergesort(right_list)

    return merge(left_list, right_list)


def mergesort_help():
    inparray = textfield_label.get()
    numbers_list = inparray.split(",")  # splitting the numbers with ","
    tobesorted = []
    for data in numbers_list:  # Converting the list of string to integers to perform sorting on them
        tobesorted.append(int(data))

    x = 250
    y = 50
    for num in range(len(tobesorted)):

        actual_array.create_text(x, y, text=tobesorted[num], font='Arial 20')
        x = x + 20
        actual_array.update()
        actual_array.after(500)
    mergesort(tobesorted)


def bubble_sort_window():
    global textfield_label, result, results, actual_array
    textfield_label = StringVar()
    window.destroy()
    bubble_window = Tk()
    bubble_window.geometry("600x600")
    bubble_window.title("Bubble Sort")
    Label(bubble_window, text = "Array").pack()
    textfield_label = Entry(bubble_window)
    textfield_label.focus()
    textfield_label.bind("<Return>", bubblesort)
    textfield_label.pack()
    search = Button(bubble_window, text="Sort", command = bubblesort).pack()
    print(search)
    actual_array = tkinter.Canvas(bg='white', width='800', height='100')
    actual_array.pack()
    results = tkinter.Canvas(bg='white',width='800',height='400')
    results.pack()
    result = Label(bubble_window, text=search)
    result.pack(fill=X)
    mainloop()


def insertion_sort_window():
    global textfield_label, result, results, actual_array
    textfield_label = StringVar()
    window.destroy()
    insertion_window = Tk()
    insertion_window.geometry("600x600")
    insertion_window.title("Insertion Sort")
    Label(insertion_window, text = "Array").pack()
    textfield_label = Entry(insertion_window)
    textfield_label.focus()
    textfield_label.bind("<Return>", insertionsort)
    textfield_label.pack()
    search = Button(insertion_window, text="Sort", command = insertionsort).pack()
    print(search)
    actual_array = tkinter.Canvas(bg='white', width='800', height='100')
    actual_array.pack()
    results = tkinter.Canvas(bg='white',width='800',height='400')
    results.pack()
    result = Label(insertion_window, text=search)
    result.pack(fill=X)
    mainloop()


def selection_sort_window():
    global textfield_label, result, results, actual_array
    textfield_label = StringVar()
    window.destroy()
    selection_window = Tk()
    selection_window.geometry("600x600")
    selection_window.title("Selection Sort")
    Label(selection_window, text = "Array").pack()
    textfield_label = Entry(selection_window)
    textfield_label.focus()
    textfield_label.bind("<Return>", selectionsort)
    textfield_label.pack()
    search = Button(selection_window, text="Sort", command = selectionsort).pack()
    print(search)
    actual_array = tkinter.Canvas(bg='white', width='800', height='100')
    actual_array.pack()
    results = tkinter.Canvas(bg='white',width='800',height='400')
    results.pack()
    result = Label(selection_window, text=search)
    result.pack(fill=X)
    mainloop()


def merge_sort_window():
    global textfield_label, result, results, actual_array
    textfield_label = StringVar()
    window.destroy()
    merge_window = Tk()
    merge_window.geometry("600x600")
    merge_window.title("Selection Sort")
    Label(merge_window, text = "Array").pack()
    textfield_label = Entry(merge_window)
    textfield_label.focus()
    textfield_label.bind("<Return>", mergesort)
    textfield_label.pack()
    search = Button(merge_window, text="Sort", command = mergesort_help).pack()
    print(search)
    actual_array = tkinter.Canvas(bg='white', width='800', height='100')
    actual_array.pack()
    results = tkinter.Canvas(bg='white',width='800',height='400')
    results.pack()
    result = Label(merge_window, text=search)
    result.pack(fill=X)
    mainloop()


if __name__ == "__main__":
    window = Tk()
    window.geometry("600x600")
    window.title("Sorting algorithms")

    head = Label(window, text="Sorting Algorithm").pack()
    bubble_sort = Button(window, text="Bubble Sort", command=bubble_sort_window).pack()
    insertion_sort = Button(window, text="Insertion sort", command=insertion_sort_window).pack()
    selection_sort = Button(window, text="Selection Sort", command=selection_sort_window).pack()
    merge_sort = Button(window, text="Merge Sort", command=merge_sort_window).pack()
    heap_sort = Button(window, text="Heap Sort").pack()
    quick_sort = Button(window, text="Quick Sort").pack()
    median3_quicksort = Button(window, text="3 Median Quick Sort").pack()
    window.mainloop()
