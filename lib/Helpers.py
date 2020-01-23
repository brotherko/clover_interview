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
        return contents

    @classmethod
    def readDataFile(self, path_to_file):
        return self._readFile(path_to_file, lambda fp: list(line.rstrip('\n') for line in fp))
