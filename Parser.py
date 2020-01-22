import csv
from fields import Field
from helpers import FileHelper


class Parser:
    def __init__(self, path_to_file):
        self.data = []
        self.fields = []
        self.loadFormat(path_to_file)
        self.debug()

    @property
    def data(self):
        return self.asObject()

    def loadFormat(self, path_to_file):
        contents = FileHelper.readFormatFile(path_to_file)
        # remove first row
        contents = contents[1::]

        start_at = 0
        for field_data in contents:
            field = Field(field_data + [start_at])
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
