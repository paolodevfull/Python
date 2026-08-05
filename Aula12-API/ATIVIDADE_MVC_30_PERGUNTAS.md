# Atividade Aula 12 — Model, Controller e View (StreamFlix)

**Disciplina:** Python / Flask  
**Profª:** Janaína Duarte  
**Projeto:** `flask/Aula12/`  
**Objetivo:** Explorar o código, localizar arquivos e explicar o que cada camada faz.

---

## Como responder

1. Abra a pasta `flask/Aula12/` no editor ou GitHub.
2. Navegue pelas pastas `models/`, `controllers/` e `views/`.
3. Rode o site (`python app.py`) quando a pergunta pedir para testar no navegador.
4. Responda com **caminho do arquivo** + **explicação em suas palavras**.

**Identificação**

- Nome: PAOLO EDUARDO MONTEIRO LOPES DE ANDRADE
- Turma: 3C1

---

## Bloco A — Model (perguntas 1 a 10)

**1.** Em qual pasta ficam as classes que representam tabelas do banco SQLite? Cite o caminho.
aula12/models/

**2.** Qual é o nome do arquivo de banco criado quando o app roda? Em qual arquivo Python essa configuração está?
streamflix.db.   No arquivo app.py

**3.** Quais classes Model existem no projeto (nome das classes)? Em quais arquivos `.py` cada uma está?
Filme_favorito e historico_busca

**4.** De qual superclasse `FilmeFavorito` e `HistoricoBusca` herdam? O que elas ganham automaticamente por herança (cite 3 campos)?
Da classe base, id, data_criacao e data_atualizacao

**5.** Qual é o `__tablename__` da tabela de favoritos? Por que usamos `__tablename__` em vez de só o nome da classe?
filmes_favoritos, para direcionar que é um nome de tabela

**6.** No model `FilmeFavorito`, qual coluna guarda o id do filme vindo da API TMDB? Ela tem alguma restrição especial (`unique`, `nullable`)?
tmdb_id,(db.Integer, nullable=False, unique=True)

**7.** Abra `models/filme_favorito.py`. O que o método `@classmethod adicionar` faz passo a passo? O que acontece se o filme já existir nos favoritos?

**8.** Onde está o método que lista as últimas 8 buscas? Qual é o nome da classe e do método?

**9.** O model grava dados da API TMDB inteira ou só alguns campos espelhados? Cite 4 campos salvos em `FilmeFavorito`.

**10.** Em `models/__init__.py`, o que é exportado além de `db`? Por que o controller importa `from models import FilmeFavorito` em vez de importar o arquivo inteiro da pasta?

---

## Bloco B — Controller (perguntas 11 a 20)

**11.** Quantos Blueprints existem no projeto? Cite o **nome** de cada um e o **url_prefix** (se tiver).
dashboard_bp (sem url_prefix)

filmes_bp (url_prefix='/filmes')

favoritos_bp (url_prefix='/favoritos')
**12.** Em qual arquivo está a rota `/filmes/populares`? Qual é o nome da função Python que responde essa URL?
Arquivo: controllers/filmes_controller.py.

Função: populares().
**13.** O que a função `populares()` faz antes de chamar `render_template`? Cite duas chamadas (Model, Service ou API).
Chama a API do TMDB via TmdbApi().populares() para pegar os filmes e busca o histórico recente com HistoricoBusca.ultimas()
**14.** Quando o usuário busca um filme em `/filmes/buscar`, qual controller registra o termo no banco? Qual model é usado e em qual linha aproximada?
Controller: controllers/filmes_controller.py.

Model: HistoricoBusca (na linha 33, chamando HistoricoBusca.registrar(...)).
**15.** Abra `controllers/favoritos_controller.py`. Qual método HTTP é exigido para adicionar favorito (`GET` ou `POST`)? Qual a URL completa de exemplo para adicionar o filme id 550?
Método HTTP: POST.

URL completa de exemplo: /favoritos/adicionar/550.

**16.** No `filmes_controller.py`, rota `detalhe(filme_id)`: o que acontece se `api.detalhe(filme_id)` retornar `None`?
Redireciona o usuário para a lista de filmes populares com uma mensagem de erro em flash.
**17.** Onde os Blueprints são **registrados** no Flask? Cite o arquivo e o comando usado (3 registros).
No arquivo app.py, através dos comandos:app.register_blueprint(dashboard_bp)   app.register_blueprint(filmes_bp)   app.register_blueprint(favoritos_bp)
**18.** Qual controller cuida da página inicial `/`? Quais variáveis ele envia para o template `index.html`?
controllers/dashboard_controller.py. populares, melhores e buscas_recentes.
**19.** A pasta `services/tmdb_api.py` é Model, Controller ou View? Justifique: quem chama essa classe e para quê?
Faz parte do Service (não é Model, Controller nem View). Ela é chamada pelos Controllers para fazer requisições HTTP e buscar os dados de filmes diretamente na API do TMDB.
**20.** No controller de busca, de onde vem o termo digitado quando o usuário usa o formulário da home (`index.html`)? É `request.form` ou `request.args`? Explique a diferença nesse projeto.
Vem de request.args (via método GET na URL, como ?q=termo).

Diferença: request.args pega parâmetros da URL (usado em consultas/buscas), enquanto request.form pega dados enviados no corpo de formulários POST.

Bloco C — View
---

## Bloco C — View (perguntas 21 a 30)

**21.** Onde ficam os templates HTML? Qual caminho completo da pasta?
views/templates/.
**22.** Qual template é a “base” de todas as páginas (layout com menu)? Como os outros templates usam esse layout (qual comando Jinja)?
O template base é o views/templates/layout.html. Os outros usam a tag {% extends "layout.html" %} no início do arquivo.
**23.** Abra `views/templates/layout.html`. Liste os 5 links do menu e o `url_for` de cada um.
Links do menu em layout.html:

Home/Logo: url_for('dashboard.index')

Populares: url_for('filmes.populares')

Melhores: url_for('filmes.melhores')

Favoritos: url_for('favoritos.lista')

Buscar (no form): url_for('filmes.buscar')
**24.** Qual arquivo HTML exibe a seção **“Onde assistir (Brasil)”**? De onde vem a variável `streaming` usada nessa tela?
Arquivo: views/templates/filmes/detalhe.html.
A variável streaming vem da chamada TmdbApi().onde_assistir(filme_id) feita no filmes_controller.py.
**25.** O arquivo `filmes/_card.html` é uma página inteira ou um pedaço reutilizado? Quem inclui esse arquivo e com qual tag Jinja?
É um pedaço reutilizado (partial). É incluído por index.html, populares.html, melhores.html e buscar.html através da tag {% include "filmes/_card.html" %}.
**26.** Em `filmes/detalhe.html`, como a View sabe se o filme já está nos favoritos? Qual variável booleana/objeto controla o botão “Salvar” vs “Remover”?
Pela variável booleana eh_favorito enviada pelo controller. Se for True, exibe o botão de remover; se for False, exibe o de salvar.
**27.** Onde está o CSS do site? Como o `layout.html` carrega esse arquivo (função Flask/Jinja)?
Fica em views/static/css/style.css. O layout.html carrega com url_for('static', filename='css/style.css').
**28.** Na listagem de favoritos (`favoritos/lista.html`), qual loop Jinja percorre os registros? Cite 3 campos exibidos na tabela.
Loop: {% for filme in favoritos %}.
**29.** O que significa `{% if modo_demo %}` no layout? Quem disponibiliza essa variável para **todos** os templates?
Exibe um aviso no topo da página avisando que a aplicação está usando dados mockados/locais por falta da chave da API. Quem envia é a função inject_globals() via @app.context_processor no app.py.
**30.** Desenhe ou descreva o fluxo completo quando o aluno clica em **“Salvar favorito”** no detalhe do filme, indicando **View → Controller → Model** (e redirect de volta). Cite arquivos envolvidos.
View: Usuário clica no botão do formulário POST em views/templates/filmes/detalhe.html.Controller: A rota /favoritos/adicionar/<int:filme_id> em controllers/favoritos_controller.py recebe a requisição, busca os dados na API (TmdbApi().detalhe) e aciona o model.Model: FilmeFavorito.adicionar(...) em models/filme_favorito.py salva o filme no banco streamflix.db.  Redirect: O controller redireciona de volta para a View views/templates/filmes/detalhe.html.
---

## Entrega

- Arquivo `.txt` ou `.md` com as 30 respostas 

**Critério:** respostas que mostrem que você **abriu o código**, não chute.

Boa exploração!
