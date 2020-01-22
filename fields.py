from enum import Enum


class DataType(Enum):
    BOOLEAN = 'BOOLEAN'
    INTEGER = 'INTEGER'
    TEXT = 'TEXT'


class Field:
    def __init__(self, field_data):
        self.name, self.width, self.dataType, self.startAt = field_data

        self.width = int(self.width)
        self.dataType = DataType(self.dataType)

    def parse(self, data):
        data = data[self.startAt:self.startAt+self.width]
        if(self.dataType == DataType.BOOLEAN):
            return bool(data)
        elif(self.dataType == DataType.INTEGER):
            return int(data)
        elif(self.dataType == DataType.TEXT):
            return data.strip()
        else:
            pass

    def __str__(self):
        return 'name: {}, width: {}, dataType: {}, startAt: {}'.format(self.name, self.width, self.dataType, self.startAt)
