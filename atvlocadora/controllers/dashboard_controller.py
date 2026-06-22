from flask import Blueprint, render_template
from models import ClienteLocadora, Locacao

# Blueprint da home — sem url_prefix, então "/" é a raiz do site
dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def index():
    return render_template(
        "index.html",
        total_clientes=ClienteLocadora.query.count(),
        total_pedidos=Locacao.query.count(),
        pedidos_recentes=Locacao.listar_com_detalhes()[:5],
    )