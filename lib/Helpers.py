import sys
import csv
import os


class FileHelper:

    @classmethod
    def _readFile(self, path_to_file, func):
        try:
            with open(path_to_file) as fp:
                return func(fp)
        except FileNotFoundError as e:
            sys.exit("Couldn't find the given file: {}".format(e))
        except OSError as e:
            sys.exit("Couldn't read the given file: {}".format(e))
        except:
            sys.exit("Unexpected error: {}".format(sys.exc_info()[0]))

    @classmethod
    def readFormatFile(self, path_to_file):
        contents = self._readFile(
            path_to_file, lambda fp: list(csv.reader(fp)))
        if(contents[0] != ["column name", "width", "datatype"]):
            raise ValueError("First line of format file should be \"column name\",width,datatype, found: {}".format(
                contents[0]))
        # remove the first line
        return contents[1::]

    @classmethod
    def readDataFile(self, path_to_file):
        return self._readFile(path_to_file, lambda fp: list(line.rstrip('\n') for line in fp))
