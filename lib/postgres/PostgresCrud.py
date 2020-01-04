import psycopg2 as psql
from psycopg2.extras import RealDictCursor
from datetime import datetime
from .postgresConfig import *

# user_name = "postgres"
# db_password = "1234"
# db_host = "127.0.0.1"
# db_port = "5432"
# db_database = "shreyanshu"


class PostgresOperation:
    def __init__(self):
        self.connection = psql.connect(user=user_name,
                                       password=db_password,
                                       host=db_host,
                                       port=db_port,
                                       database=db_database)
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

    def loginModule(self, data):
        users_data = """select * from user_details WHERE user_id= '{}'""".format(
            data['user_id'])
        self.cursor.execute(users_data)
        users_db_data = self.cursor.fetchone()
        if users_db_data:
            if users_db_data['auth_value'] == data['auth_value']:
                return 1, data, users_db_data
            else:
                return False, "password error"
        else:
            return 2, "user not registered"

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
        pass

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
    # data_val = {
    #     "user_name": "shrey731e12",
    #     "auth_value": "abecd",
    #     "user_email": "avdvadefe@gmail.com",
    #     "user_phone": "64571269766",
    #     "phone_verified": False,
    #     "email_verified": False,
    #     "bank_verified": False,
    #     "latitude": None,
    #     "longitude": None,
    #     "user_device_id": "shreyanshu__one"
    # }
    # print(ob.signupModule(data_val))
# try:
    # connection = psql.connect(user="postgres",
    #                           password="1234",
    #                           host="127.0.0.1",
    #                           port="5432",
    #                           database="shreyanshu")

#     cursor = connection.cursor(cursor_factory=RealDictCursor)
#     user_id = "shreya42a1"
    # get_data_from_sql = """select auth_value from user_details WHERE user_id= '{}' """.format(
    #     user_id)

#     # Print PostgreSQL version
    # cursor.execute(get_data_from_sql)
    # record = cursor.fetchone()
#     print(record['auth_value'])

# except (Exception, psql.Error) as error:
#     print("Error while connecting to PostgreSQL", error)
# finally:
#     # closing database connection.
#     if(connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")
# .format(
#                 user_data["user_name"],
#                 user_data["auth_value"],
#                 user_data["user_email"],
#                 user_data["user_phone"],
#                 user_data["phone_verified"],
#                 user_data["email_verified"],
#                 user_data["bank_verified"],
#                 user_data["latitude"],
#                 user_data["longitude"],
#                 user_data["user_device_id"],
#                 datetime.now()
#             )
