from lib.parser import Parser
from lib.fields import *
import unittest


class TestParser(unittest.TestCase):
    def test_getSchema(self):
        schema_input = [
            ["test1", "2", "TEXT"],
            ["test2", "1", "BOOLEAN"],
            ["test3", "3", "INTEGER"],
        ]

        fields = Parser._getSchema(schema_input)
        expect = [TextField("test1", 2, 0), BooleanField(
            "test2", 1, 2), IntegerField("test3", 3, 3)]
        self.assertListEqual(fields, expect)
