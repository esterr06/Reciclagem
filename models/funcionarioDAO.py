class FuncionarioDAO():
    def __init__(self, con):
        self.con = con

    # CRUD - Create, Retrieve, Update, Delete
    def inserir(self, funcionario):
        try:
            sql = "INSERT INTO Funcionario(primeiro_nome, ultimo_nome, data_de_nasc, " \
                  "email, senha, cidade, bairro, rua, numero) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

            cursor = self.con.cursor()
            cursor.execute(sql, (funcionario.primeiro_nome, funcionario.ultimo_nome,
                                 funcionario.data_de_nasc, funcionario.email,
                                 funcionario.senha, funcionario.cidade,
                                 funcionario.bairro, funcionario.rua, funcionario.numero))
            self.con.commit()
            id = cursor.lastrowid
            return id
        except:
            return 0


    def autenticar(self, email, senha):
        try:
            sql = "SELECT * FROM Funcionario WHERE email=%s AND senha=%s"

            cursor = self.con.cursor()
            cursor.execute(sql, (email, senha))

            funcionario = cursor.fetchone() # lastrowid, fetchone, fetchall
            return funcionario
        except:
            return None

    def listar(self, codigo=None):
        try:
            cursor = self.con.cursor()
            if codigo != None:
                # pegar somente uma planta
                sql = "SELECT * FROM Funcionario WHERE codigo=%s"
                cursor.execute(sql, (codigo,))
                funcionario = cursor.fetchone()
                return funcionario
            else:
                # pegar todas as plantas
                sql = "SELECT * FROM Funcionario"
                cursor.execute(sql)
                funcionario = cursor.fetchall()
                return funcionario
        except:
            return None