from flask import Flask, render_template

app = Flask(__name__)

lista = ['pippo', 'pluto', 'paperino', 'paperone', 'minnie', 'topolino']

@app.route('/')
def index():
    return render_template('index.html', lista=lista)

@app.route('/profilo')
def profilo():
    return "Questa è la pagina del profilo!"

if __name__ == '__main__':
    app.run(debug=True)