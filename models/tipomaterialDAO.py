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