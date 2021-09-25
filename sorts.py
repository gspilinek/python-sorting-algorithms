#written by gerald spilinek
#last updated 09/25/2021

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

    def gnomesort(self):#also listed as stupid sort on wikipedia
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

    def insertionsort(self,low,high): 
        i = low+1
        while i < high:
            x = self.list_of_ints[i]
            j = i-1
            while j >= 0 and self.list_of_ints[j] > x:
                self.list_of_ints[j+1] = self.list_of_ints[j]
                j = j - 1
            self.list_of_ints[j+1] = x
            i = i + 1
       
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

    def quicksortprime(self,low,high): #becomes faster than regular quicksort by 1000+
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
            
            if high - low < 15:
                self.insertionsort(low,high)
            else:
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
    print("bubble sort", end=" ")
    l.bubblesort()
    print()
    #l.printlist()
    l.randomize()

    # selection sort
    print("selection sort", end=" ")
    l.selectionsort()
    print()#l.printlist()
    l.randomize()

    # gnome sort
    print("gnome sort", end=" ")
    l.gnomesort()
    print()
    #l.printlist()
    l.randomize()

    # insertion sort
    print("insertion sort", end=" ")
    starttime = timeit.default_timer()
    l.insertionsort(0,ArrayLength)
    stoptime = timeit.default_timer()
    print("(" + str(stoptime - starttime), end=" secs): ")

    print()
    #l.printlist()
    l.randomize()

    # quick sort
    print("quick sort iterative", end=" ")  # my instance of python had a limit on recursion depth
    l.quicksort(0, ArrayLength-1)
    print()
    #l.printlist()
    l.randomize()
    
    #quick & insertion combo sort
    print("quick & insertion combo", end=" ") 
    starttime = timeit.default_timer() 
    l.quicksortprime(0, ArrayLength-1)
    stoptime = timeit.default_timer()
    print("(" + str(stoptime - starttime), end=" secs): ")
    print()
    #l.printlist()
    l.randomize()


if __name__ == '__main__':
    main()
