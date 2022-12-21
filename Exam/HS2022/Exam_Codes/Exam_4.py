def unique_sorted(values):
    return list(sorted(set(values), reverse=True))

from unittest import TestCase

class TestSuite(TestCase):
    
    def test_removes_duplicates_but_not_sort(self):
        a = unique_sorted(["A", "B", "C", "D", "E", "E", "E", "C"])
        b = ["A", "B", "D", "E", "C"]
        self.assertNotEqual(b, a)

    def test_empty_list(self):
        a = unique_sorted([])
        b = []
        self.assertEqual(b, a)
        c = unique_sorted(["A", "B", "C", "C"])
        d = ["C", "B", "A"]
        self.assertEqual(d, c)

    def test_duplicates_remain(self):
        a = unique_sorted(["A", "B", "C", "C"])
        b = ["C", "C", "B", "A"]
        self.assertNotEqual(b, a)





