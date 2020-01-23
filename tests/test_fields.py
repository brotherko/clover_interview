from lib.fields import *
import unittest


class TestFields_valid(unittest.TestCase):
    def setUp(self):
        self.data = "abc012345"

    def test_TextField(self):
        field = TextField("test", 3, 0)
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
        expect = ValueError
        self.assertRaises(expect, self.field.parse, data)

    def test_spaces(self):
        data = "     "
        expect = ValueError
        self.assertRaises(expect, self.field.parse, data)

    def test_2minus(self):
        data = "--"
        expect = ValueError
        self.assertRaises(expect, self.field.parse, data)

    def test_decimal(self):
        data = "0.333"
        expect = ValueError
        self.assertRaises(expect, self.field.parse, data)


class TestTextField(unittest.TestCase):

    def setUp(self):
        self.field = TextField("test", 5, 0)

    def test_valid_string(self):
        data = "abc12"
        expect = "abc12"
        self.assertEqual(self.field.parse(data), expect)

    def test_non_alnum(self):
        data = "r�s-*"
        expect = ValueError
        self.assertRaises(expect, self.field.parse, data)

    def test_mix_empty_alnum(self):
        data = "ab 12"
        expect = "ab 12"
        self.assertEqual(self.field.parse(data), expect)

    def test_empty(self):
        data = ""
        expect = ""
        self.assertEqual(self.field.parse(data), expect)

    def test_many_empty(self):
        data = "    "
        expect = ""
        self.assertEqual(self.field.parse(data), expect)

    def test_mix_non_alnum(self):
        data = "r�sab"
        expect = ValueError
        self.assertRaises(expect, self.field.parse, data)


class TestBooleanField(unittest.TestCase):
    def setUp(self):
        self.field = BooleanField("test", 1, 0)

    def test_true(self):
        data = "1"
        expect = True
        self.assertEqual(self.field.parse(data), expect)

    def test_false(self):
        data = "0"
        expect = False
        self.assertEqual(self.field.parse(data), expect)

    def test_non_10(self):
        data = "a"
        expect = ValueError
        self.assertRaises(expect, self.field.parse, data)

    def test_space(self):
        data = " "
        expect = ValueError
        self.assertRaises(expect, self.field.parse, data)
