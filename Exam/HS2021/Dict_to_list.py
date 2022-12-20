import unittest

def dict_to_lists(d):
    pass


class MyTestSuite(unittest.TestCase):
    def test_normal2(self):
        self.assertEqual((["a", "z"], [20, 1]), dict_to_lists({"a": 20, "z": 1}))
    
    def test_leng(self):
        l1, l2 = dict_to_lists({"a": 20, "z": 1})
        self.assertTrue(len(l1) == len(l2))

    def test_error(self):
        with self.assertRaises(TypeError):
            dict_to_lists([{"a":1}])
        
    def test_non_order(self):
        self.assertNotEqual((["a", "z"], [1, 20]), dict_to_lists({"a": 20, "z": 1}))

    def test_wrong_output(self):
        self.assertNotEqual([["a", "z"], [20, 1]], dict_to_lists({"a": 20, "z": 1}))
    
    def test_wrong_lists(self):
        self.assertNotEqual(([20, 1], ["a", "z"]), dict_to_lists({"a": 20, "z": 1}))
    



    
    
