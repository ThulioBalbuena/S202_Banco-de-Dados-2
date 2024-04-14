class Passageiro:
    def __init__(self,nome, documento):
        self.nome = nome
        self.documento = documento

    def to_dict(self):
        return {
            "nome": self.nome,
            "documento": self.documento
        }
        

class Corrida:
    def __init__(self, nota, distancia, valor, passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro

    def to_dict(self):
        return {
            "nota": self.nota,
            "distancia": self.distancia,
            "valor": self.valor,
            "passageiro": self.passageiro.to_dict()
        }

class Motorista:
    corridas = []

    def __init__(self, nota, corridas):
        self.nota = nota
        self.corridas = corridas

    def to_dict(self):
        return {
            "nota": self.nota,
            "corridas": [corrida.to_dict() for corrida in self.corridas]
        }

# to-dict `otimiza` para inserir no banco de dados