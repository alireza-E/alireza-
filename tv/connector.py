from pymysql import connect



class Connect():
    def do_connect(self):
        try:
            conn = connect('localhost',
                           'poulstar',
                           'poulstar',
                           'Person')
            cursor = conn.cursor()
            print("connected")

        except:
            print("acces denied")

        return conn, cursor



Connect().do_connect()
