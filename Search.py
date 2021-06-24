def binary_search_recursive(lst, value):
    lower_bound, upper_bound = 0, len(lst) - 1

    if lower_bound <= upper_bound and lst[lower_bound] <= value and value <= lst[upper_bound]:

        mid = lower_bound + (upper_bound - lower_bound) // 2

        if lst[mid] < value:  # right half
            lower_bound = mid + 1
            return lower_bound + binary_search_recursive(lst[lower_bound:], value)  # lower_bound + BS determine index
        if lst[mid] > value:  # left half
            upper_bound = mid
            return binary_search_recursive(lst[:upper_bound], value)
        if lst[mid] == value:
            return mid

    return -1


def binary_search_iterative(lst, value):
    lower_bound, upper_bound = 0, len(lst) - 1

    while lower_bound <= upper_bound:

        mid = lower_bound + (upper_bound - lower_bound) // 2
        if lst[mid] < value:
            lower_bound = mid + 1
        if lst[mid] > value:
            upper_bound = mid - 1
        if lst[mid] == value:
            return mid

    return -1


############################################################################
# from Pseudocode
# mid = Lo + ((Hi - Lo) / (A[Hi] - A[Lo])) * (X - A[Lo])
#
# where −
#    A    = list
#    Lo   = Lowest index of the list
#    Hi   = Highest index of the list
#    A[n] = Value stored at index n in the list
def interpolation_search(lst, value):
    lower_bound, upper_bound = 0, len(lst) - 1

    if lower_bound <= upper_bound and lst[lower_bound] <= value and value <= lst[upper_bound]:
        try:
            mid = lower_bound + ((upper_bound - lower_bound) // (lst[upper_bound] - lst[lower_bound])) * \
                  (value - lst[lower_bound])
        except ZeroDivisionError:
            mid = 0

        if lst[mid] < value:  # right sub-list
            lower_bound = mid + 1
            return lower_bound + interpolation_search(lst[lower_bound:], value)  # lower_bound + IS determine index
        if lst[mid] > value:  # left sub-list
            upper_bound = mid
            return interpolation_search(lst[:upper_bound], value)
        if lst[mid] == value:
            return mid

    return -1
