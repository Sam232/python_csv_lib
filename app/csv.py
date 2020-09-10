import csv


class CsvTutorials:
    file_name = "/home/dev_fiatse/Projects/using_csv_tutorials/PASL_10_08_2020.csv"

    @staticmethod
    def read_csv():
        # with open(CsvTutorials.file_name) as csv_file:
        #     csv_reader = csv.reader(csv_file, delimiter=",")  # The reader method returns a list during a loop
        #     line_count = 0
        #
        #     print("File reading started")
        #     for row in csv_reader:
        #         line_count += 1
        #         print("Row {}: {}".format(line_count, "++++".join(row).strip()))
        #
        #     print("total number of rows is {}".format(line_count))
        #     print("File reading ended")

        with open(CsvTutorials.file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",", escapechar="\"")  # The DictReader will return a dictionary during a loop
            line_count = 0

            print("File reading started")
            for row in csv_reader:
                line_count += 1
                print("Row {}: {}+++{}+++{}".format(line_count, row[0], row[1], row[2]))

            print("total number of rows is {}".format(line_count))
            print("File reading ended")
