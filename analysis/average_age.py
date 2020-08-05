from db_creator import database as db


class AvgAgeCalc:
    def __init__(self, param):
        self.param = param


    def calculate(self):

        if self.param == "male":
            result = self._execute_sql()
            return "Average age of male: " + str(result[0])

        elif self.param == "female":
            result = self._execute_sql()
            return "Average age of female: " + str(result[0])

        elif self.param == "overall":
            result = self._execute_sql_overall()
            return "Overall average age: " + str(result[0])

        else:
            return "Incorrect parameter"


    def _execute_sql(self):
        cursor = db.execute_sql("SELECT AVG(dob_age) "
                                "FROM Users "
                                "WHERE gender='%s'" % self.param)

        return cursor.fetchone()

    @staticmethod
    def _execute_sql_overall():
        cursor = db.execute_sql("SELECT AVG(dob_age) "
                                "FROM Users ")

        return cursor.fetchone()
