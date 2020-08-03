import db_service
import rating
from datetime import datetime
import day_counter

users = db_service.Users
db = db_service.database


def percent_fm():
    female = users.select().where(users.gender == "female").count()
    male = users.select().where(users.gender == "male").count()

    both_sexes = female + male
    male_percent = male / both_sexes * 100
    female_percent = female / both_sexes * 100

    print("Sum: {}, male: {}%, female:{}%".format(both_sexes, male_percent, female_percent))


def average_age(parameter):
    if parameter == "male":
        cursor = db.execute_sql("SELECT AVG(dob_age) FROM users WHERE gender='male'")
        male_age_avg = cursor.fetchone()
        print("Male age average: " + str(male_age_avg[0]))

    elif parameter == "female":
        cursor = db.execute_sql("SELECT AVG(dob_age) FROM users WHERE gender='female'")
        female_age_avg = cursor.fetchone()
        print("Female age average: " + str(female_age_avg[0]))

    elif parameter == "overall":
        cursor = db.execute_sql("SELECT AVG(dob_age) FROM users;")
        overall_avg = cursor.fetchone()
        print("Overall average: " + str(overall_avg[0]))


def most_common_cities(n):
    cursor = db.execute_sql("SELECT location_city "
                            "FROM users "
                            "GROUP BY location_city "
                            "ORDER BY COUNT(location_city) DESC "
                            "LIMIT " + str(n))

    cities = cursor.fetchall()
    for tuple in cities:
        for element in tuple:
            print(element)


def most_common_password(n):
    cursor = db.execute_sql("SELECT login_password "
                            "FROM users "
                            "GROUP BY login_password "
                            "ORDER BY COUNT(location_city) DESC "
                            "LIMIT " + str(n))

    passwords = cursor.fetchall()
    for tuple in passwords:
        for element in tuple:
            print(element)


def most_secure_password():
    best_pass = ''
    best_score = -1

    passwords = users.select(users.login_password)

    for p in passwords:
        text = p.login_password
        new_score = rating.count_points(text)
        if new_score > best_score:
            best_score = new_score
            best_pass = text

    print("Best password in database: " + best_pass)


def born_between(date1, date2):
    date1 = date1 + 'T00:00:00.000Z'
    date2 = date2 + 'T23:59:59.999Z'

    chosen = users.select().where(users.dob_date.between(date1, date2))

    for user in chosen:
        print(user.id, user.name_first, user.name_last)
