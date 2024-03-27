from flask import Flask, make_response, jsonify, request
from banquinho import Database

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

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


@app.route('/busca', methods=['GET'])
def get_produtos_por_nome():
    nome_produto = request.args.get('nome')

    if nome_produto is None:
        return make_response(jsonify({"mensagem": "Por favor, forneça o parâmetro 'nome' na busca."}), 400)

    db = Database()
    produtos = db.consulta_produtos_por_nome(nome_produto)

    if not produtos:
        return make_response(jsonify({"mensagem": f"Nenhum produto encontrado com o nome '{nome_produto}'."}), 404)

    produtos_formatados = []
    for produto in produtos:
        produto_formatado = {
            'id': produto['id'],
            'nome': produto['nome'],
            'empresa': produto['empresa'],
            'descricao': produto['descricao'],
            'quantidade': produto['quantidade'],
            'marca': produto['marca'],
            'valor': produto['valor']
        }
        produtos_formatados.append(produto_formatado)

    return make_response(jsonify(produtos_formatados))




app.run(debug=True, host="0.0.0.0")
