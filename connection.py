import pymysql

class callUsers:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='#Ignacio98',
            db='testdb'

        )
        self.cursor =  self.connection.cursor()

    def select_user(self, id):
        sql = 'SELECT * FROM cliente WHERE rutCliente = {}'.format(id)

        full_name = ""

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()

            full_name = user[2] + " " + user[3]

        except Exception as e:
            pass

        return full_name