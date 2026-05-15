from flask import Flask, jsonify, request

app = Flask(__name__)

# dados de exemplo
livros = [
    {"id": 1, "titulo": "Corte de Espinhos e Rosas"},
    {"id": 2, "titulo": "Quarta Asa"}
]

# rota principal com todos os endpoints disponíveis
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "mensagem": "API da Livraria funcionando!",
        "endpoints": {
            "GET /livros": "Listar todos os livros",
            "GET /livros/<id>": "Buscar um livro pelo ID",
            "POST /livros": "Adicionar um novo livro",
            "PUT /livros/<id>": "Atualizar um livro existente",
            "DELETE /livros/<id>": "Remover um livro"
        }
    })

# GET - listar todos os livros
@app.route('/livros', methods=['GET'])
def listar_livros():
    return jsonify({"livros": livros})

# GET - buscar um livro específico pelo id
@app.route('/livros/<int:livro_id>', methods=['GET'])
def buscar_livro(livro_id):
    livro = next((l for l in livros if l["id"] == livro_id), None)

    if livro:
        return jsonify({"livro": livro})

    return jsonify({"erro": "Livro não encontrado"}), 404

# POST - adicionar um novo livro
@app.route('/livros', methods=['POST'])
def adicionar_livro():
    novo_livro = {
        "id": len(livros) + 1,
        "titulo": request.json["titulo"]
    }

    livros.append(novo_livro)

    return jsonify({
        "mensagem": "Livro adicionado com sucesso!",
        "livro": novo_livro
    }), 201

# PUT - atualizar um livro existente
@app.route('/livros/<int:livro_id>', methods=['PUT'])
def atualizar_livro(livro_id):
    livro = next((l for l in livros if l["id"] == livro_id), None)

    if livro:
        livro["titulo"] = request.json["titulo"]
        return jsonify({"livro": livro})

    return jsonify({"erro": "Livro não encontrado"}), 404

# DELETE - remover um livro
@app.route('/livros/<int:livro_id>', methods=['DELETE'])
def deletar_livro(livro_id):
    global livros
    livros = [l for l in livros if l["id"] != livro_id]

    return jsonify({"resultado": True})

if __name__ == '__main__':
    app.run(debug=True)