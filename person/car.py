from pymysql import connect

class Connect():
    def my_db(self):


        try:
            conn= connect(
                "localhost",
                "poulstar",
                "poulstar",
                "person",
            )
            cursor=conn.cursor()
            print("connected:(")

        except:
            print("Error")


        return conn,cursor

