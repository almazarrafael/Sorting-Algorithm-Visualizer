import tkinter as tk
import time
import random

data1 = [random.randint(1,20) for _ in range(20)]
data2 = [random.randint(1,20) for _ in range(20)]

root = tk.Tk()
root.title("Sort Visualizer")

y_stretch = 15  # The highest y = max_data_value * y_stretch
y_gap = 20  # The gap between lower canvas edge and x axis
x_stretch = 10  # Stretch x wide enough to fit the variables
x_width = 20  # The width of the x-axis
x_gap = 20  # The gap between left canvas edge and y axis

c_width = len(data1) * (x_width + (x_gap * .6))  # Define it's width
c_height = 350  # Define it's height
c = tk.Canvas(root, width=c_width, height=c_height, bg = 'white')
c.pack()
label = tk.Label(root, text = "Bubble Sort", bg = "white")
label.place(relx = 0.05, rely = 0.05)

# The variables below size the bar graph


def main():
    heapSort(data1)
    c.delete("all")
    label = tk.Label(root, text = "Heap Sort", bg = "white")
    label.place(relx = 0.05, rely = 0.05)
    bubbleSort(data2)

def heapify(arr, n, i): 
    largest = i  # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 

def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        print(arr)
        time.sleep(0.1)
        c.delete("all")
        heapify(arr, i, 0) 
        print(arr)
        time.sleep(0.1)
        c.delete("all")

def bubbleSort(data):
    nlist = data
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
                print(nlist)
                time.sleep(0.1)
                c.delete("all")
                

def print(data):
    for x, y in enumerate(data):
        x0 = x * x_stretch + x * x_width + x_gap
        y0 = c_height - (y * y_stretch + y_gap)
        x1 = x * x_stretch + x * x_width + x_width + x_gap
        y1 = c_height - y_gap
        c.create_rectangle(x0, y0, x1, y1, fill="red")
        c.create_text(x0 + 2, y0, anchor=tk.SW, text=str(y))

    root.update_idletasks()
    root.update()

if __name__ == "__main__":
    main()
