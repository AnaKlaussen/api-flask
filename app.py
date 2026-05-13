from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {"id": 1, "titulo": "Corte de Espinhos e Rosas"},
    {"id": 2, "titulo": "Quarta Asa"}
]

@app.route('/', methods=['GET'])
def listar_livros():
    return jsonify(livros)

@app.route('/', methods=['POST'])
def adicionar_livro():
    novo_livro = request.json
    livros.append(novo_livro)

    return jsonify({
        "mensagem": "Livro adicionado com sucesso!",
        "livro": novo_livro
    })

if __name__ == '__main__':
    app.run(debug=True)