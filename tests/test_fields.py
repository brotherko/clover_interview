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
