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
            return StringField(name, width, start_at)

    def parse(self, raw):
        data = self._get(raw)
        try:
            self._validate(data)
        except ValueError as e:
            exit("These are problem with the data '{}': {}".format(raw, e))
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

    def __str__(self):
        return '{}: name: {}, width: {}, start_at: {}'.format(self.__class__.__name__, self.name, self.width, self.start_at)


class BooleanField(Field):
    def _validate(self, data):
        super()._validate(data)
        if(data not in [1, 0, "1", "0"]):
            raise ValueError(
                "Boolean field should be in the set of 1 and 0, found {}".format(data))

    def _parse(self, data):
        return bool(int(data))


class IntegerField(Field):
    def _validate(self, data):
        super()._validate(data)
        if(not re.match(r'^\W*?-?[0-9]*\W*$', data)):
            raise ValueError(
                "Integer Field should be numeric value, found {}".format(data))

    def _parse(self, data):
        return int(data)


class StringField(Field):
    def _validate(self, data):
        super()._validate(data)

    def _parse(self, data):
        return data.strip()
