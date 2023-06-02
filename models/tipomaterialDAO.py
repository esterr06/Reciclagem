class TipomaterialDAO():
    def __init__(self, con):
        self.con = con

    # CRUD - Create, Retrieve, Update, Delete
    def inserir(self, tipomaterial):
        try:
            sql = "INSERT INTO tipo_de_material(nome, descricao) " \
                  "VALUES (%s, %s)"

            cursor = self.con.cursor()
            cursor.execute(sql, (tipomaterial.nome, tipomaterial.descricao))
            self.con.commit()
            id = cursor.lastrowid
            return id
        except:
            return 0

    def listar(self, codigo=None):
        try:
            cursor = self.con.cursor()
            if codigo != None:
                sql = "select t.nome as tipo," \
                      "count(t.id) as qtde " \
                      "from Tipo_de_material as t " \
                      "group by t.nome WHERE codigo=%s"
                cursor.execute(sql, (codigo,))
                tmaterial = cursor.fetchone()
                return tmaterial
            else:
                sql = "select t.nome as tipo, " \
                      "count(t.id) as qtde " \
                      "from Tipo_de_material as t " \
                      "group by t.nome"
                cursor.execute(sql)
                tmaterial = cursor.fetchall()
                return tmaterial
        except:
            return None