from flask import Blueprint, redirect, render_template, request, url_for

# Import SEM ponto — controller fica fora de models/
from models import ClienteLocadora, Locacao, Veiculo, db

# Blueprint "locadora" — grupo de rotas; url_prefix faz tudo começar com /locadora/
locadora_bp = Blueprint("locadora", __name__, url_prefix="/locadora")


# @route = decorator: esta URL chama a função logo abaixo
@locadora_bp.route("/")
def index():
    # TODO ALUNO: passe locacoes para o template
    locacoes = Locacao.listar_com_detalhes()
    return render_template("locadora/lista.html", locacoes=[locacoes])


@locadora_bp.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    clientes = ClienteLocadora.listar()
    veiculos = Veiculo.listar()

    if request.method == "POST":

        loc = Locacao(
            cliente_id = request.form.get(["cliente_id"]),
            veiculo_id = request.form.get(["veiculo_id"]),
            data_inicio = request.form.get(["data_inicio"]),
            data_fim = request.form.get(["data_fim"]),
            valor_total = request.form.get(["valor_total"]))
        # TODO ALUNO: ler form, criar Locacao, add, commit, redirect index
        pass

    return render_template(
        "locadora/formulario.html",
        clientes=clientes,
        veiculos=veiculos,
    )
