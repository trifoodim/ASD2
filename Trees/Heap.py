class Heap:

    def __init__(self):
        self.HeapArray = []
        self.__capacity = 0
        self.__size = 0

    def MakeHeap(self, a, depth):
        self.__capacity = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * self.__capacity
        self.__size = 0
        for key in a:
            self.Add(key)

    def GetMax(self):
        if self.__size == 0:
            return -1
        if self.__size == 1:
            return self.__get_last()

        root = self.HeapArray[0]
        self.HeapArray[0] = self.__get_last()
        self.__sift_down(0)
        return root

    def Add(self, key):
        if self.__size == self.__capacity:
            return False
        self.__add_to_end(key)
        self.__sift_up(self.__size - 1)
        return True

    def __get_last(self):
        self.__size -= 1
        key = self.HeapArray[self.__size]
        self.HeapArray[self.__size] = None
        return key

    def __sift_down(self, index):
        left = _left_child_index(index)
        if left >= self.__size:
            return
        right = _right_child_index(index)
        go_left = right >= self.__size or self.HeapArray[right] < self.HeapArray[left]
        target = left if go_left else right

        if self.__fix_order(index, target):
            self.__sift_down(target)

    def __add_to_end(self, key):
        self.HeapArray[self.__size] = key
        self.__size += 1

    def __sift_up(self, index):
        if index == 0:
            return
        parent = _parent_index(index)
        if self.__fix_order(parent, index):
            self.__sift_up(parent)

    def __fix_order(self, parent, child):
        if self.HeapArray[parent] > self.HeapArray[child]:
            return False
        self.__swap(parent, child)
        return True

    def __swap(self, i1, i2):
        tmp = self.HeapArray[i1]
        self.HeapArray[i1] = self.HeapArray[i2]
        self.HeapArray[i2] = tmp


def _left_child_index(i):
    return 2 * i + 1


def _right_child_index(i):
    return 2 * i + 2


def _parent_index(i):
    return (i - 1) // 2
