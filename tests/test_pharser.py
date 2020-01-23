import unittest
from tests.util import mockFileName
from lib.parser import Parser


def output_pharser_result(format_file_input, data_file_input):
    format_file = mockFileName(format_file_input)
    data_file = mockFileName(data_file_input)

    parser = Parser(format_file)
    parser.loadData(data_file)

    return parser.asObject()


class TestPharser(unittest.TestCase):
    def setUp(self):
        pass

    def test_normal(self):
        format_file_input = """\
            "column name",width,datatype
            test1,2,TEXT
            test2,1,TEXT
            test3,3,INTEGER
            test4,1,BOOLEAN
            test5,3,INTEGER
        """

        data_file_input = """\
            abc1230444
            abc1230444
            abc1230444
        """
        pharer_result = output_pharser_result(
            format_file_input, data_file_input)
        expect = [{'test1': 'ab', 'test2': 'c', 'test3': 123, 'test4': False, 'test5': 444}, {'test1': 'ab', 'test2': 'c',
                                                                                              'test3': 123, 'test4': False, 'test5': 444}, {'test1': 'ab', 'test2': 'c', 'test3': 123, 'test4': False, 'test5': 444}]
        self.assertEqual(pharer_result, expect)

    def test_data_no_header(self):
        format_file_input = """\
            test1,2,TEXT
            test2,1,TEXT
            test3,3,INTEGER
            test4,1,BOOLEAN
            test5,3,INTEGER
        """

        data_file_input = """\
            abc1230444
            abc1230444
            abc1230444
        """
        expect = ValueError
        self.assertRaises(expect, output_pharser_result,
                          format_file_input, data_file_input)

    def test_format_has_blank_line(self):
        format_file_input = """\
            test1,2,TEXT
            test2,1,TEXT
            test3,3,INTEGER

            test4,1,BOOLEAN
            test5,3,INTEGER
        """

        data_file_input = """\
            abc1230444
            abc1230444
            abc1230444
        """
        expect = ValueError
        self.assertRaises(expect, output_pharser_result,
                          format_file_input, data_file_input)

    def test_data_has_blank_line(self):
        format_file_input = """\
            test1,2,TEXT
            test2,1,TEXT
            test3,3,INTEGER
            test4,1,BOOLEAN
            test5,3,INTEGER
        """

        data_file_input = """\
            abc1230444

            abc1230444
            abc1230444
        """
        expect = ValueError
        self.assertRaises(expect, output_pharser_result,
                          format_file_input, data_file_input)

    def test_data_overflow(self):
        format_file_input = """\
            test1,2,TEXT
            test2,2,TEXT
        """

        data_file_input = """\
            ab123
            ab12
        """
        expect = ValueError
        self.assertRaises(expect, output_pharser_result,
                          format_file_input, data_file_input)

    def test_data_underflow(self):
        format_file_input = """\
            test1,2,TEXT
            test2,2,TEXT
        """

        data_file_input = """\
            a23
            ab12
        """
        expect = ValueError
        self.assertRaises(expect, output_pharser_result,
                          format_file_input, data_file_input)
