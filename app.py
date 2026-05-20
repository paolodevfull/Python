from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    
    nome = 'Ana'
    idade = '18'

    return render_template('index.html', nome = nome, idade = idade) 


@app.route('/dados_usuario')
def dados():
    
    dados_usuario = {"nome": "Ana", "email": "ana@email.com"}

    return render_template('dados.html', dados_usuario = dados_usuario) 

@app.route('/lista')
def lista():

    aluno = [
        {"nome": "Ana", "nota": "8"},
        {"nome": "Pedro", "nota": "4"}
    ]
    
    return render_template('alunos.html', aluno = aluno)

if __name__ == '__main__':
    app.run(debug=True)