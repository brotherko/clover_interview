import csv
import sys
from lib.fields import Field
from lib.helpers import FileHelper
from lib.enums import DataType


class Parser:
    def __init__(self, path_to_file):
        self.data = []
        self.fields = []
        self.loadFormat(path_to_file)
        self.debug()

    def loadFormat(self, path_to_file):
        contents = FileHelper.readFormatFile(path_to_file)
        # remove first row
        contents = contents[1::]

        start_at = 0
        for field_data_idx, field_data in enumerate(contents):
            try:
                name, width, data_type = field_data
                field = Field.create(name, width, start_at, data_type)
            except ValueError as e:
                sys.exit("The format defination file on line {} is not correct: {}".format(
                    field_data_idx+2, e))
            except Exception as e:
                sys.exit("Unexpected Error in format defination on line {}: {}".format(
                    field_data_idx+2, e))

            start_at += field.width
            self.fields.append(field)

    def loadData(self, path_to_file):
        contents = FileHelper.readDataFile(path_to_file)
        for row in contents:
            rowMap = {}
            for field_idx, field in enumerate(self.fields):
                rowMap[field.name] = field.parse(row)
            self.data.append(rowMap)

    def asObject(self):
        return self.data

    def debug(self):
        for field in self.fields:
            print(field)
