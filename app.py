from flask import Flask, render_template, request

app = Flask(__name__)

lista = ['pippo', 'pluto', 'paperino', 'paperone', 'minnie', 'topolino']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        elemento = request.form.get('elemento')
        lista.append(elemento)
        render_template("index.html", lista=lista)
        

    return render_template('index.html', lista=lista)

@app.route('/profilo')
def profilo():
    return "Questa è la pagina del profilo!"



if __name__ == '__main__':
    app.run(debug=True)