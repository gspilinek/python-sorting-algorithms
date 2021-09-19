import random
import timeit
import math
ArrayLength = 1000


class NumbersToSort:

    def __init__(self):
        self.list_of_ints = [0]*ArrayLength
        for x in range(0, len(self.list_of_ints)):
            self.list_of_ints[x] = random.randrange(ArrayLength)

    def randomize(self):
        for x in range(0, len(self.list_of_ints)):
            newspot = random.randrange(ArrayLength)
            temp = self.list_of_ints[x]
            self.list_of_ints[x] = self.list_of_ints[newspot]
            self.list_of_ints[newspot] = temp

    def printlist(self):
        for x in range(0, ArrayLength):
            print(self.list_of_ints[x], end=" ")
        print()

    def bubblesort(self):
        starttime = timeit.default_timer()
        for x in range(len(self.list_of_ints)):
            for y in range(ArrayLength - x - 1):
                if self.list_of_ints[y] > self.list_of_ints[y+1]:
                    self.list_of_ints[y+1], self.list_of_ints[y] = self.list_of_ints[y], self.list_of_ints[y+1]
        stoptime = timeit.default_timer()
        print("(" + str(stoptime - starttime), end=" secs): ")

    def selectionsort(self):
        starttime = timeit.default_timer()
        start = 0
        while start < ArrayLength:
            minimum = [self.list_of_ints[start], start]
            for x in range(start+1, ArrayLength):
                if self.list_of_ints[x] < minimum[0]:
                    minimum[0] = self.list_of_ints[x]
                    minimum[1] = x

            self.list_of_ints[minimum[1]] = self.list_of_ints[start]
            self.list_of_ints[start] = minimum[0]
            start += 1
        stoptime = timeit.default_timer()
        print("(" + str(stoptime - starttime), end=" secs): ")

    def gnomesort(self):
        starttime = timeit.default_timer()
        pos = 0
        while pos < ArrayLength:
            if pos == 0 or self.list_of_ints[pos] >= self.list_of_ints[pos-1]:
                pos += 1
            else:
                self.list_of_ints[pos], self.list_of_ints[pos-1] = self.list_of_ints[pos-1], self.list_of_ints[pos]
                pos -= 1
        stoptime = timeit.default_timer()
        print("(" + str(stoptime - starttime), end=" secs): ")

    def insertionsort(self):
        starttime = timeit.default_timer()
        i = 1
        while i < ArrayLength:
            j = 1
            while j > 0 and self.list_of_ints[j-1] > self.list_of_ints[j]:
                self.list_of_ints[j], self.list_of_ints[j-1] = self.list_of_ints[j-1], self.list_of_ints[j]
                j -= 1
            i += 1
        stoptime = timeit.default_timer()
        print("(" + str(stoptime - starttime), end=" secs): ")

    def quicksort(self, low, high):
        starttime = timeit.default_timer()
        size = high - low + 1
        stack = [0] * size

        top = -1

        top += 1
        stack[top] = low
        top += 1
        stack[top] = high

        while top >= 0:

            high = stack[top]
            top -= 1
            low = stack[top]
            top -= 1

            p = partition(self.list_of_ints, low, high)

            if p - 1 > low:
                top += 1
                stack[top] = low
                top += 1
                stack[top] = p - 1

            if p + 1 < high:
                top += 1
                stack[top] = p + 1
                top += 1
                stack[top] = high
        stoptime = timeit.default_timer()
        print("(" + str(stoptime - starttime), end=" secs): ")


def partition(numlist, low, high):
    i = low - 1
    x = numlist[high]
    for j in range(low, high):
        if numlist[j] <= x:
            i += 1
            numlist[i], numlist[j] = numlist[j], numlist[i]
    numlist[i+1], numlist[high] = numlist[high], numlist[i+1]
    return i + 1


def main():
    l = NumbersToSort()
    l.randomize()

    # bubble sort
    print("random: ", end=" ")
    l.printlist()
    print("bubble sort", end=" ")
    l.bubblesort()
    l.printlist()
    l.randomize()

    # selection sort
    print("random: ", end=" ")
    l.printlist()
    print("selection sort", end=" ")
    l.selectionsort()
    l.printlist()
    l.randomize()

    # gnome sort
    print("random: ", end=" ")
    l.printlist()
    print("gnome sort", end=" ")
    l.gnomesort()
    l.printlist()
    l.randomize()

    # insertion sort
    print("random: ", end=" ")
    l.printlist()
    print("insertion sort", end=" ")
    l.insertionsort()
    l.printlist()
    l.randomize()

    # quick sort
    print("random: ", end=" ")
    l.printlist()
    print("quick sort iterative", end=" ")  # my instance of python had a limit on recursion depth
    l.quicksort(0, ArrayLength-1)
    l.printlist()
    l.randomize()


if __name__ == '__main__':
    main()

