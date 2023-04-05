# Sorting Vizualizer
This is a sorting visualizer made in Pygame, which allows users to see how different sorting algorithms work on an array of values. The visualizer can be run on any computer with Python 3 and Pygame installed.

## Features
* Supports various sorting algorithms such as Bubble Sort, Quick Sort, Merge Sort, and Radix Sort
* User can adjust the size of the array and the speed of the visualization
* Color-coded visual display of the sorting process
* Real-time updates of the sorting process

## Getting Started
To use this program, you will beed to have Python3 and Pygame installed on your computer. You can install Python3 by heading to this website: https://www.python.org/downloads/

To install Pygame, use the following command:
```
pip install pygame
```

Once installed, download the git repo and navigate to the directory:
```
git clone https://github.com/gnoixs/pathfinder.git
```

You can run the program using the following command:
```
python main.py
```

## Algorithms
This program supports the following sorting algorithms:

* Bubble Sort: A simple comparison-based algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. It has a worst-case and average-case complexity of O(n^2).

* Counting Sort: An integer sorting algorithm that works by determining the number of elements that have a distinct key value in the input array. It has a linear time complexity of O(n + k), where k is the range of the non-negative key values.

* Heap Sort: A comparison-based sorting algorithm that uses a binary heap data structure to sort elements. It has an average-case and worst-case complexity of O(n log n).

* Insertion Sort: A simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. It has an average-case and worst-case complexity of O(n^2).

* Merge Sort: A divide-and-conquer algorithm that works by recursively splitting the input array into smaller sub-arrays, sorting them, and merging them back together. It has a worst-case and average-case complexity of O(n log n).

* Quick Sort: Another divide-and-conquer algorithm that works by selecting a pivot element from the array, partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot, and recursively sorting the sub-arrays. It has an average-case complexity of O(n log n) but can have a worst-case complexity of O(n^2) if the pivot is consistently poorly chosen.

* Radix Sort: A non-comparison integer sorting algorithm that works by grouping elements by their individual digits or bytes. It has a linear time complexity of O(nk), where k is the number of passes of the sort.

* Selection Sort: A simple comparison-based algorithm that repeatedly selects the smallest remaining unsorted element and swaps it with the leftmost unsorted element. It has an average-case and worst-case complexity of O(n^2).

## Bugs
When running the program, you will be asteriks(*) with some of the algorithms. These aglorithms have bugs or have yet to be impletemented.

## Usage
To use this program, fow these steps:
1. Select sorting algorithm
2. Choose size of list
3. Select start

## Example

## License
MIT License

Copyright (c) [2020] [Samantha Xiong]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.