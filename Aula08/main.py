from database import Database
from GameDatabase import GameDatabase

db = Database("bolt://44.192.59.240:7687", "neo4j", "chairwoman-saying-sprayers")

game_db = GameDatabase(db)

def create_player():
    name = input("Digite o nome do jogador: ")
    game_db.create_player(name)
    print(f"Jogador '{name}' criado com sucesso!")

def read_players():
    players = game_db.get_players()
    if players:
        print("Jogadores:")
        for player in players:
            print(player["name"])
    else:
        print("Não há jogadores cadastrados.")

def update_player():
    player_id = int(input("Digite o ID do jogador a ser atualizado: "))
    new_name = input("Digite o novo nome do jogador: ")
    game_db.update_player(player_id, new_name)
    print(f"Nome do jogador ID={player_id} atualizado para '{new_name}'.")

def delete_player():
    player_id = int(input("Digite o ID do jogador a ser excluído: "))
    game_db.delete_player(player_id)
    print(f"Jogador ID={player_id} excluído com sucesso!")

def create_match():
    players = input("Digite os nomes dos jogadores separados por vírgula: ").split(",")
    result = input("Digite o resultado da partida: ")
    game_db.create_match(players, result)
    print("Partida registrada com sucesso!")

def delete_match():
    match_id = int(input("Digite o ID da partida a ser excluída: "))
    game_db.delete_match(match_id)
    print(f"Partida ID={match_id} excluída com sucesso!")

def get_matches():
    matches = game_db.get_matches()
    if matches:
        print("Partidas registradas:")
        for match in matches:
            print(f"ID: {match['match_id']}, Resultado: {match['result']}")
    else:
        print("Não há partidas registradas.")

def get_player_matches():
    player_id = int(input("Digite o ID do jogador para obter seu histórico de partidas: "))
    matches = game_db.get_player_matches(player_id)
    if matches:
        print(f"Histórico de partidas do jogador ID={player_id}:")
        for match in matches:
            print(f"Partida ID={match['match_id']}, Resultado: {match['result']}")
    else:
        print(f"O jogador ID={player_id} não possui histórico de partidas.")

def close_connection():
    db.close()
    print("Conexão com o banco de dados fechada.")

# Menu interativo
while True:
    print("\nMenu:")
    print("1. Criar jogador")
    print("2. Listar jogadores")
    print("3. Atualizar jogador")
    print("4. Excluir jogador")
    print("5. Registrar partida")
    print("6. Excluir partida")
    print("7. Listar partidas")
    print("8. Histórico de partidas de um jogador")
    print("9. Fechar conexão com o banco de dados")
    print("10. Sair")

    choice = input("Escolha uma opção: ")

    if choice == "1":
        create_player()
    elif choice == "2":
        read_players()
    elif choice == "3":
        update_player()
    elif choice == "4":
        delete_player()
    elif choice == "5":
        create_match()
    elif choice == "6":
        delete_match()
    elif choice == "7":
        get_matches()
    elif choice == "8":
        get_player_matches()
    elif choice == "9":
        close_connection()
        break
    elif choice == "10":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
