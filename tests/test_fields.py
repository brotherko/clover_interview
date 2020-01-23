from lib.fields import *
import unittest


class TestFields_valid(unittest.TestCase):
    def setUp(self):
        self.data = "abc012345"

    def test_StringField(self):
        field = StringField("test", 3, 0)
        expect = "abc"
        self.assertEqual(field.parse(self.data), expect)

    def test_BooleanField(self):
        field = BooleanField("test", 1, 3)
        expect = False
        self.assertEqual(field.parse(self.data), expect)

    def test_IntegerField(self):
        field = IntegerField("test", 5, 4)
        expect = 12345
        self.assertEqual(field.parse(self.data), expect)


class TestIntegerField(unittest.TestCase):
    def setUp(self):
        self.field = IntegerField("test", 5, 0)

    def test_positive_integer(self):
        data = "11111"
        expect = 11111
        self.assertEqual(self.field.parse(data), expect)

    def test_positive_integer_with_plus(self):
        data = "+1111"
        expect = 1111
        self.assertEqual(self.field.parse(data), expect)

    def test_negative_integer(self):
        data = "-1323"
        expect = -1323
        self.assertEqual(self.field.parse(data), expect)

    def test_alpha(self):
        data = "abcde"
        expect = SystemExit
        self.assertRaises(expect, self.field.parse, data)

    def test_decimal(self):
        data = "0.333"
        expect = SystemExit
        self.assertRaises(expect, self.field.parse, data)
