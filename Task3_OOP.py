# TASK 3 #

# utility function from Appendix D - to check if the value is an integer
# it validates input when creating a Heap_numbers object
def is_int(value):
    return isinstance(value, int)

# define Heap_numbers class - to store numbers that can be sorted later
class Heap_numbers:
    def __init__(self, data):
        # check if all elements in the input list are integers
        if not all(is_int(x) for x in data):
            raise TypeError('All elements must be integers.')
        # make a copy of the list so the original isn’t modified
        self.data = data[:]
        # convert the list into a max heap right after initialization
        self.heapify()

    # get index of left child
    def left(self, index):
        return 2 * index + 1

    # get index of right child
    def right(self, index):
        return 2 * index + 2

    # move elements down the heap
    def move_down(self, index, heap_size):
        largest = index # assume that current node is the largest
        left = self.left(index)
        right = self.right(index)

        # compare with left child, if it's within bounds and larger
        if left < heap_size and self.data[left] > self.data[largest]:
            largest = left
        # compare with right child, if it's within bounds and larger
        if right < heap_size and self.data[right] > self.data[largest]:
            largest = right
        # if the largest is not the current node, swap and continue moving down
        if largest != index:
            # swap and continue
            self.data[index], self.data[largest] = self.data[largest], self.data[index]
            self.move_down(largest, heap_size)

    # turn the list into a max heap
    def heapify(self):
        # start from the last parent node and move up to the root
        for i in range(len(self.data) // 2 -1, -1, -1):
            self.move_down(i, len(self.data))

    # sort the elements using heapsort algorithm and return the sorted list
    def heapsort(self):
        sorted_list = self.data[:]
        n = len(sorted_list)

        # build a max heap that's already done by heapify
        for i in range(n // 2 - 1, -1, -1):
            self.move_down(i, n)

        # extract the maximum element and move it to the end, then fix the heap
        for i in range(n - 1, 0, -1):
            # swap the root (max) with the last unsorted element
            sorted_list[0], sorted_list[i] = sorted_list[i], sorted_list[0]
            # move down new root to restore the heap
            self._move_down_static(sorted_list, 0, i)
        return sorted_list # list is sorted in ascending order

    # static version of move_down used for heapsort
    # works on a given list without modifying self.data
    def _move_down_static(self, data, index, heap_size):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        # compare with left and right children
        if left < heap_size and data[left] > data[largest]:
            largest = left
        if right < heap_size and data[right] > data[largest]:
            largest = right

        # if needed swap, and continue moving down
        if largest != index:
            data[index], data[largest] = data[largest], data[index]
            self._move_down_static(data, largest, heap_size)

    # remove all numbers greater than x
    def remove_greater_than(self, x):
        if not is_int(x):
            raise TypeError('x must be an integer.')
        # keep only numbers less than or equal to x
        self.data = [num for num in self.data if num <= x]
        # rebuild the heap after modifying the data
        self.heapify()

# example usage of the code
nums = [20, 14, 35, 9, 42, 18]
heap = Heap_numbers(nums)

print('Original heapified data:', heap.data)
print('Sorted:', heap.heapsort())

heap.remove_greater_than(20)
print('After removing numbers > 20:', heap.data)