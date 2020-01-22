import sys
import csv


class FileHelper:
    @classmethod
    def readFormatFile(self, path_to_file):
        try:
            with open(path_to_file) as fp:
                rows = csv.reader(fp)
                return list(rows)
        except OSError:
            print "Couldn't read this file"
        except:
            print "Unexpected error:", sys.exc_info()[0]

    @classmethod
    def readDataFile(self, path_to_file):
        try:
            with open(path_to_file) as fp:
                return [line.rstrip('\n') for line in fp]
        except OSError:
            print "Couldn't read this file"
        except:
            print "Unexpected error:", sys.exc_info()[0]
