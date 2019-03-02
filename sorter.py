# Now a more abstract idea, having an Object which does not represent
# a structure, but rather something that must perform some task.
# A bit bizzare in Python, but a very common design pattern in C#/Java
import copy

class Sorter:
    # Start with bubble sort if this is all a little alien. It's the
    # easiest to understand.
    
    def __init__(self):
        self.sortCount = 0

    def insertionSort(self, lst):
        for i in range(len(lst)):   # For each index (i) in lst,
            j = i                   # set j = i.
            while(j > 0 and (lst[j] < lst[j-1])): # while not sorted,
                temp = lst[j]       # switch the elements j and j-1
                lst[j] = lst[j-1]
                lst[j-1] = temp     # reduce j by one, and repeat again
                j = j - 1           # for the next i
        return lst
    
    def selectionSort(self, lst):
    # Run through a list, grab the smallest element each time
    # O(n^2) runtime complexity
        for i in range(len(lst)):
            mini = i
            for j in range(i+1, len(lst)):
                if(lst[j] < lst[mini]):
                    temp = lst[mini]
                    lst[mini] = lst[j]
                    lst[j] = temp
        return lst

    def bubbleSort(self, lstOriginal):
    # Iterate across a list, and "bubble up" the largest element to the
    # top of the list each time.
    # O(n^2) runtime (i.e. "not efficient")

        # A very common theme in my code is something referred to as
        # "referential transparency". Its not an accurate term, but
        # part of it is the idea that we want to mutate our parameters
        # as little as possible. In this example, I define a new
        # variable lst, which is a perfect copy of lstOriginal. That
        # way, I can make changes to lst without changing the original
        # list at all. The next definition is an example that DOES
        # mutate that parameter
        lst = copy.copy(lstOriginal)
        
        for i in range(len(lst)):
            for j in range(0,len(lst)-i-1):
                if(lst[j] > lst[j+1]):
                    temp = lst[j]
                    lst[j] = lst[j+1]
                    lst[j+1] = temp
        return lst

    def bubbleSortMutate(self, lst):
        # Whether or not you want to mutate things is purely a personal
        # preference. Like all inconsequential things, a nerd is going
        # to fight you over it regardless of whether or not it bears
        # any importance.
        for i in range(len(lst)):
            for j in range(0,len(lst)-i-1):
                if(lst[j] > lst[j+1]):
                    temp = lst[j]
                    lst[j] = lst[j+1]
                    lst[j+1] = temp
        # return lst # No need to return this, the original parameter
                     # has been changed instead


# A few important notes:
#    1) Python has a default sort method. We could call b.sort(),
#       and b would sort itself for us (very efficiently, nlog(n) time).
#       Calling b.sort does not RETURN the sorted list though.
#       I personally prefer when the item is returned, rather than
#       mutated in place. Python tends more towards mutation though.
#           >>> b = [5,6,1,5]
#           >>> b.sort()
#           >>> b
#           [1,5,5,6]
#
#    2) The fact that we have to call a = Sorter(), then a.Sort(list)
#       is entirely superfluous. It is perfectly acceptable to define
#       these sorts outside of a class (remeber to remove the SELF
#       parameter). I only do this to refamiliarize myself with how
#       C# and Java do things.
def test():
    a = Sorter()
    b = [5,4,6,1,8,2,9,10,3]
    print(a.insertionSort(b))
    print(a.selectionSort(b))
    print(a.bubbleSort(b))

    a.bubbleSortMutate(b)
    print(b)
