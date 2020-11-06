# staticSort Copyright(C) 2020 thatsOven
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


# Copied and Pythonified from https://github.com/MusicTheorist/ArrayVisualizer/blob/master/src/templates/HeapSorting.java
# Min heap support was also removed
class MaxHeapSort:
    @classmethod
    def siftDown(cls, arr, root, dist, start):
        while root <= dist // 2:
            leaf = 2 * root
            if leaf < dist and arr[start + leaf - 1] < arr[start + leaf]:
                leaf += 1
            if arr[start + root - 1] < arr[start + leaf - 1]:
                arr[start + root - 1], arr[start + leaf - 1] = arr[start + leaf -1], arr[start + root - 1]
                root = leaf
            else:
                break

    @classmethod
    def heapify(cls, arr, low, high):
        length = high - low
        for i in range(length // 2, 0, -1):
            cls.siftDown(arr, i, length, low)

    @classmethod
    def sort(cls, arr, start, n):
        cls.heapify(arr, start, n)
        for i in range(n - start, 1, -1):
            arr[start], arr[start + i - 1] = arr[start + i - 1], arr[start]
            cls.siftDown(arr, 1, i - 1, start)


def insertion_sort(arr, n):
    for i in range(1, n):
        j = i-1
        key = arr[i]
        while (arr[j] > key) and (j >= 0):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def thatsOvens_staticSort(a):
    M = max(a)
    size = len(a)
    constant = M/(size+4)
    counter = 0
    listcount = 0
    while listcount < size:
        if type(a[counter]) is list:
            counter += 1
        else:
            if int(a[counter]*constant) == counter:
                a[counter] = [a[counter]]
            else:
                if type(a[int(a[counter]*constant)]) is list:
                    a[int(a[counter]*constant)].append(a[counter])
                    a[counter] = []
                else:
                    a[int(a[counter]*constant)], a[counter] = [a[counter]
                                                               ], a[int(a[counter]*constant)]
            listcount += 1
    for i in range(len(a)):
        lt = len(a[i])
        if lt > 1:
            if lt > 16:
                MaxHeapSort.sort(a[i], 0, lt)
            else:
                insertion_sort(a[i], lt)
    array_join(a)


def array_join(arr):
    i = 0
    while i < len(arr):
        count = len(arr[i])
        arr[i:i+1] = arr[i]
        i += count
