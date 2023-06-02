class ClienteDAO():
    def __init__(self, con):
        self.con = con

    # CRUD - Create, Retrieve, Update, Delete
    def inserir(self, cliente):
        try:
            sql = "INSERT INTO Cliente(email, ultimo_nome, primeiro_nome, " \
                  "senha, cidade, bairro, rua, numero) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

            cursor = self.con.cursor()
            cursor.execute(sql, (cliente.email, cliente.ultimo_nome,
                                 cliente.primeiro_nome, cliente.senha,
                                 cliente.cidade, cliente.bairro,
                                 cliente.rua, cliente.numero))
            self.con.commit()
            id = cursor.lastrowid
            return id
        except:
            return 0


    def autenticar(self, email, senha):
        try:
            sql = "SELECT * FROM Cliente WHERE email=%s AND senha=%s"

            cursor = self.con.cursor()
            cursor.execute(sql, (email, senha))

            cliente = cursor.fetchone() # lastrowid, fetchone, fetchall
            return cliente
        except:
            return None

    def listar(self, codigo=None):
        try:
            cursor = self.con.cursor()
            if codigo != None:
                # pegar somente um cliente
                sql = "SELECT * FROM Cliente WHERE codigo=%s"
                cursor.execute(sql, (codigo,))
                cliente = cursor.fetchone()
                return cliente
            else:
                # pegar todos os clientes
                sql = "SELECT * FROM Cliente"
                cursor.execute(sql)
                clientes = cursor.fetchall()
                return clientes
        except:
            return None

    def atualizar(self, cliente):
        try:
            sql = "UPDATE Cliente " \
                  "SET email=%s, ultimo_nome=%s, primeiro_nome=%s, " \
                  "senha=%s, cidade=%s, bairro=%s" \
                  "rua=%s, numero=%s WHERE id=%s"

            cursor = self.con.cursor()
            cursor.execute(sql, (cliente.email, cliente.ultimo_nome,
                                 cliente.primeiro_nome,cliente.senha,
                                 cliente.cidade,cliente.bairro,
                                 cliente.rua, cliente.numero, cliente.id))
            self.con.commit()
            return cursor.rowcount
        except:
            return 0