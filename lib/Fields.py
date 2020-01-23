from abc import ABC
from lib.enums import DataType


class Field(ABC):
    def __init__(self, name, width, start_at):
        self.name = name
        self.width = width
        self.start_at = start_at

    @classmethod
    def create(self, name, width, start_at, data_type):

        try:
            _name = str(name)
        except ValueError:
            raise ValueError("Couldn't convert column name to str")

        try:
            _width = int(width)
        except ValueError:
            raise ValueError("Couldn't convert width to integer")

        try:
            _data_type = DataType(data_type)
        except ValueError:
            raise ValueError(
                "{} is not a valid data type".format(data_type))

        return self._mapField(_name, _width, start_at, _data_type)

    @staticmethod
    def _mapField(name, width, start_at, data_type):

        if(data_type == DataType.BOOLEAN):
            return BooleanField(name, width, start_at)
        elif(data_type == DataType.INTEGER):
            return IntegerField(name, width, start_at)
        elif(data_type == DataType.TEXT):
            return StringField(name, width, start_at)

    def _get(self, data):
        start_idx = self.start_at
        end_idx = self.start_at+self.width
        data = data[start_idx:end_idx]
        return data

    def validate(self):
        data = self._get(data)
        pass

    def parse(self, data):
        pass

    def __str__(self):
        return '{}: name: {}, width: {}, start_at: {}'.format(self.__class__.__name__, self.name, self.width, self.start_at)


class BooleanField(Field):
    def validate(self, data):
        super().validate(data)
        if(data not in [1, 0, "1", "0"]):
            raise ValueError("")

    def parse(self, data):
        return bool(int(self._get(data)))


class IntegerField(Field):
    def validate(self, data):
        super().validate(data)
        if(not data.isnumeric()):
            raise ValueError("")

    def parse(self, data):
        return int(self._get(data))


class StringField(Field):

    def validate(self, data):
        super().validate(data)

    def parse(self, data):
        return self._get(data).strip()
