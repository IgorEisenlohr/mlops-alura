from flask import Flask, request, jsonify
import pickle
from flask_basicauth import BasicAuth
import os

colunas = ['tamanho','ano','garagem']
with open(r'C:\Users\R2\Desktop\mlops-deploy\models\modelo.sav', 'rb') as file:
  model = pickle.load(file)

#app
app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD')

basic_auth = BasicAuth(app)

@app.route('/')
def home():
    return "Primeira API"


@app.route('/preco/', methods=['POST'])
@basic_auth.required
def valor_casa():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas]
    cotacao = model.predict([dados_input])
    return jsonify(preco=cotacao[0])


app.run(debug=True, host='0.0.0.0')