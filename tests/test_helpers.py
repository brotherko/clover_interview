from lib.helpers import FileHelper
from tests.util import mockFileName
import unittest


class TestFileHelper(unittest.TestCase):
    def test_readFormatFile_valid(self):

        mock = mockFileName("""\
                "column name",width,datatype
                name,10,TEXT
                valid,1,BOOLEAN
                count,3,INTEGER
                """)

        func = FileHelper.readFormatFile(mock)
        expect = [['name', '10', 'TEXT'], [
            'valid', '1', 'BOOLEAN'], ['count', '3', 'INTEGER']]
        self.assertEqual(func, expect, "Couldn't read csv file")

    def test_readDataFile_valid(self):

        mock = mockFileName("""\
                Foonyor   1  1
                Barzane   0-12
                Quuxitude 1103
                """)

        func = FileHelper.readDataFile(mock)
        expect = ['Foonyor   1  1', 'Barzane   0-12', 'Quuxitude 1103']
        self.assertEqual(func, expect, "Couldn't read text file")

        mock = mockFileName("""\
                Foonaaayorsdffs
                Barzanea123asda
                Quuxituebb21103
                """)

        func = FileHelper.readDataFile(mock)
        expect = ['Foonaaayorsdffs', 'Barzanea123asda', 'Quuxituebb21103']
        self.assertEqual(func, expect, "Couldn't read text file")

    def test_readDataFile_huge(self):
        mock = mockFileName("")
        func = FileHelper.readDataFile(mock)
        expect = []
        self.assertEqual(func, expect, "Couldn't read text file")
