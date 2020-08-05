from db_creator import Users
from db_creator import database as db
from analysis.pass_rating import PassRating
from analysis.average_age import AvgAgeCalc


def percent_of_gender():
    female = Users.select().where(Users.gender == "female").count()
    male = Users.select().where(Users.gender == "male").count()

    both = female + male
    male_percent = male / both * 100
    female_percent = female / both * 100

    print("Male: {}%, female:{}%".format(male_percent, female_percent))


def average_age(parameter):
    average = AvgAgeCalc(parameter)
    result = average.calculate()
    print(result)


def most_common_cities(number_of_results):
    result = execute_sql_common("location_city", number_of_results)
    print_most_common(number_of_results, result, "cities")


def most_common_password(number_of_results):
    result = execute_sql_common("login_password", number_of_results)
    print_most_common(number_of_results, result, "passwords")


def most_secure_password():
    passwords = PassRating()
    passwords.rate_passwords()
    best_password = passwords.get_best_password()

    print("Best password in database: " + best_password + "\n")


def born_between(date1, date2):
    date1 = date1 + 'T00:00:00.000Z'
    date2 = date2 + 'T23:59:59.999Z'

    chosen = Users.select().where(Users.dob_date.between(date1, date2))

    for user in chosen:
        print(user.id, user.name_first, user.name_last)


def execute_sql_common(column, n):
    cursor = db.execute_sql("SELECT " + column +
                            " FROM Users "
                            "GROUP BY " + column +
                            " ORDER BY COUNT(" + column + ") DESC "
                                                          "LIMIT " + str(n))

    return cursor.fetchall()


def print_most_common(number_of_results, tuples, what_is_it):

    print(str(number_of_results) + " most common " + what_is_it + " :")

    for results in tuples:
        for single_result in results:
            print(single_result)

    print("\n")