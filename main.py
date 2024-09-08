import tkinter as tk
from tkinter import ttk
import random

# Function to draw the bars on the canvas
def draw_graph(data, color_array):
    canvas.delete("all")
    canvas_height = 380
    canvas_width = 600
    bar_width = canvas_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalized_data = [i / max(data) for i in data]

    for i, height in enumerate(normalized_data):
        x0 = i * bar_width + offset + spacing
        y0 = canvas_height - height * 340
        x1 = (i + 1) * bar_width + offset
        y1 = canvas_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
        canvas.create_text(x0 + 2, y0, anchor=tk.SW, text=str(data[i]))

    root.update_idletasks()

# Bubble sort implementation
def bubble_sort(data, draw, speed):
    for _ in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw(data, ['#ff5555' if x == j or x == j + 1 else '#a1c4fd' for x in range(len(data))])
                root.after(speed_scale.get())  # No need for multiplication
                root.update()

    draw(data, ['#a1c4fd' for x in range(len(data))])

# Insertion sort implementation
def insertion_sort(data, draw, speed):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            draw(data, ['#ff5555' if x == j or x == i else '#a1c4fd' for x in range(len(data))])
            root.after(speed_scale.get())  # No need for multiplication
            root.update()
        data[j + 1] = key
    draw(data, ['#a1c4fd' for x in range(len(data))])

# Selection sort implementation
def selection_sort(data, draw, speed):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        draw(data, ['#ff5555' if x == min_idx or x == i else '#a1c4fd' for x in range(len(data))])
        root.after(speed_scale.get())  # No need for multiplication
        root.update()
    draw(data, ['#a1c4fd' for x in range(len(data))])

# Merge sort implementation
def merge_sort(data, left, right, draw, speed):
    if left < right:
        mid = (left + right) // 2
        merge_sort(data, left, mid, draw, speed)
        merge_sort(data, mid + 1, right, draw, speed)
        merge(data, left, mid, right, draw, speed)

def merge(data, left, mid, right, draw, speed):
    left_part = data[left:mid + 1]
    right_part = data[mid + 1:right + 1]

    left_idx = right_idx = 0
    sorted_idx = left

    while left_idx < len(left_part) and right_idx < len(right_part):
        if left_part[left_idx] <= right_part[right_idx]:
            data[sorted_idx] = left_part[left_idx]
            left_idx += 1
        else:
            data[sorted_idx] = right_part[right_idx]
            right_idx += 1
        sorted_idx += 1
        draw(data, get_color_array(len(data), left, mid, right, sorted_idx))
        root.after(speed_scale.get())  # No need for multiplication
        root.update()

    while left_idx < len(left_part):
        data[sorted_idx] = left_part[left_idx]
        left_idx += 1
        sorted_idx += 1
        draw(data, get_color_array(len(data), left, mid, right, sorted_idx))
        root.after(speed_scale.get())  # No need for multiplication
        root.update()
        
    while right_idx < len(right_part):
        data[sorted_idx] = right_part[right_idx]
        right_idx += 1
        sorted_idx += 1
        draw(data, get_color_array(len(data), left, mid, right, sorted_idx))
        root.after(speed_scale.get())  # No need for multiplication
        root.update()

def get_color_array(length, left, mid, right, curr_index):
    color_array = []
    for i in range(length):
        if left <= i <= right:
            if i <= mid:
                color_array.append('#ff5555')  # Red for left part
            else:
                color_array.append('#ff5555')  # Red for right part
        else:
            color_array.append('#a1c4fd')  # Blue for sorted part
    return color_array


# Quick sort implementation
def quick_sort(arr, start, end, draw, speed):
    if start < end:
        pivot_index = partition(arr, start, end, draw, speed)
        quick_sort(arr, start, pivot_index - 1, draw, speed)
        quick_sort(arr, pivot_index + 1, end, draw, speed)

def partition(arr, start, end, draw, speed):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        draw(arr, ['#ff5555' if x == i or x == j else '#a1c4fd' for x in range(len(arr))])
        root.after(speed_scale.get())  # No need for multiplication
        root.update()
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    draw(arr, ['#ff5555' if x == i + 1 or x == end else '#a1c4fd' for x in range(len(arr))])
    return i + 1

# Function to start sorting
def start_sorting():
    global data
    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, draw_graph, speed_scale.get())
    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort(data, draw_graph, speed_scale.get())
    elif algo_menu.get() == 'Selection Sort':
        selection_sort(data, draw_graph, speed_scale.get())
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data) - 1, draw_graph, speed_scale.get())  # Corrected function call
    elif algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data) - 1, draw_graph, speed_scale.get())


# Function to generate a new array
def generate_array():
    global data
    data = [random.randint(1, 100) for _ in range(int(size_scale.get()))]
    draw_graph(data, ['#a1c4fd' for x in range(len(data))])

# UI setup
root = tk.Tk()
root.title("Sorting Algorithm Visualization")
root.maxsize(900, 600)
root.config(bg="#333333")

# Frame for user interface
UI_frame = tk.Frame(root, width=600, height=200, bg="#333333")
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# Dropdown menu to select sorting algorithm
algo_menu = ttk.Combobox(UI_frame, values=['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort'])
algo_menu.grid(row=0, column=0, padx=5, pady=5)
algo_menu.current(0)

# Slider for array size
size_scale = tk.Scale(UI_frame, from_=3, to=30, resolution=1, orient=tk.HORIZONTAL, label="Size of Array", bg="#333333", fg="white")
size_scale.grid(row=0, column=1, padx=5, pady=5)

# Slider for sorting speed
speed_scale = tk.Scale(UI_frame, from_=1, to=1000, resolution=1, orient=tk.HORIZONTAL, label="Select Speed [ms]", bg="#333333", fg="white")
speed_scale.grid(row=0, column=2, padx=5, pady=5)

# Button to generate array
generate_button = tk.Button(UI_frame, text="Generate Array", command=generate_array, bg="#4CAF50", fg="white")
generate_button.grid(row=1, column=0, padx=5, pady=5)

# Button to start sorting
start_button = tk.Button(UI_frame, text="Start Sorting", command=start_sorting, bg="#FF5722", fg="white")
start_button.grid(row=1, column=1, padx=5, pady=5)

# Canvas for drawing the array bars
canvas = tk.Canvas(root, width=600, height=380, bg="#333333")
canvas.grid(row=1, column=0, padx=10, pady=5)

root.mainloop()
