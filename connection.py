import pymysql

class callUsers:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='ignacio98',
            db='shieldersystem'

        )
        self.cursor =  self.connection.cursor()

    def select_user(self, id):
        sql = 'SELECT * FROM cliente WHERE rut_cliente = {}'.format(id)

        full_name = ""

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()

            full_name = user[2] + " " + user[3]

        except Exception as e:
            full_name = "ERROR"
            pass

        return full_name

    def user_validation(self, usr, pss):
        sql = 'SELECT * FROM users WHERE name_users="{}" and pass_users="{}"'.format(usr, pss)

        validado = ""

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            validado = user[0]

        except Exception as e:
            pass
        return validado

    def id_user(self, id):
        sql = 'SELECT * FROM cliente WHERE rut_cliente = {}'.format(id)

        id_cliente = ""

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()

            id_cliente = user[0]
        except Exception as e:
            pass
        return id_cliente

    def insert_photo(self, archivo, clientt):

        sql = 'INSERT INTO photos (nom_photo, cliente_photo) VALUES ("{}", {})'.format(archivo, clientt)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            #print("PASS")
        except Exception as e:
            pass
        print("Guardado")
    
    def insert_cliente(self, rut, nombre, apellido, fono):
        sql = 'INSERT INTO cliente (rut_cliente, nom_cliente, ape_cliente, fono_cliente, admin_cliente) VALUES ("{}", "{}", "{}", {}, 1)'.format(rut, nombre, apellido, fono)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Cliente guardado")
        except Exception as e:
            pass

#datab = callUsers()

#print(datab.id_user("19853982"))