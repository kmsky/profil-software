import argparse
import db_analysis


class Args:
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
            db_analysis.percent_of_gender()

        if self.args.avg is not None:
            db_analysis.average_age(self.args.avg)

        if self.args.city is not None:
            db_analysis.most_common_cities(self.args.city)

        if self.args.password is not None:
            db_analysis.most_common_password(self.args.password)

        if self.args.secure is not False:
            db_analysis.most_secure_password()

        if self.args.dates is not None:
            db_analysis.born_between(self.args.dates[0], self.args.dates[1])
