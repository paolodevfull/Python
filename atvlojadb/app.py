import os

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

banco_loja = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    banco_loja, "loja.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# --- MODEL (tabela no banco) ---
class Produto(db.Model):
    __tablename__ = "produto"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(60), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    estoque = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Produto {self.id} {self.nome_produto}>"


with app.app_context():
    db.create_all()

def _ler_formulario():
    """Lê campos do POST — nomes devem bater com o HTML (name=)."""
    return {
        "nome": request.form.get("nome", "").strip(),
        "categoria": request.form.get("categoria", "").strip(),
        "preco": request.form.get("preco", "").strip(),
        "estoque": request.form.get("estoque", "").strip(),
    }


def _validar(dados):
    if not dados["nome"] or not dados["categoria"] or not dados["preco"]:
        return "Preencha nome, categoria e preço."
    try:
        preco = float(dados["preco"].replace(",", "."))
        estoque = int(dados["estoque"] or 0)
    except ValueError:
        return "Preço ou estoque inválido."
    if preco < 0 or estoque < 0:
        return "Preço e estoque não podem ser negativos."
    return None


# --- READ ---
@app.route("/")
def index():
    # BUSCA NO BANCO: ordena os produtos pelo atributo nome
    produtos = Produto.query.order_by(Produto.nome).all()
    return render_template("lista.html", produtos=produtos)


# --- CREATE ---
@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        dados = _ler_formulario()
        erro = _validar(dados)
        if erro:
            return render_template(
                "formulario.html",
                titulo="Cadastrar produto",
                erro=erro,
                **dados,
            )
        produto = Produto(
            nome=dados["nome"],
            categoria=dados["categoria"],
            preco=float(dados["preco"].replace(",", ".")),
            estoque=int(dados["estoque"] or 0),
        )
        db.session.add(produto)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("formulario.html", titulo="Cadastrar produto")


# --- UPDATE ---
@app.route("/editar/<int:produto_id>", methods=["GET", "POST"])
def editar(produto_id):
    # CORRIGIDO: busca o produto pelo ID diretamente no banco
    produto = db.session.get(Produto, produto_id)

    # Se o produto não existir, volta para a lista
    if not produto:
        return redirect(url_for("index"))

    if request.method == "POST":
        dados = _ler_formulario()
        erro = _validar(dados)
        if erro:
            return render_template(
                "formulario.html",
                titulo="Editar produto",
                erro=erro,
                produto_id=produto.id,
                **dados,
            )
        # Atualiza os campos do objeto com os novos dados do formulário
        produto.nome = dados["nome"]
        produto.categoria = dados["categoria"]
        produto.preco = float(dados["preco"].replace(",", "."))
        produto.estoque = int(dados["estoque"] or 0)
        
        # CORRIGIDO: salva as alterações no banco de dados
        db.session.commit()
        return redirect(url_for("index"))

    # CORRIGIDO: quando for GET, envia os dados atuais do produto para o formulário
    return render_template(
        "formulario.html",
        titulo="Editar produto",
        nome=produto.nome,
        categoria=produto.categoria,
        preco=produto.preco,
        estoque=produto.estoque,
        produto_id=produto.id,
    )


# --- DELETE ---
@app.route("/excluir/<int:produto_id>", methods=["POST"])
def excluir(produto_id):
    # CORRIGIDO: busca o produto pelo ID
    produto = db.session.get(Produto, produto_id)
    
    # CORRIGIDO: se ele existir, deleta e faz o commit
    if produto:
        db.session.delete(produto)
        db.session.commit()
        
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)