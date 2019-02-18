
def insertionSort(lst):
    # Run through a list with indexes i,
    # introduce each i into "completed" part of the list.
    # When introducing each i, insert it relative to its
    # position amongst the other elements
    for i in range(len(lst)):
        j = i
        while(j > 0 and (lst[j] < lst[j-1])):
            temp = lst[j]
            lst[j] = lst[j-1]
            lst[j-1] = temp
            j = j - 1
    return lst

def selectionSort(lst):
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
            
            
a = [6, 4, 3, 9, 1, 0, 10]
print(insertionSort(a))
print(selectionSort(a))

# I understand arrays in Python are really just cleverly disguised
# lists. However for the intentions of these exercises, I will be
# treating them seperately.
# Python lists will represent arrays commonly found in languages
# such as C or Java.
# These self-defined lists will represent lists that would otherwise
# have to be defined by the programmer in these other non-Python
# langauges
class Node:
    def __init__(self, value, nxt):
        self.val = value
        self.nxt = nxt

# Make a list given a Python array/list/red-headed-stepchild
def recMakeList(arr):
    if(not arr):
        return None
    return Node(arr[0], recMakeList(arr[1:]))

def search(l, val, index=0):
    if(not l):
        return -1
    if(l.val == val):
        return index
    else:
        return search(l.nxt, val, index+1)

def insert()
    
a = makeList()
print(search(a, 4))
