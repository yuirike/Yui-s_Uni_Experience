#!/usr/bin/env python3

from unittest import TestCase
from script import ProfanityFilter


class PublicTestSuite(TestCase):

    def test_example(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi mastard jklmno"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? jklmno"
        self.assertEqual(expected, actual)

    def test_New_Curses(self):
        f = ProfanityFilter(["Slut", "Bitch","Whore","Shit","Cockless"], "---")
        msg = "I really hate you. You're such a Slut. I can't believe how much of a bitch you've become."
        actual = f.filter(msg)
        expected = "I really hate you. You're such a ----. I can't believe how much of a ----- you've become."
        self.assertEqual(expected, actual)

    def test_Capital_cases(self):
        f = ProfanityFilter(["BiTcH","Cock","Dick"], "?#$")
        msg = "She's quite a bitch, isn't she? cock No wonder her boyfriend cheated on her with his massive dick."
        actual = f.filter(msg)
        expected = "She's quite a ?#$?#, isn't she? ?#$? No wonder her boyfriend cheated on her with his massive ?#$?."
        self.assertEqual(expected, actual)

    def test_Capital_cases2(self):
        f = ProfanityFilter(["BiTcH","Cock","Dick"], "?#$")
        msg = "She's quite a bitchy BITCH, isn't she? No wonder her boyfriend cheated on her with his massive dick, nay, I mean cock!"
        actual = f.filter(msg)
        expected = "She's quite a ?#$?#y ?#$?#, isn't she? No wonder her boyfriend cheated on her with his massive ?#$?, nay, I mean ?#$?!"
        self.assertEqual(expected, actual)

    def test_Capital_cases3(self):
        f = ProfanityFilter(["Anus","Penis","Dick","Cock"], "@")
        msg = "KLSJLQJDIJOOJDOQJPOLJFDLOanuskjdijofjaoöfjjfcock"
        actual = f.filter(msg)
        expected = "KLSJLQJDIJOOJDOQJPOLJFDLO@@@@kjdijofjaoöfjjf@@@@"
        self.assertEqual(expected, actual)

    def test_Capital_cases3(self):
        f = ProfanityFilter(["Profit"], "*")
        msg = "Our profit was really profitable today, I feel profitably good."
        actual = f.filter(msg)
        expected = "Our ****** was really ******able today, I feel ******ably good."
        self.assertEqual(expected, actual)

    def test_Subword(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "*")
        msg = "I duckshot him in the face!"
        actual = f.filter(msg)
        expected = "I ******** him in the face!"
        self.assertEqual(expected, actual)


    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly ecncourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
