import tkinter
from tkinter import *


def bubblesort():
    inparray = textfield_label.get()
    numbers_list = inparray.split(",")  # splitting the numbers with ","
    tobesorted = []
    min_index=0
    next_index=0
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


if __name__ == "__main__":
    window = Tk()
    window.geometry("600x600")
    window.title("Sorting algorithms")

    head = Label(window, text="Sorting Algorithm").pack()
    bubble_sort = Button(window, text="Bubble Sort", command=bubble_sort_window).pack()
    insertion_sort = Button(window, text="Insertion sort").pack()
    selection_sort = Button(window, text="Selection Sort").pack()
    merge_sort = Button(window, text="Merger Sort").pack()
    heap_sort = Button(window, text="Heap Sort").pack()
    quick_sort = Button(window, text="Quick Sort").pack()
    median3_quicksort = Button(window, text="3 Median Quick Sort").pack()
    window.mainloop()
