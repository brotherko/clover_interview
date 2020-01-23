import csv
import sys
from lib.fields import Field
from lib.helpers import FileHelper
from lib.enums import DataType


class Parser:
    def __init__(self, path_to_file):
        self.loadFormat(path_to_file)
        self.debug()

    def loadFormat(self, path_to_file):
        format_contents = FileHelper.readFormatFile(path_to_file)
        self.fields = self._getFieldsFormat(format_contents)

    def _getFieldsFormat(self, format_contents):
        fields = []
        start_at = 0
        for field_data_idx, field_data in enumerate(format_contents):
            try:
                name, width, data_type = field_data
                field = Field.create(name, width, start_at, data_type)
            except ValueError as e:
                sys.exit("The format defination file on line {} is not correct: {}".format(
                    field_data_idx+2, e))
            except Exception as e:
                sys.exit("Unexpected Error in format defination on line {}: {}".format(
                    field_data_idx+2, e))

            fields.append(field)
            start_at += field.width
        return fields

    def loadData(self, path_to_file):
        data_contents = FileHelper.readDataFile(path_to_file)
        self.data = self._getData(data_contents)

    def _getData(self, data_contents):
        data = []
        for row in data_contents:
            rowMap = {}
            for field_idx, field in enumerate(self.fields):
                rowMap[field.name] = field.parse(row)
            data.append(rowMap)
        return data

    def asObject(self):
        return self.data

    def debug(self):
        for field in self.fields:
            print(field)
