import tkinter
from tkinter import *
import timeit
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random


def bubble_sorts():
    inparray = textfield_label.get()
    print(inparray)
    numbers_list = inparray.split(",")  # splitting the numbers with ","
    tobe_sorted = []
    for data in numbers_list:  # Converting the list of string to integers to perform sorting on them
        tobe_sorted.append(int(data))
    start_time = timeit.default_timer()
    for value in range(len(tobe_sorted)):  # for loop for running the inner code for the length of array times
        for values in range(len(tobe_sorted)-1):  # for loop to traverse the array till the n-1 element
            if tobe_sorted[values] > tobe_sorted[values+1]:  # Comparing the first element with the next element
                temp = tobe_sorted[values]                  # If next element is small we swap the elements using a
                tobe_sorted[values] = tobe_sorted[values+1]  # temporary variable
                tobe_sorted[values+1] = temp
    elapsed = timeit.default_timer() - start_time
    print(elapsed)
    runtime.create_text(200, 80, text=elapsed, font='Arial 20', fill='white')
    result.create_text(100, 80, text=tobe_sorted, font='Arial 20', fill='white')
    return elapsed


def insertion_sorts():
    inparray = textfield_label.get()
    numbers_list = inparray.split(",")  # splitting the numbers with ","
    tobe_sorted = []
    for data in numbers_list:  # Converting the list of string to integers to perform sorting on them
        tobe_sorted.append(int(data))
    start_time = timeit.default_timer()
    for values in range(1, len(tobe_sorted)):
        temp = tobe_sorted[values]
        index = values-1
        while temp < tobe_sorted[index] and index >= 0:
            tobe_sorted[index+1] = tobe_sorted[index]
            index = index-1

        tobe_sorted[index+1] = temp
    elapsed = timeit.default_timer() - start_time
    print(elapsed)
    runtime.create_text(200, 80, text=elapsed, font='Arial 20', fill='white')
    result.create_text(100, 80, text=tobe_sorted, font='Arial 20', fill='white')
    return elapsed


def selection_sorts():
    inparray = textfield_label.get()
    numbers_list = inparray.split(",")  # splitting the numbers with ","
    tobe_sorted = []
    for data in numbers_list:  # Converting the list of string to integers to perform sorting on them
        tobe_sorted.append(int(data))
    start_time = timeit.default_timer()
    for values in range(len(tobe_sorted)):
        initial_value = values
        min = values
        for values in range(values,len(tobe_sorted)):
            if tobe_sorted[values]<tobe_sorted[min]:
                min = values

        temp = tobe_sorted[initial_value]
        tobe_sorted[initial_value] = tobe_sorted[min]
        tobe_sorted[min] = temp
        print(tobe_sorted)
    elapsed = timeit.default_timer() - start_time
    print(elapsed)
    runtime.create_text(200, 80, text=elapsed, font='Arial 20', fill='white')
    result.create_text(100, 80, text=tobe_sorted, font='Arial 20', fill='white')
    return elapsed


def merges(left_array, right_array):
    finals_array = []
    while len(left_array)>0 and len(right_array)>0:
        if left_array[0] > right_array[0]:
            finals_array.append(right_array[0])
            right_array.remove(right_array[0])
        else:
            finals_array.append(left_array[0])
            left_array.remove(left_array[0])

    while len(left_array)>0:
        finals_array.append(left_array[0])
        left_array.remove(left_array[0])

    while len(right_array)>0:
        finals_array.append(right_array[0])
        right_array.remove(right_array[0])
    return finals_array


def merge_sorts(tobe_sorted):
    array_length = len(tobe_sorted)
    if array_length == 1:
        return tobe_sorted

    left_list = tobe_sorted[:int(array_length/2)]
    right_list = tobe_sorted[int(array_length/2):]

    left_list = merge_sorts(left_list)
    right_list = merge_sorts(right_list)
    return merges(left_list, right_list)


def heapifys(tobe_sorted, n, value):
    largest = value
    left = 2 * value + 1
    right = 2 * value + 2

    if left < n and tobe_sorted[largest] < tobe_sorted[left]:
        largest = left

    if right < n and tobe_sorted[largest] < tobe_sorted[right]:
        largest = right

    if largest != value:
        tobe_sorted[value], tobe_sorted[largest] = tobe_sorted[largest], tobe_sorted[value]
        heapifys(tobe_sorted, n, largest)


def heap_sorts(tobe_sorted):
    n = len(tobe_sorted)

    for value in range(n//2 - 1, -1, -1):
        heapifys(tobe_sorted, n, value)

    for values in range(n-1, 0, -1):
        tobe_sorted[0], tobe_sorted[values] = tobe_sorted[values], tobe_sorted[0]
        heapifys(tobe_sorted, values, 0)

    return tobe_sorted


def quick_sorts(tobe_sorted, low, high):
    if low < high:
        partition_index = partitions(tobe_sorted, low, high)

        quick_sorts(tobe_sorted, low, partition_index-1)
        quick_sorts(tobe_sorted, partition_index+1, high)
        return tobe_sorted


def partitions(tobe_sorted, low, high):
    pivot = tobe_sorted[high]

    i = low-1

    for j in range(low, high):
        if tobe_sorted[j] < pivot:
            i = i+1
            temp = tobe_sorted[i]
            tobe_sorted[i] = tobe_sorted[j]
            tobe_sorted[j] = temp

    temp = tobe_sorted[i+1]
    tobe_sorted[i+1] = tobe_sorted[high]
    tobe_sorted[high] = temp

    return (i+1)


def quick_sorts_3(tobe_sorted, low, high):
    if low < high:
        partition_index = partitions3(tobe_sorted, low, high)

        quick_sorts_3(tobe_sorted, low, partition_index - 1)
        quick_sorts_3(tobe_sorted, partition_index + 1, high)
        return tobe_sorted


def partitions3(tobe_sorted, low, high):
    mid = (len(tobe_sorted)-1) // 2
    medians = [low, mid, high]
    for value in range(len(tobe_sorted)):
        for values in range(len(medians) - 1):
            if tobe_sorted[medians[values]] > tobe_sorted[medians[values + 1]]:
                temp = medians[values]
                medians[values] = medians[values + 1]
                medians[values + 1] = temp
    pivot = tobe_sorted[medians[1]]
    temp = tobe_sorted[medians[1]]
    tobe_sorted[medians[1]] = tobe_sorted[high]
    tobe_sorted[high] = temp
    print(medians, tobe_sorted, pivot)
    i = low-1

    for j in range(low, high):
        if tobe_sorted[j] < pivot:
            i = i+1
            temp = tobe_sorted[i]
            tobe_sorted[i] = tobe_sorted[j]
            tobe_sorted[j] = temp

    temp = tobe_sorted[i+1]
    tobe_sorted[i+1] = tobe_sorted[high]
    tobe_sorted[high] = temp

    return (i+1)


def bubblesort(tobesorted):
    min_index = 0
    next_index = 0
    for value in range(len(tobesorted)):  # for loop for running the inner code for the length of array times
        for values in range(len(tobesorted)-1):  # for loop to traverse the array till the n-1 element
            if tobesorted[values] > tobesorted[values+1]:
                min_index = values
                next_index = values+1
                # Comparing the first element with the next element
                temp = tobesorted[values]                  # If next element is small we swap the elements using a
                tobesorted[values] = tobesorted[values+1]  # temporary variable
                tobesorted[values+1] = temp
            x = 50
            y = 80
            results.delete('all')
            for data in range(len(tobesorted)):
                if data == min_index or data == next_index:
                    results.create_text(x, y, text=tobesorted[data], font='Arial 20', fill='yellow')
                else:
                    results.create_text(x, y, text=tobesorted[data], font='Arial 20', fill='white')
                x = x+20
            results.update()
            results.after(1000)
    return tobesorted  # Return the sorted array


def insertionsort(tobesorted):
    for values in range(1, len(tobesorted)):
        temp = tobesorted[values]
        index = values-1
        min_index = values
        while temp < tobesorted[index] and index >= 0:
            tobesorted[index+1] = tobesorted[index]
            index = index-1

            x = 50
            y = 80
            results.delete('all')
            for data in range(len(tobesorted)):
                if data == min_index or data == index:
                    results.create_text(x, y, text=tobesorted[data], font='Arial 20', fill='yellow')
                else:
                    results.create_text(x, y, text=tobesorted[data], font='Arial 20', fill='white')
                x = x+20
            results.update()
            results.after(1000)

        tobesorted[index+1] = temp
        x = 50
        y = 80
        results.delete('all')
        for data in range(len(tobesorted)):
            results.create_text(x, y, text=tobesorted[data], font='Arial 20', fill='white')
            x = x + 20
        results.update()
        results.after(1000)
    return tobesorted  # Return the sorted array


def selectionsort(tobesorted):
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

        x = 50
        y = 80
        results.delete('all')
        for data in range(len(tobesorted)):
            if data == min or data == initial_value:
                results.create_text(x, y, text=tobesorted[data], font='Arial 20', fill='yellow')
            else:
                results.create_text(x, y, text=tobesorted[data], font='Arial 20', fill='white')
            x = x+20
        results.update()
        results.after(1000)

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
        results.create_text(x, y, text=left_list, font='Arial 20', fill='white')
        y = y + 30
    x = x+250
    for y in range(len(right_list)):
        results.create_text(x, y, text=right_list, font='Arial 20', fill='white')

    left_list = mergesort(left_list)
    right_list = mergesort(right_list)

    return merge(left_list, right_list)


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


def heapsort(tobesorted):
    n = len(tobesorted)

    for value in range(n//2 - 1, -1, -1):
        heapify(tobesorted, n, value)

    for values in range(n-1, 0, -1):
        tobesorted[0], tobesorted[values] = tobesorted[values], tobesorted[0]
        heapify(tobesorted, values, 0)
    return tobesorted


def quicksort(tobesorted, low, high):
    if low < high:
        partition_index = partition(tobesorted, low, high)

        quicksort(tobesorted, low, partition_index-1)
        quicksort(tobesorted, partition_index+1, high)
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
    print(tobesorted, pivot)

    return (i+1)


def quicksort3(tobesorted, low, high):
    if low < high:
        partition_index = partition3(tobesorted, low, high)

        quicksort3(tobesorted, low, partition_index - 1)
        quicksort3(tobesorted, partition_index + 1, high)
        return tobesorted


def partition3(tobesorted, low, high):
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


def bubblesort_help():
    inparray = textfield_label.get()
    numbers_list = inparray.split(",")  # splitting the numbers with ","
    tobesorted = []
    min_index = 0
    next_index = 0
    for data in numbers_list:  # Converting the list of string to integers to perform sorting on them
        tobesorted.append(int(data))

    x = 50
    y = 50
    for num in range(len(tobesorted)):
        actual_array.create_text(x, y, text=tobesorted[num], font='Arial 20', fill='white')
        x = x + 20
        actual_array.update()
        actual_array.after(500)
    bubble_sorts()
    bubblesort(tobesorted)


def insertionsort_help():
    inparray = textfield_label.get()
    numbers_list = inparray.split(",")  # splitting the numbers with ","
    tobesorted = []
    min_index = 0
    next_index = 0
    for data in numbers_list:  # Converting the list of string to integers to perform sorting on them
        tobesorted.append(int(data))

    x = 50
    y = 50
    for num in range(len(tobesorted)):
        actual_array.create_text(x, y, text=tobesorted[num], font='Arial 20', fill='white')
        x = x + 20
        actual_array.update()
        actual_array.after(500)
    insertion_sorts()
    insertionsort(tobesorted)


def selectionsort_help():
    inparray = textfield_label.get()
    numbers_list = inparray.split(",")  # splitting the numbers with ","
    tobesorted = []
    min_index = 0
    next_index = 0
    for data in numbers_list:  # Converting the list of string to integers to perform sorting on them
        tobesorted.append(int(data))

    x = 50
    y = 50
    for num in range(len(tobesorted)):
        actual_array.create_text(x, y, text=tobesorted[num], font='Arial 20', fill='white')
        x = x + 20
        actual_array.update()
        actual_array.after(500)
    selection_sorts()
    selectionsort(tobesorted)


def mergesort_help():
    inparray = textfield_label.get()
    numbers_list = inparray.split(",")  # splitting the numbers with ","
    tobesorted = []
    for data in numbers_list:  # Converting the list of string to integers to perform sorting on them
        tobesorted.append(int(data))
    tobe_sorted = tobesorted
    x = 50
    y = 50
    for num in range(len(tobesorted)):

        actual_array.create_text(x, y, text=tobesorted[num], font='Arial 20', fill='white')
        x = x + 20
        actual_array.update()
        actual_array.after(500)
    start_time = timeit.default_timer()
    sorted_array = merge_sorts(tobe_sorted)
    elapsed = timeit.default_timer() - start_time
    result.create_text(100, 80, text=sorted_array, font='Arial 20', fill='white')
    runtime.create_text(200, 80, text=elapsed, font='Arial 20', fill='white')
    mergesort(tobesorted)
    return elapsed


def heapsort_help():
    inparray = textfield_label.get()
    numbers_list = inparray.split(",")  # splitting the numbers with ","
    tobesorted = []
    for data in numbers_list:  # Converting the list of string to integers to perform sorting on them
        tobesorted.append(int(data))
    tobe_sorted = tobesorted
    x = 50
    y = 50
    for num in range(len(tobesorted)):
        actual_array.create_text(x, y, text=tobesorted[num], font='Arial 20', fill='white')
        x = x + 20
        actual_array.update()
        actual_array.after(500)
    start_time = timeit.default_timer()
    sorted_array = heap_sorts(tobe_sorted)
    elapsed = timeit.default_timer() - start_time
    result.create_text(100, 80, text=sorted_array, font='Arial 20', fill='white')
    runtime.create_text(200, 80, text=elapsed, font='Arial 20', fill='white')
    heapsort(tobesorted)
    return elapsed


def quicksort_help():
    inparray = textfield_label.get()
    numbers_list = inparray.split(",")  # splitting the numbers with ","
    tobesorted = []
    for data in numbers_list:  # Converting the list of string to integers to perform sorting on them
        tobesorted.append(int(data))
    tobe_sorted = tobesorted
    x = 50
    y = 50
    for num in range(len(tobesorted)):
        actual_array.create_text(x, y, text=tobesorted[num], font='Arial 20', fill='white')
        x = x + 20
        actual_array.update()
        actual_array.after(500)

    start_time = timeit.default_timer()
    sorted_array = quick_sorts(tobe_sorted, 0, len(tobesorted)-1)
    elapsed = timeit.default_timer() - start_time
    result.create_text(100, 80, text=sorted_array, font='Arial 20', fill='white')
    runtime.create_text(200, 80, text=elapsed, font='Arial 20', fill='white')
    quicksort(tobesorted, 0, len(tobesorted)-1)
    return elapsed


def quicksort3_help():
    inparray = textfield_label.get()
    numbers_list = inparray.split(",")  # splitting the numbers with ","
    tobesorted = []
    for data in numbers_list:  # Converting the list of string to integers to perform sorting on them
        tobesorted.append(int(data))
    tobe_sorted = tobesorted
    x = 50
    y = 50
    for num in range(len(tobesorted)):
        actual_array.create_text(x, y, text=tobesorted[num], font='Arial 20', fill='white')
        x = x + 20
        actual_array.update()
        actual_array.after(500)
    start_time = timeit.default_timer()
    sorted_array = quick_sorts_3(tobe_sorted, 0, len(tobesorted) - 1)
    elapsed = timeit.default_timer() - start_time
    result.create_text(100, 80, text=sorted_array, font='Arial 20', fill='white')
    runtime.create_text(200, 80, text=elapsed, font='Arial 20', fill='white')
    quicksort3(tobesorted, 0, len(tobesorted)-1)
    return elapsed


def goback(existing_window):
    existing_window.destroy()
    mainwindow()


def bubble_sort_window():
    global textfield_label, result, results, actual_array, runtime
    textfield_label = StringVar()
    window.destroy()
    bubble_window = Tk()
    bubble_window.geometry("600x600")
    bubble_window.config(bg="black")
    bubble_window.title("Bubble Sort")
    Button(bubble_window, text="<", bg="black", foreground="white", font=("Arial",15), border=0, command=lambda:goback(bubble_window)).place(x=0, y=0, width=30)
    Label(bubble_window, text="Bubble Sort", bg="black", foreground="white", font=("Arial", 20)).pack()
    Label(bubble_window, text = "Array", bg="black", foreground="white", font=("Arial", 10)).place(x=225, y=50)
    Label(bubble_window, text="______________________________", bg="black", foreground="white").place(x=273, y=60)
    textfield_label = Entry(bubble_window, bg="black", foreground="white", border=0, insertbackground="white")
    textfield_label.focus()
    textfield_label.bind("<Return>", bubblesort)
    textfield_label.place(x=275, y=50, height=20, width=150)
    search = Button(bubble_window, text="Sort", command = bubblesort_help).place(x=250, y=100, width=100)
    print(search)
    Label(bubble_window, text = "Input", font=("Arial",15), bg="black", foreground="white").place(x=100, y=170)
    actual_array = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    actual_array.place(x=200, y=150)
    Label(bubble_window, text="Output", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=270)
    result = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    result.place(x=200, y=250)
    Label(bubble_window, text="Runtime", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=370)
    runtime = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    runtime.place(x=200, y=350)
    Label(bubble_window, text="Execution", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=470)
    results = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    results.place(x=200, y=450)
    mainloop()


def insertion_sort_window():
    global textfield_label, result, results, actual_array, runtime
    textfield_label = StringVar()
    window.destroy()
    insertion_window = Tk()
    insertion_window.geometry("600x600")
    insertion_window.config(bg="black")
    insertion_window.title("Insertion Sort")
    Button(insertion_window, text="<", bg="black", foreground="white", font=("Arial", 15), border=0, command=lambda: goback(insertion_window)).place(x=0, y=0, width=30)
    Label(insertion_window, text="Insertion Sort", bg="black", foreground="white", font=("Arial", 20)).pack()
    Label(insertion_window, text="Array", bg="black", foreground="white", font=("Arial", 10)).place(x=225, y=50)
    Label(insertion_window, text="______________________________", bg="black", foreground="white").place(x=273, y=60)
    textfield_label = Entry(insertion_window, bg="black", foreground="white", border=0, insertbackground="white")
    textfield_label.focus()
    textfield_label.bind("<Return>", insertionsort)
    textfield_label.place(x=275, y=50, height=20, width=150)
    search = Button(insertion_window, text="Sort", command=insertionsort_help).place(x=250, y=100, width=100)
    print(search)
    Label(insertion_window, text="Input", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=170)
    actual_array = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    actual_array.place(x=200, y=150)
    Label(insertion_window, text="Output", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=270)
    result = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    result.place(x=200, y=250)
    Label(insertion_window, text="Runtime", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=370)
    runtime = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    runtime.place(x=200, y=350)
    Label(insertion_window, text="Execution", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=470)
    results = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    results.place(x=200, y=450)
    mainloop()


def selection_sort_window():
    global textfield_label, result, results, actual_array, runtime
    textfield_label = StringVar()
    window.destroy()
    selection_window = Tk()
    selection_window.geometry("600x600")
    selection_window.config(bg="black")
    selection_window.title("Selection Sort")
    Button(selection_window, text="<", bg="black", foreground="white", font=("Arial", 15), border=0,
           command=lambda: goback(selection_window)).place(x=0, y=0, width=30)
    Label(selection_window, text="Selection Sort", bg="black", foreground="white", font=("Arial", 20)).pack()
    Label(selection_window, text="Array", bg="black", foreground="white", font=("Arial", 10)).place(x=225, y=50)
    Label(selection_window, text="______________________________", bg="black", foreground="white").place(x=273, y=60)
    textfield_label = Entry(selection_window, bg="black", foreground="white", border=0, insertbackground="white")
    textfield_label.focus()
    textfield_label.bind("<Return>", selectionsort)
    textfield_label.place(x=275, y=50, height=20, width=150)
    search = Button(selection_window, text="Sort", command=selectionsort_help).place(x=250, y=100, width=100)
    print(search)
    Label(selection_window, text="Input", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=170)
    actual_array = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    actual_array.place(x=200, y=150)
    Label(selection_window, text="Output", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=270)
    result = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    result.place(x=200, y=250)
    Label(selection_window, text="Runtime", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=370)
    runtime = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    runtime.place(x=200, y=350)
    Label(selection_window, text="Execution", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=470)
    results = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    results.place(x=200, y=450)
    mainloop()


def merge_sort_window():
    global textfield_label, result, results, actual_array, runtime
    textfield_label = StringVar()
    window.destroy()
    merge_window = Tk()
    merge_window.geometry("600x600")
    merge_window.config(bg="black")
    merge_window.title("Merge Sort")
    Button(merge_window, text="<", bg="black", foreground="white", font=("Arial", 15), border=0,
           command=lambda: goback(merge_window)).place(x=0, y=0, width=30)
    Label(merge_window, text="Merge Sort", bg="black", foreground="white", font=("Arial", 20)).pack()
    Label(merge_window, text="Array", bg="black", foreground="white", font=("Arial", 10)).place(x=225, y=50)
    Label(merge_window, text="______________________________", bg="black", foreground="white").place(x=273, y=60)
    textfield_label = Entry(merge_window, bg="black", foreground="white", border=0, insertbackground="white")
    textfield_label.focus()
    textfield_label.bind("<Return>", mergesort)
    textfield_label.place(x=275, y=50, height=20, width=150)
    search = Button(merge_window, text="Sort", command=mergesort_help).place(x=250, y=100, width=100)
    print(search)
    Label(merge_window, text="Input", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=170)
    actual_array = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    actual_array.place(x=200, y=150)
    Label(merge_window, text="Output", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=270)
    result = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    result.place(x=200, y=250)
    Label(merge_window, text="Runtime", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=370)
    runtime = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    runtime.place(x=200, y=350)
    Label(merge_window, text="Execution", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=470)
    results = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    results.place(x=200, y=450)
    mainloop()


def heap_sort_window():
    global textfield_label, result, results, actual_array, runtime
    textfield_label = StringVar()
    window.destroy()
    heap_window = Tk()
    heap_window.geometry("600x600")
    heap_window.config(bg="black")
    heap_window.title("Heap Sort")
    Button(heap_window, text="<", bg="black", foreground="white", font=("Arial", 15), border=0,
           command=lambda: goback(heap_window)).place(x=0, y=0, width=30)
    Label(heap_window, text="Heap Sort", bg="black", foreground="white", font=("Arial", 20)).pack()
    Label(heap_window, text="Array", bg="black", foreground="white", font=("Arial", 10)).place(x=225, y=50)
    Label(heap_window, text="______________________________", bg="black", foreground="white").place(x=273, y=60)
    textfield_label = Entry(heap_window, bg="black", foreground="white", border=0, insertbackground="white")
    textfield_label.focus()
    textfield_label.bind("<Return>", heapsort)
    textfield_label.place(x=275, y=50, height=20, width=150)
    search = Button(heap_window, text="Sort", command=heapsort_help).place(x=250, y=100, width=100)
    print(search)
    Label(heap_window, text="Input", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=170)
    actual_array = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    actual_array.place(x=200, y=150)
    Label(heap_window, text="Output", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=270)
    result = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    result.place(x=200, y=250)
    Label(heap_window, text="Runtime", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=370)
    runtime = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    runtime.place(x=200, y=350)
    Label(heap_window, text="Execution", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=470)
    results = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    results.place(x=200, y=450)
    mainloop()


def quick_sort_window():
    global textfield_label, result, results, actual_array, runtime
    textfield_label = StringVar()
    window.destroy()
    quick_window = Tk()
    quick_window.geometry("600x600")
    quick_window.config(bg="black")
    quick_window.title("Quick Sort")
    Button(quick_window, text="<", bg="black", foreground="white", font=("Arial", 15), border=0,
           command=lambda: goback(quick_window)).place(x=0, y=0, width=30)
    Label(quick_window, text="Quick Sort", bg="black", foreground="white", font=("Arial", 20)).pack()
    Label(quick_window, text="Array", bg="black", foreground="white", font=("Arial", 10)).place(x=225, y=50)
    Label(quick_window, text="______________________________", bg="black", foreground="white").place(x=273, y=60)
    textfield_label = Entry(quick_window, bg="black", foreground="white", border=0, insertbackground="white")
    textfield_label.focus()
    textfield_label.bind("<Return>", quicksort)
    textfield_label.place(x=275, y=50, height=20, width=150)
    search = Button(quick_window, text="Sort", command=quicksort_help).place(x=250, y=100, width=100)
    print(search)
    Label(quick_window, text="Input", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=170)
    actual_array = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    actual_array.place(x=200, y=150)
    Label(quick_window, text="Output", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=270)
    result = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    result.place(x=200, y=250)
    Label(quick_window, text="Runtime", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=370)
    runtime = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    runtime.place(x=200, y=350)
    Label(quick_window, text="Execution", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=470)
    results = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    results.place(x=200, y=450)
    mainloop()


def quick3_sort_window():
    global textfield_label, result, results, actual_array, runtime
    textfield_label = StringVar()
    window.destroy()
    quick3_window = Tk()
    quick3_window.geometry("600x600")
    quick3_window.config(bg="black")
    quick3_window.title("3 Median Quick Sort")
    Button(quick3_window, text="<", bg="black", foreground="white", font=("Arial", 15), border=0,
           command=lambda: goback(quick3_window)).place(x=0, y=0, width=30)
    Label(quick3_window, text="3 Median Quick Sort", bg="black", foreground="white", font=("Arial", 20)).pack()
    Label(quick3_window, text="Array", bg="black", foreground="white", font=("Arial", 10)).place(x=225, y=50)
    Label(quick3_window, text="______________________________", bg="black", foreground="white").place(x=273, y=60)
    textfield_label = Entry(quick3_window, bg="black", foreground="white", border=0, insertbackground="white")
    textfield_label.focus()
    textfield_label.bind("<Return>", quicksort3)
    textfield_label.place(x=275, y=50, height=20, width=150)
    search = Button(quick3_window, text="Sort", command=quicksort3_help).place(x=250, y=100, width=100)
    print(search)
    Label(quick3_window, text="Input", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=170)
    actual_array = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    actual_array.place(x=200, y=150)
    Label(quick3_window, text="Output", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=270)
    result = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    result.place(x=200, y=250)
    Label(quick3_window, text="Runtime", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=370)
    runtime = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    runtime.place(x=200, y=350)
    Label(quick3_window, text="Execution", font=("Arial", 15), bg="black", foreground="white").place(x=100, y=470)
    results = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    results.place(x=200, y=450)
    mainloop()


def graph_display():
    bubble = bubble_sorts()
    insertion = insertion_sorts()
    selection = selection_sorts()
    merge = mergesort_help()
    heap = heapsort_help()
    quick = quicksort_help()
    quick_3 = quicksort3_help()

    algorithms = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort", "Heap Sort", "Quick Sort",
                  "3 Median Quick Sort"]
    runtimes = [bubble, insertion, selection, merge, heap, quick, quick_3]

    plt.bar(algorithms, runtimes)
    plt.title("Runtime Comparison")
    plt.xlabel("Algorithms")
    plt.ylabel("Runtime")
    plt.show()
    fig = Figure(figsize=(10, 14), dpi=60)
    a = fig.add_subplot(111)
    a.bar(algorithms, runtimes)
    a.set_title("Runtime Comparison")
    a.set_ylabel("Runtime")
    a.set_xlabel("Algorithms")
    a.set_xticklabels(algorithms, rotation=45)
    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.get_tk_widget().place(x=50, y=150)
    canvas.draw()


def graphs_display():
    bubble = bubble_sorts()
    insertion = insertion_sorts()
    selection = selection_sorts()
    merge = mergesort_help()
    heap = heapsort_help()
    quick = quicksort_help()
    quick_3 = quicksort3_help()

    algorithms = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort", "Heap Sort", "Quick Sort",
                  "3 Median Quick Sort"]
    runtimes = [bubble, insertion, selection, merge, heap, quick, quick_3]

    plt.bar(algorithms, runtimes)
    plt.title("Runtime Comparison")
    plt.xlabel("Algorithms")
    plt.ylabel("Runtime")
    plt.show()
    fig = Figure(figsize=(10, 14), dpi=60)
    a = fig.add_subplot(111)
    a.bar(algorithms, runtimes)
    a.set_title("Runtime Comparison")
    a.set_ylabel("Runtime")
    a.set_xlabel("Algorithms")
    a.set_xticklabels(algorithms, rotation=45)
    canvas = FigureCanvasTkAgg(fig, master=graphs_window)
    canvas.get_tk_widget().place(x=50, y=150)
    canvas.draw()


def randomornot():
    global ran_window
    window.destroy()
    ran_window = Tk()
    ran_window.geometry("600x600")
    ran_window.config(bg="black")
    ran_window.title("Graph Comparison")
    Button(ran_window, text="Use Random 10 value array", wraplength=200, command=graph_ran).place(x=100, y=250, width=150, height=50)
    Button(ran_window, text="Give User Input", command=graph).place(x=350, y=250, width=150, height=50)


def graph():
    global textfield_label, actual_array, runtime, result, results, graph_window
    textfield_label = StringVar()
    ran_window.destroy()
    graph_window = Tk()
    graph_window.geometry("1000x1000")
    graph_window.config(bg="black")
    graph_window.title("Graph")
    Button(graph_window, text="<", bg="black", foreground="white", font=("Arial", 15), border=0,
           command=lambda: goback(graph_window)).place(x=0, y=0, width=30)
    Label(graph_window, text="Algorithm Comparison", bg="black", foreground="white", font=("Arial", 20)).pack()
    Label(graph_window, text="Array", bg="black", foreground="white", font=("Arial", 10)).place(x=225, y=50)
    Label(graph_window, text="______________________________", bg="black", foreground="white").place(x=273, y=60)
    textfield_label = Entry(graph_window, bg="black", foreground="white", border=0, insertbackground="white")
    textfield_label.focus()
    textfield_label.place(x=275, y=50, height=20, width=150)
    search = Button(graph_window, text="Run", command=graph_display).place(x=250, y=100, width=100)
    print(search)
    result = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    result.place(x=200, y=250)
    runtime = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    runtime.place(x=200, y=350)
    results = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    results.place(x=200, y=450)
    actual_array = tkinter.Canvas(bg='black', width='800', height='500', highlightthickness=0)
    actual_array.place(x=0, y=150)
    actual_arrays = tkinter.Canvas(bg='black', width='800', height='800', highlightthickness=0)
    actual_arrays.place(x=0, y=150)


def graph_ran():
    global textfield_label, actual_array, runtime, result, results, graphs_window
    textfield_label = StringVar()
    ran_window.destroy()
    graphs_window = Tk()
    graphs_window.geometry("1000x1000")
    graphs_window.config(bg="black")
    graphs_window.title("Graph")
    Button(graphs_window, text="<", bg="black", foreground="white", font=("Arial", 15), border=0,
           command=lambda: goback(graphs_window)).place(x=0, y=0, width=30)
    Label(graphs_window, text="Algorithm Comparison", bg="black", foreground="white", font=("Arial", 20)).pack()
    numbers = []
    for value in range(0, 10):
        numbers.append(str(random.randint(0, 100)))

    str_num = ",".join(numbers)
    print(str_num)
    textfield_label = Entry(graphs_window, bg="black", foreground="white", border=0,
                            insertbackground="white")
    textfield_label.insert(END, str_num)
    textfield_label.focus()
    Label(graphs_window, text=str_num, bg="black", foreground="white", font=("Arial",10)).pack()
    search = Button(graphs_window, text="Run", command=graphs_display).pack()
    print(search)
    textfield_label.place(x=275, y=250, height=20, width=150)
    result = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    result.place(x=200, y=250)
    runtime = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    runtime.place(x=200, y=350)
    results = tkinter.Canvas(bg='black', width='800', height='100', highlightthickness=0)
    results.place(x=200, y=450)
    actual_array = tkinter.Canvas(bg='black', width='800', height='500', highlightthickness=0)
    actual_array.place(x=0, y=150)
    actual_arrays = tkinter.Canvas(bg='black', width='800', height='800', highlightthickness=0)
    actual_arrays.place(x=0, y=150)


if __name__ == "__main__":
    def mainwindow():
        global window
        window = Tk()
        window.geometry("800x600")
        window.title("Sorting algorithms")
        window.config(bg="black")
        head = Label(window, text="Sorting Algorithms", bg="black", foreground="white", font=("Arial", 25)).pack()
        bubble_sort = Button(window, text="Bubble Sort", command=bubble_sort_window, bg="white", borderwidth=2).place(x=200, y=100, height=50, width=150)
        insertion_sort = Button(window, text="Insertion sort", command=insertion_sort_window, bg="white", borderwidth=2).place(x=500, y=100, height=50, width=150)
        selection_sort = Button(window, text="Selection Sort", command=selection_sort_window, bg="white", borderwidth=2).place(x=200, y=200, height=50, width=150)
        merge_sort = Button(window, text="Merge Sort", command=merge_sort_window, bg="white", borderwidth=2).place(x=500, y=200, height=50, width=150)
        heap_sort = Button(window, text="Heap Sort", command=heap_sort_window, bg="white", borderwidth=2).place(x=200, y=300, height=50, width=150)
        quick_sort = Button(window, text="Quick Sort", command=quick_sort_window, bg="white", borderwidth=2).place(x=500, y=300, height=50, width=150)
        median3_quicksort = Button(window, text="3 Median Quick Sort", command=quick3_sort_window, bg="white", borderwidth=2).place(x=200, y=400, height=50, width=150)
        graphs = Button(window, text="Graph Comparison", command=randomornot, bg="white", borderwidth=2).place(x=500, y=400, height=50, width=150)
        window.mainloop()
    mainwindow()