from lib.Parser import Parser


def parse_flatfile(datafilename, formatfilename):
    parser = Parser(formatfilename)
    parser.loadData(datafilename)
    print(parser.asObject())


parse_flatfile("data/testformat1_2015-06-28.txt", "specs/testformat1.csv")
