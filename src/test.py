from algorithm import bubble_sort, quick_sort, merge_sort
from random import randint


def test_algorithm():
    for i in range(10):
        print(f"Test {i+1}")
        array = [randint(10, 99) for x in range(55)]
        test_bubble = bubble_sort(array)
        test_merge = merge_sort(array)
        test_quick = quick_sort(array)
        assert(test_bubble == sorted(array))
        assert(test_merge == sorted(array))
        assert(test_quick == sorted(array))


test_algorithm()
