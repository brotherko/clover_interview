import sys
import re
from abc import ABC
from lib.enums import DataType


class Field(ABC):
    def __init__(self, name, width, start_at):
        self.name = name
        self.width = width
        self.start_at = start_at

    @classmethod
    def create(self, name, width, start_at, data_type):
        _name, _width, _start_at, _data_type = self._convertAndValidateParam(
            name, width, start_at, data_type)
        return self._mapField(_name, _width, _start_at, _data_type)

    @staticmethod
    def _convertAndValidateParam(name, width, start_at, data_type):

        try:
            _name = str(name)
        except ValueError:
            sys.exit("Couldn't convert the column name to str")

        try:
            _width = int(width)
        except ValueError:
            sys.exit("Couldn't convert the width value to int")

        try:
            _data_type = DataType(data_type)
        except ValueError:
            sys.exit("{} is not a valid data type".format(data_type))

        return [_name, _width, start_at, _data_type]

    @staticmethod
    def _mapField(name, width, start_at, data_type):

        if(data_type == DataType.BOOLEAN):
            return BooleanField(name, width, start_at)
        elif(data_type == DataType.INTEGER):
            return IntegerField(name, width, start_at)
        elif(data_type == DataType.TEXT):
            return TextField(name, width, start_at)

    def parse(self, raw):
        data = self._get(raw)
        self._validate(data)
        return self._parse(data)

    def _get(self, raw):
        start_idx = self.start_at
        end_idx = self.start_at+self.width
        data = raw[start_idx:end_idx]
        return data

    def _validate(self, data):
        pass

    def _parse(self, data):
        pass

    def __eq__(self, other):
        return (
            type(self) == type(other)
            and self.width == other.width
            and self.name == other.name
            and self.start_at == other.start_at
        )

    def __str__(self):
        return '{}: name: {}, width: {}, start_at: {}'.format(self.__class__.__name__, self.name, self.width, self.start_at)


class BooleanField(Field):
    def __init__(self, name, width, start_at):
        super().__init__(name, width, start_at)
        if(self.width != 1):
            raise ValueError(
                "The width of Boolean should be 1, found {}".format(width))

    def _validate(self, data):
        super()._validate(data)
        if(not re.match(r'[0,1]', data)):
            raise ValueError(
                "The {} field should be either 1 or 0, found {}".format(self.name, data))

    def _parse(self, data):
        return bool(int(data))


class IntegerField(Field):
    def _validate(self, data):
        super()._validate(data)
        if(not re.match(r'^\W*?-?[0-9]*\W*$', data)):
            raise ValueError(
                "The {} field should be numeric value, found {}".format(self.name, data))

    def _parse(self, data):
        return int(data)


class TextField(Field):
    def _validate(self, data):
        super()._validate(data)
        data = data.strip()
        if(not re.match(r'^[a-zA-Z0-9 ]*$', data)):
            raise ValueError(
                "The {} field should only contain alphabet, number and space, found {}".format(self.name, data))

    def _parse(self, data):
        return data.strip()
