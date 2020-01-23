from lib.helpers import FileHelper
import tempfile
import unittest
import textwrap


def mockFileName(str):
    temp = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
    temp.writelines(textwrap.dedent(str))
    temp.close()
    return temp.name


class TestFileHelper(unittest.TestCase):
    def test_readFormatFile_valid(self):

        mock = mockFileName("""\
                "column name",width,datatype
                name,10,TEXT
                valid,1,BOOLEAN
                count,3,INTEGER
                """)

        func = FileHelper.readFormatFile(mock)
        expect = [['column name', 'width', 'datatype'], ['name', '10', 'TEXT'], [
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
