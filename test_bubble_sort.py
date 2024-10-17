import unittest
from bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        bubble_sort(arr)
        self.assertEqual(arr, [11, 12, 22, 25, 34, 64, 90])

    def test_single_element(self):
        arr = [42]
        bubble_sort(arr)
        self.assertEqual(arr, [42])

    def test_empty_array(self):
        arr = []
        bubble_sort(arr)
        self.assertEqual(arr, [])

if __name__ == "__main__":
    unittest.main()
