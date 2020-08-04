from database.database import Users
from database.database import database as db
from pass_rating import PassRating


def percent_of_gender():
    female = Users.select().where(Users.gender == "female").count()
    male = Users.select().where(Users.gender == "male").count()

    both = female + male
    male_percent = male / both * 100
    female_percent = female / both * 100

    print("Male: {}%, female:{}%".format(male_percent, female_percent))


def average_age(parameter):
    if parameter == "male":
        cursor = db.execute_sql("SELECT AVG(dob_age) "
                                "FROM Users "
                                "WHERE gender='male'")

        male_age_avg = cursor.fetchone()
        print("Male age average: " + str(male_age_avg[0]))

    elif parameter == "female":
        cursor = db.execute_sql("SELECT AVG(dob_age) "
                                "FROM Users "
                                "WHERE gender='female'")
        female_age_avg = cursor.fetchone()
        print("Female age average: " + str(female_age_avg[0]))

    elif parameter == "overall":
        cursor = db.execute_sql("SELECT AVG(dob_age) "
                                "FROM Users;")
        overall_avg = cursor.fetchone()
        print("Overall average: " + str(overall_avg[0]))


def most_common_cities(n):
    cursor = db.execute_sql("SELECT location_city "
                            "FROM Users "
                            "GROUP BY location_city "
                            "ORDER BY COUNT(location_city) DESC "
                            "LIMIT " + str(n))

    result = cursor.fetchall()
    for cities in result:
        for city in cities:
            print(city)


def most_common_password(n):
    cursor = db.execute_sql("SELECT login_password "
                            "FROM Users "
                            "GROUP BY login_password "
                            "ORDER BY COUNT(location_city) DESC "
                            "LIMIT " + str(n))

    result = cursor.fetchall()
    for passwords in result:
        for password in passwords:
            print(password)


def most_secure_password():
    best_score = -1

    query = Users.select(Users.login_password)

    for row in query:
        password = row.login_password

        rate = PassRating(password)
        new_score = rate.count_points()

        if new_score > best_score:
            best_score = new_score
            best_pass = password

    print("Best password in database: " + best_pass)


def born_between(date1, date2):
    date1 = date1 + 'T00:00:00.000Z'
    date2 = date2 + 'T23:59:59.999Z'

    chosen = Users.select().where(Users.dob_date.between(date1, date2))

    for user in chosen:
        print(user.id, user.name_first, user.name_last)


if __name__ == "__main__":
    most_secure_password()
