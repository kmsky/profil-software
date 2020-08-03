import argparse
import statistics


class Args():
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-percent-fm', action='store_true', dest='percent')
        parser.add_argument('-average-age', action='store', type=str, dest='avg')
        parser.add_argument('-most-common-city', action='store', type=int, dest='city')
        parser.add_argument('-most-common-password', action='store', type=int, dest='password')
        parser.add_argument('-most-secure-password', action='store_true', dest='secure')
        parser.add_argument('-born-between', action='store', type=str, dest='dates', nargs='+')

        self.args = parser.parse_args()

    def choose_function(self):
        if self.args.percent is not False:
            statistics.percent_fm()

        if self.args.avg is not None:
            statistics.average_age(self.args.avg)

        if self.args.city is not None:
            statistics.most_common_cities(self.args.city)

        if self.args.password is not None:
            statistics.most_common_password(self.args.password)

        if self.args.secure is not False:
            statistics.find_best_password()

        if self.args.dates is not None:
            statistics.born_between(self.args.dates[0], self.args.dates[1])


if __name__ == "__main__":
    args = Args()
    args.choose_function()
