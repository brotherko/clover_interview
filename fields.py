from abc import ABC
from enums import DataType


class Field(ABC):
    def __init__(self, name, width, start_at):
        self.name = str(name)
        self.width = int(width)
        self.start_at = int(start_at)

    @classmethod
    def create(self, name, width, start_at, data_type):
        try:
            width = int(width)
        except ValueError as e:
            raise ValueError("Couldn't convert width to integer") from e

        try:
            data_type = DataType(data_type)
        except ValueError as e:
            raise ValueError(
                "{} is not a valid data type".format(data_type)) from e

        if(data_type == DataType.BOOLEAN):
            return BooleanField(name, width, start_at)
        elif(data_type == DataType.INTEGER):
            return IntegerField(name, width, start_at)
        elif(data_type == DataType.TEXT):
            return StringField(name, width, start_at)

    def get(self, data):
        start_idx = self.start_at
        end_idx = self.start_at+self.width
        data = data[start_idx:end_idx]
        return data

    def validate(self):
        data = self.get(data)
        pass

    def parse(self, data):
        pass

    def __str__(self):
        return '{}: name: {}, width: {}, start_at: {}'.format(self.__class__.__name__, self.name, self.width, self.start_at)


class BooleanField(Field):
    def validate(self, data):
        super().validate(data)
        print(data)
        if(data not in [1, 0]):
            raise ValueError("")

    def parse(self, data):
        return bool(self.get(data))


class IntegerField(Field):
    def validate(self, data):
        super().validate(data)
        if(not data.isnumeric()):
            raise ValueError("")

    def parse(self, data):
        return int(self.get(data))


class StringField(Field):

    def validate(self, data):
        super().validate(data)

    def parse(self, data):
        return self.get(data).strip()
