
from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')    
def layout():

    return render_template('index.html')

@app.route('/expectativas')    
def expectativas():

    return render_template('expectativas.html')


@app.route('/curriculo')    
def curriculo():

    return render_template('curriculo.html')





if __name__ == '__main__':
    app.run(debug=True)