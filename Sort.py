def merge(lst1, lst2):
    rtn_lst = []
    i = j = 0
    total_size = len(lst1) + len(lst2)

    while i + j < total_size:
        if (j == len(lst2)) or (i < len(lst1) and lst1[i] <= lst2[j]):
            rtn_lst.append(lst1[i])
            i += 1
        else:
            rtn_lst.append(lst2[j])
            j += 1

    return rtn_lst


def merge_sort(lst):
    lst_length = len(lst)

    if lst_length < 2:
        return lst

    mid = lst_length // 2

    lst1 = lst[:mid]
    lst2 = lst[mid:lst_length]

    return merge(merge_sort(lst1), merge_sort(lst2))


################################################

def partition(lst, start, end):
    pivot = lst[end]

    i = start - 1

    for j in range(start, end):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[i + 1], lst[end] = lst[end], lst[i + 1]

    return i + 1


def quick_sort(lst, start, end):
    if len(lst) < 2:
        return lst

    if start < end:
        index = partition(lst, start, end)
        quick_sort(lst, start, index - 1)
        quick_sort(lst, index + 1, end)

    return lst


#####################################################################

# order => left < root < right
def maxHeap(lst, heap_size, root_index):
    left = 2 * root_index + 1
    right = 2 * root_index + 2

    if left < heap_size and lst[root_index] < lst[left]:
        largest = left
    elif right < heap_size and lst[root_index] < lst[right]:
        largest = right
    else:
        largest = root_index

    # keep swapping until satisfy heap invariant
    if largest != root_index:
        lst[root_index], lst[largest] = lst[largest], lst[root_index]
        maxHeap(lst, heap_size, largest)


# list is zero based indexing
def heap_sort(lst):
    mid = len(lst) - 1 // 2

    # create BinaryHeap - bubble_up
    for i in range(mid, -1, -1):
        maxHeap(lst, mid, i)

    # root is max, get max value from index then re-arrange rest of the heap (bubble_down)
    # to satisfy heap invariant then iterate index
    heap_size = len(lst)
    for i in range(heap_size - 1, -1, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heap_size -= 1
        maxHeap(lst, heap_size, 0)

    return lst


########################################################

def bubble_sort(lst):
    for i in range(len(lst)):  # for each item
        for j in range(0, len(lst) - i - 1):  # compare rest of the list
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


#########################################################
# find smallest then put at beginning for each iteration
def selection_sort(lst):
    for i in range(len(lst)):
        min = i

        for j in range(i + 1, len(lst)):
            if lst[min] > lst[j]:
                min = j

        lst[i], lst[min] = lst[min], lst[i]

    return lst

#############################################################
# pick key current index + 1, then iterate through list, compare key with each item to find smaller
# then insert key
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]

        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = key

    return lst