import psycopg2 as psql
from psycopg2.extras import RealDictCursor
from datetime import datetime
from .postgresConfig import *


class PostgresOperation:
    def __init__(self):
        self.connection = psql.connect(user=user_name,
                                       password=db_password,
                                       host=db_host,
                                       port=db_port,
                                       database=db_database)
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

    def loginModule(self, data):
        users_data = """select * from user_details WHERE user_email= '{}'""".format(
            data['user_id'])
        self.cursor.execute(users_data)
        users_db_data = self.cursor.fetchone()
        if users_db_data:
            if users_db_data['auth_value'] == data['auth_value']:
                return 1, data, users_db_data
            else:
                return False, "password error", "error in password"
        else:
            return 2, "user not registered", "user_not registered"

    def signupModule(self, user_data):
        try:
            create_query = """ insert into user_details (user_name,user_id, auth_value, user_email,\
                user_phone, phone_verified, email_verified, bank_verified,
                latitude, longitude, user_device_id, created_at) values \
                (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            self.cursor.execute(create_query, (
                user_data["user_name"],
                user_data["user_id"],
                user_data["auth_value"],
                user_data["user_email"],
                user_data["user_phone"],
                user_data["phone_verified"],
                user_data["email_verified"],
                user_data["bank_verified"],
                user_data["latitude"],
                user_data["longitude"],
                user_data["user_device_id"],
                datetime.now()
            ))
            self.connection.commit()
            return True, "user Created"
        except Exception as e:
            print(e)
            return False, e

    def updateMobileStatus(self, user_id):
        try:
            query = """update user_details set phone_verified = %s where \
                user_id = %s"""
            self.cursor.execute(query, (True, user_id))
            self.connection.commit()
            return True, "Done"
        except Exception as e:
            return False, e

    def updateEmailStatus(self, user_id):
        try:
            query = """update user_details set email_verified = %s where \
                user_id = %s"""
            self.cursor.execute(query, (True, user_id))
            self.connection.commit()
            return True, "Done"
        except Exception as e:
            return False, e

    def updateBankStatus(self, user_id):
        try:
            query = """update user_details set bank_verified = %s where \
                user_id = %s"""
            self.cursor.execute(query, (True, user_id))
            self.connection.commit()
            return True, "Done"
        except Exception as e:
            return False, e

    def getAllUsers(self):
        query = """select * from user_details"""
        data = self.cursor.execute(query)
        record = self.cursor.fetchall()
        for i in record:
            print(i)

    def changeEmail(self, user_id, val):
        try:
            query = """update user_details set user_email = %s where \
                user_id = %s"""
            self.cursor.execute(query, (val, user_id))
            self.connection.commit()
            return True, "Done"
        except Exception as e:
            return False, e

    def changeMobile(self, user_id, val):
        try:
            query = """update user_details set user_phone = %s where \
                user_id = %s"""
            self.cursor.execute(query, (val, user_id))
            self.connection.commit()
            return True, "Done"
        except Exception as e:
            return False, e


if __name__ == "__main__":
    ob = PostgresOperation()
    # ob.getAllUsers()
    data = {
        'user_id': "abcdef",
        'auth_value': "abecd"
    }
    # print(ob.loginModule(data))
    print(ob.updateMobileStatus(data))
    print(ob.updateEmailStatus(data))
