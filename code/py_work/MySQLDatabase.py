import mysql.connector
from mysql.connector import Error

class MySQLDatabase:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def execute_query(self, query, params=None):
        result = None
        try:
            with mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query, params)
                    if query.lower().strip().startswith("select"):
                        result = cursor.fetchall()  # Return fetched data for SELECT queries
                    else:
                        connection.commit()  # Commit changes for INSERT, UPDATE, DELETE
                        result = cursor.rowcount  # Return the number of affected rows
            return result
        except Error as e:
            print(f"Error: '{e}'")
            return None

# 使用该类的示例

# db_config = {
#     'host': 'localhost',
#     'user': 'yourusername',
#     'password': 'yourpassword',
#     'database': 'yourdatabase'
# }
#
# db = MySQLDatabase(**db_config)
#
# # SELECT 查询示例
# select_query = "SELECT * FROM yourtable"
# rows = db.execute_query(select_query)
# for row in rows:
#     print(row)
#
# # INSERT 查询示例
# insert_query = "INSERT INTO yourtable (column1, column2) VALUES (%s, %s)"
# affected_rows = db.execute_query(insert_query, params=("value1", "value2"))
# print(f"{affected_rows} rows inserted.")