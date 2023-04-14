from flask import Flask, g, render_template,\
    request, redirect, url_for, flash, session

import mysql.connector

from models.cliente import Cliente
from models.clienteDAO import ClienteDAO

from models.funcionario import Funcionario
from models.funcionarioDAO import FuncionarioDAO

from models.tipomaterial import Tipomaterial
from models.tipomaterialDAO import TipomaterialDAO

app = Flask(__name__)
app.secret_key = "senha123"

DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = ""
DB_NAME = "reciclagem"


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    return render_template("login.html")


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == "POST":
        # valor = request.form['campoHTML']
        email = request.form['email']
        ultimo_nome = request.form['ultimo_nome']
        primeiro_nome = request.form['primeiro_nome']
        senha = request.form['senha']
        cidade = request.form['cidade']
        bairro = request.form['bairro']
        rua = request.form['rua']
        numero = request.form['numero']

        cliente = Cliente(email, ultimo_nome, primeiro_nome, senha,
                          cidade, bairro, rua, numero)

        dao = ClienteDAO(get_db())
        codigo = dao.inserir(cliente)

        if codigo > 0:
            flash("Cadastrado com sucesso! Código %d" % codigo, "success")
        else:
            flash("Erro ao cadastrar!", "danger")

    vartitulo = "Cadastro"
    return render_template("register.html", titulo=vartitulo)

@app.route('/cadastrar_funcionario', methods=['GET', 'POST'])
def cadastrarfuncionario():
    if request.method == "POST":
        # valor = request.form['campoHTML']
        primeiro_nome = request.form['primeiro_nome']
        ultimo_nome = request.form['ultimo_nome']
        data_de_nasc = request.form['data_de_nasc']
        email = request.form['email']
        senha = request.form['senha']
        cidade = request.form['cidade']
        bairro = request.form['bairro']
        rua = request.form['rua']
        numero = request.form['numero']

        funcionario = Funcionario(primeiro_nome, ultimo_nome, data_de_nasc, email,
                          senha, cidade, bairro, rua, numero)

        dao = FuncionarioDAO(get_db())
        codigo = dao.inserir(funcionario)

        if codigo > 0:
            flash("Cadastrado com sucesso! Código %d" % codigo, "success")
        else:
            flash("Erro ao cadastrar!", "danger")

    vartitulo = "Cadastro"
    return render_template("register_funcionario.html", titulo=vartitulo)

@app.route('/cadastrar_tipo_material', methods=['GET', 'POST'])
def cadastrartipomaterial():
    if request.method == "POST":
        # valor = request.form['campoHTML']
        nome = request.form['nome']
        descricao = request.form['descricao']

        tipomaterial = Tipomaterial(nome, descricao)

        dao = TipomaterialDAO(get_db())
        codigo = dao.inserir(tipomaterial)

        if codigo > 0:
            flash("Cadastrado com sucesso! Código %d" % codigo, "success")
        else:
            flash("Erro ao cadastrar!", "danger")

    vartitulo = "Cadastro"
    return render_template("register_tipo_material.html", titulo=vartitulo)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        senha = request.form['senha']

        # Verificar dados
        dao = ClienteDAO(get_db())
        cliente = dao.autenticar(email, senha)

        if cliente is not None:
            session['logado'] = {
                'codigo': cliente[0],
                'primeiro_nome': cliente[3],
                'ultimo_nome': cliente[4],
                'email': cliente[1],
            }
            return redirect(url_for('/painel'))
        else:
            flash("Erro ao efetuar login!", "danger")

    return render_template("index.html", titulo="/painel")

@app.route('/listar_cliente', methods=['GET',])
def listar_cliente():
    dao = ClienteDAO(get_db())
    cliente_db = dao.listar()
    return render_template('listar_cliente.html', cliente=cliente_db)

@app.route('/logout')
def logout():
    session['logado'] = None
    session.clear()
    return redirect(url_for('index'))


@app.route('/index.html')
def painel():
    return render_template("index.html", titulo="/painel")


if __name__=='__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
