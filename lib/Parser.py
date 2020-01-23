import csv
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
            except ValueError as e:
                raise ValueError(
                    "The field defination on line {} is not correct".format(field_data_idx+2))

            try:
                field = Field.create(name, width, start_at, data_type)
            except Exception as e:
                raise Exception(
                    "There is problem with the spec string on line {}".format(field_data_idx+2))

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
