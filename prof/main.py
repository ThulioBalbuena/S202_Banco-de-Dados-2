from teacher_crud import TeacherCRUD
from database import Database

db = Database("bolt://44.192.11.117:7687", "neo4j", "convenience-checkpoint-confidences")
crud = TeacherCRUD(db)

option = 0

while option != 5:
    print("1 - Criar professor")
    print("2 - Buscar professor")
    print("3 - Atualizar cpf professor")
    print("4 - Deletar professor")
    print("5 - Sair")
    
    try:
        option = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Opção inválida. Por favor, digite um número entre 1 e 5.")
        continue
    
    if option == 1:
        name = input("Digite o nome do professor: ")
        try:
            ano_nasc = int(input("Digite o ano de nascimento do professor: "))
        except ValueError:
            print("Ano de nascimento inválido. Por favor, digite um ano válido.")
            continue
        cpf = input("Digite o cpf do professor: ")
        crud.create_teacher(name, ano_nasc, cpf)
    elif option == 2:
        name = input("Digite o nome do professor: ")
        teacher = crud.read_teacher(name)
        if teacher:
            print(f'Nome: {teacher[0]["t.name"]}, Ano de nascimento: {teacher[0]["t.ano_nasc"]}, CPF: {teacher[0]["t.cpf"]}')
        else:
            print("Professor não encontrado.")
    elif option == 3:
        name = input("Digite o nome do professor: ")
        new_cpf = input("Digite o novo cpf do professor: ")
        crud.update_teacher(name, new_cpf)
    elif option == 4:
        name = input("Digite o nome do professor: ")
        crud.delete_teacher(name)
    elif option == 5:
        db.close()
    else:
        print("Opção inválida. Por favor, digite um número entre 1 e 5.")
