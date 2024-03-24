from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['biblioteca']

livros_schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["_id", "titulo", "autor", "ano", "preco"],
        "properties": {
            "_id": {
                "bsonType": ["string", "int"],
                "description": "deve ser uma string ou um inteiro e é obrigatório"
            },
            "titulo": {
                "bsonType": "string",
                "description": "deve ser uma string e é obrigatório"
            },
            "autor": {
                "bsonType": "string",
                "description": "deve ser uma string e é obrigatório"
            },
            "ano": {
                "bsonType": "int",
                "description": "deve ser um inteiro e é obrigatório"
            },
            "preco": {
                "bsonType": "double",
                "description": "deve ser um número de ponto flutuante e é obrigatório"
            }
        }
    }
}

livros_collection = db.get_collection('Livros')

def menu():
    print("\nMenu:")
    print("1. Adicionar livro")
    print("2. Atualizar livro")
    print("3. Remover livro")
    print("4. Listar todos os livros")
    print("5. Sair")

def adicionar_livro():
    _id = input("Digite o ID do livro: ")
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = int(input("Digite o ano do livro: "))
    preco = float(input("Digite o preço do livro: "))
    livro = {"_id": _id, "titulo": titulo, "autor": autor, "ano": ano, "preco": preco}
    livros_collection.insert_one(livro)
    print("Livro adicionado com sucesso!")

def atualizar_livro():
    _id = input("Digite o ID do livro que deseja atualizar: ")
    livro = livros_collection.find_one({"_id": _id})
    if livro:
        titulo = input("Digite o novo título do livro (ou pressione Enter para manter o atual): ")
        autor = input("Digite o novo autor do livro (ou pressione Enter para manter o atual): ")
        ano = input("Digite o novo ano do livro (ou pressione Enter para manter o atual): ")
        preco = input("Digite o novo preço do livro (ou pressione Enter para manter o atual): ")
        update_data = {}
        if titulo:
            update_data["titulo"] = titulo
        if autor:
            update_data["autor"] = autor
        if ano:
            update_data["ano"] = int(ano)
        if preco:
            update_data["preco"] = float(preco)
        livros_collection.update_one({"_id": _id}, {"$set": update_data})
        print("Livro atualizado com sucesso!")
    else:
        print("Livro não encontrado.")

def remover_livro():
    _id = input("Digite o ID do livro que deseja remover: ")
    result = livros_collection.delete_one({"_id": _id})
    if result.deleted_count:
        print("Livro removido com sucesso!")
    else:
        print("Livro não encontrado.")

def listar_livros():
    livros = livros_collection.find()
    print("\nLista de Livros:")
    for livro in livros:
        print("ID:", livro["_id"])
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])
        print("Preço:", livro["preco"])
        print("--------------------")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_livro()
    elif opcao == "2":
        atualizar_livro()
    elif opcao == "3":
        remover_livro()
    elif opcao == "4":
        listar_livros()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
