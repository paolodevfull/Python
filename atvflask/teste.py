
#Crie uma aplicação Flask que contenha uma rota específica responsável por explicar o conceito de decorator em Python.
#Requisitos
#Crie uma rota acessível por meio do caminho: /decorator
#Ao acessar essa rota no navegador, deve ser exibido um texto explicando:
#O que é um decorator em Python
#Para que ele serve
#Como ele é utilizado no Flask (exemplo: @app.route)


from flask import Flask

app = Flask(__name__)

@app.route('/decorator') # ----> o / puxa direto do raiz caso o codigo esteja em outro arquivo tem que colocar o caminho
def explicacaodecorator():  
    explicacao = """
    
    É uma ferramenta que permite modificar, estender ou envolver o comportamento de funções ou métodos existentes, sem alterar o seu código original. </br>
    É usada para reutilizar funções e logicas de codigos </br>
    No framework Flask, os decorators são essenciais para o mapeamento de URLs (roteamento). O @app.route() associa uma URL específica a uma função de visualização (view function)
    
    """
    return explicacao



if __name__ == '__main__':
    app.run(debug=True)