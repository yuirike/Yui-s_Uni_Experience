#!/usr/bin/env python3

from unittest import TestCase
from script import analyze

# This test suite does not exhaustively test the implementation,
# a passing "test & run" does not mean that all possible cases
# have been considered. For the grading, an extended tests suite
# will be executed that will cover many more cases.

# Feel free to add additional test cases here. All test cases
# will be executed as part of the "Test & Run".

from their_script import analyze2
from script import analyze

class PublicTestSuite(TestCase):

    def test_1(self):
        input = analyze(["hi #weekend",
                          "good morning #zurich #limmat",
                          "spend my #weekend in #zurich",
                          "#zurich <3"])
        actual = analyze(input)
        expected = analyze2(input)
        self.assertEqual(expected, actual)
