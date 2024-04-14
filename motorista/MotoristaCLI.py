from UML import Motorista, Corrida, Passageiro

class MotoristaCLI:
    def __init__(self, motorista_model):
        self.motorista_model = motorista_model
        
    def create_motorista(self):
        corridas = self.create_corridas()
        nota = input("Digite a nota do motorista: ")
        motorista = Motorista(nota, corridas)
        self.motorista_model.create_motorista(motorista.to_dict())

        
    def create_passageiro(self):
        nome = input("Digite o nome do passageiro: ")
        documento = input("Digite o documento do passageiro: ")
        passageiro = Passageiro(nome, documento)
        return passageiro

    def create_corridas(self):
        corridas = []
        while True:
            passageiro = self.create_passageiro()
            nota = int(input("Digite a nota da corrida: "))
            distancia = float(input("Digite a distância percorrida: "))
            valor = float(input("Digite o valor da corrida: "))
            corrida = Corrida(nota, distancia, valor, passageiro)
            corridas.append(corrida)
            adicionar_outra = input("Deseja adicionar outra corrida? (s/n): ")
            if adicionar_outra.lower() != "s":
                break
        return corridas

    def read_motorista(self):
        id = input("Digite o id do motorista: ")
        self.motorista_model.read_motorista(id)

    def update_motorista(self):
        id = input("Digite o id do motorista: ")
        corridas = self.create_corridas()
        nota = input("Digite a nota do motorista: ")
        motorista = Motorista(nota, corridas)
        self.motorista_model.update_motorista(id, motorista.to_dict())

    def delete_motorista(self):
        id = input("Digite o id do motorista: ")
        self.motorista_model.delete_motorista(id)

    def menu(self):
        print("### Menu do Motorista ###")
        print("1. Criar motorista")
        print("2. Ler motorista")
        print("3. Atualizar motorista")
        print("4. Deletar motorista")
        print("5. Sair")

    def run(self):
        while True:
            self.menu()
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.create_motorista()
            elif opcao == "2":
                self.read_motorista()
            elif opcao == "3":
                self.update_motorista()
            elif opcao == "4":
                self.delete_motorista()
            elif opcao == "5":
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida. Tente novamente.")
