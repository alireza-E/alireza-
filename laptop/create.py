from term4.person.connect import Connect

class Create():
    def __init__(self, name, family, age, phone):
        self.name = name
        self.family = family
        self.age = age
        self.phone = phone
    def create_data(self):
        try:
            conn, cursor = Connect().do_connect()
            query = "INSERT INTO user(name, family, age, phone) VALUES(%s,%s,%s,%s)"
            data =(self.name,self.family,self.age,self.phone)
            cursor.execute(query, data)
            conn.commit()
            print("Sent data to your database.")

        except:
            print("sending error!")

name = input("name:")
family = input("family:")        