#!/usr/bin/env python3

from unittest import TestCase
from script import Publication
# from their_script import Publication

class PublicTestSuite(TestCase):

    def test_example(self):
        a = Publication(["A"], "B", 1234)
        b = Publication(["A"], "B", 1234)
        self.assertEqual(a, b)

    ref1 = [
        Publication(["Gamma", "Helm", "Johnson", "Vlissides"], "Design Patterns", 1994),
        Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
        Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    ]

    ref2 = [
        Publication(["Gamma"], "Design Patterns", 1994),
        Publication(["Gamma"], "Writing Effective Use Cases", 2000),
        Publication(["Gamma"], "Continuous Integration", 2007)
    ]

    ref3 = [
        Publication(["Gamma"], "Design Patterns", 1994),
        Publication(["Gamma"], "Design Patterns", 2000),
        Publication(["Gamma"], "Design Patterns", 2007)
    ]

    def test_same_objects(self):
        a = Publication(["A"], "B", 1234)
        b = Publication(["A"], "B", 1234)
        self.assertEqual(a, b)

    def test_NOTsame_objects(self):
        a = Publication(["A"], "B", 1235)
        b = Publication(["A"], "B", 1234)
        self.assertNotEqual(a, b)

    '''
    All the other 5 operator cases.
    '''

    def test_GT_EQ(self):
        a = Publication(["A"], "B", 1235)
        b = Publication(["A"], "B", 1235)
        self.assertGreaterEqual(a, b)

    def test_LT_EQ(self):
        a = Publication(["A"], "B", 1232)
        b = Publication(["A"], "B", 1235)
        self.assertLessEqual(a, b)

    def test_GT_Year(self):
        T = PublicTestSuite()
        a = T.ref3[0]
        b = T.ref3[1]
        self.assertGreater(b, a)

    def test_LT_Year(self):
        T = PublicTestSuite()
        a = T.ref3[0]
        b = T.ref3[1]
        self.assertLess(a, b)

    def test_GT_Titles(self):
        T = PublicTestSuite()
        a = T.ref2[0]
        b = T.ref2[1]
        self.assertGreater(b, a)

    def test_GT_Titles_SIMPLE(self):
        a = Publication(["A"], "B", 1232)
        b = Publication(["A"], "AB", 1235)
        self.assertGreater(b, a)

    def test_LT_Titles(self):
        T = PublicTestSuite
        a = T.ref2[0]
        b = T.ref2[1]
        self.assertLess(a, b)

    def test_GT_Authors(self):
        T = PublicTestSuite()
        a = T.ref1[0]
        b = T.ref1[1]
        self.assertGreater(a, b)

    def test_GT_Authors(self):
        T = PublicTestSuite()
        a = T.ref1[0]
        b = T.ref1[1]
        self.assertLess(b, a)

    '''
    Special cases
    '''

    def test_dic(self):
        p1 = Publication(["A"], "B", 1234)
        d = {p1: 300}
        a = d[p1]
        b = 300
        self.assertEqual(b, a)

    def test_string_output(self):
        p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
        s = "Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"
        a = str(p)
        b = s
        self.assertEqual(a, b)

    def test_mutability_authors(self):
        T = PublicTestSuite()
        a = T.ref1[0].get_authors().copy()
        T.ref1[0].get_authors().append("John")
        self.assertEqual(a, T.ref1[0].get_authors())


# github


    def test_to_stringN(self):
        pub = Publication(["Duvall", "Matyas"], "Continuous Integration", 2007)
        self.assertEqual(
            str(pub), "Publication([\"Duvall\", \"Matyas\"], \"Continuous Integration\", 2007)")

    def test_equalN(self):
        a = Publication(["A"], "B", 1234)
        b = Publication(["A"], "B", 1234)
        self.assertEqual(a, b)

    def test_not_equalN(self):
        a = Publication(["A"], "B", 1234)
        b = Publication(["B"], "C", 2345)
        self.assertNotEqual(a, b)


    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly ecncourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
