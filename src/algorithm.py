
def bubble_sort(array):
    l = len(array)
    for i in range(l):
        swap = False

        for j in range(0, l-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swap = True
        if swap == False:
            break
    return array


def merge_sort(array):
    # Divide the array into 2 parts
    if len(array) > 1:
        right = array[:(len(array)//2)]
        left = array[(len(array)//2):]
    # call merge_sort on each array
        merge_sort(right)
        merge_sort(left)
    # Loop while both arrays still have elements
    # Create a temp array
    # Compare the first element and move to temp array
    # Move pointer to the next location if any element is moved to the temp array
    # Move pointer of the temp array
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
    # check if there are any left
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array


def quick_sort(array):
    def partition(array, low, high):
        left_index = low + 1
        right_index = high
        pivot = array[low]

        done_flag = False

        while not done_flag:
            while left_index <= right_index and array[left_index] <= pivot:
                left_index += 1
            while array[right_index] > pivot and right_index >= left_index:
                right_index -= 1

            if right_index < left_index:
                done_flag = True
            else:
                array[left_index], array[right_index] = array[right_index], array[left_index]

        array[right_index], array[low] = array[low], array[right_index]
        return right_index

    def helper(array, low, high):
        if low < high:
            pivot_element = partition(array, low, high)
            helper(array, low, pivot_element - 1)
            helper(array, pivot_element + 1, high)

    helper(array, 0, len(array) - 1)
    return array
