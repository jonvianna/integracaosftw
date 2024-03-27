from flask import Flask, make_response, jsonify, request
from banquinho import Database

app = Flask(__name__)

@app.route("/produtos", methods=['GET'])
def get_produtos():
    db = Database()
    meus_produtos = db.consulta_produtos()

    produtos = list()
    for produto in meus_produtos:
        produtos.append(
            {
                'id': produto[0],
                'nome': produto[1],
                'empresa': produto[2],
                'descricao': produto[3],
                'quantidade': produto[4],
                'marca': produto[5],
                'valor': produto[6]
            }
        )

    return make_response(
        jsonify(
            produtos
        )
    )


@app.route('/produtos', methods=['POST'])
def create_produto():
    produto = request.json

    db = Database()
    db.create_produto(produto)

    return make_response(
        jsonify(
            mensagem="Produto cadastrado com sucesso",
            produto = produto
        )
    )


app.run(debug=True, host="0.0.0.0")