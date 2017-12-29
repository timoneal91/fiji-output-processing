import csv
from datetime import datetime
from functools import reduce
from os import path


class App:
    # number of decimal places for final output
    PRECISION = 3

    def __init__(self, source):

        if not source.endswith(".csv"):
            raise Exception("We can only process CSV output")

        if not path.isfile(source):
            raise Exception("Provided path is not a file")

        self.source = source
        self.data = []
        self.output = []

    def run(self):
        print(f"Loading data from: {self.source}")
        self.load_data()

        if len(self.data) <= 10:
            raise Exception("Can only process data lengths greater than 10")

        print("Data loaded, processing")
        self.process_data()

        print("Data processed, writing to disk")
        self.output_data()

        print("Writing complete!")

    def load_data(self):
        with open(self.source, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
                # skip a blank row or one that is just headers
                if len(row) == 0 or row[0].strip() == '':
                    continue

                row_data = []
                # skip the first col
                for col in row[1:]:
                    row_data.append(col)
                self.data.append(row_data)

    # noinspection PyBroadException
    def process_data(self):
        output = []

        # first pass, subtract last row from each preceding
        for row in self.data:
            row_data = []
            last_idx = len(row) - 1
            last_data = row[last_idx]
            for col in row[:-1]:
                try:
                    row_data.append(float(col) - float(last_data))
                except Exception:
                    continue

            output.append(row_data)

        output_second = []

        # second pass, skip first ten rows,
        for row_idx, row in enumerate(output):
            # skip the first 10 rows
            if row_idx < 10:
                continue

            row_data = []

            for col_idx, col in enumerate(row):
                col_val = float(col)

                print(col_val)

                preceding_col_values = []

                for r in output[row_idx - 10:row_idx]:
                    preceding_col_values.append(r[col_idx])

                preceding_col_values = sorted(preceding_col_values)

                bottom_values = preceding_col_values[:5]

                print(f'Preceding: {preceding_col_values}')

                bottom_mean = reduce(lambda x, y: x + y, bottom_values) / len(bottom_values)

                print(f'Bottom mean: {bottom_mean}')

                final_val = (col_val - bottom_mean) / bottom_mean

                print(f'Final: {final_val}')

                row_data.append(final_val)

            output_second.append(row_data)

        # all done
        self.output = output_second

    def output_data(self):
        d = path.dirname(self.source)
        f = path.basename(self.source)

        output_location = path.join(d, 'processed_{}_{}.csv'.format(datetime.now().strftime('%Y%m%d-%H%M%S'), f))

        with open(output_location, 'w') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for row in self.output:
                writer.writerow(row)

        print(f'Wrote output to: {output_location}')
