class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self, assunto):
        return f"O professor {self.nome} está ministrando uma aula sobre {assunto}."

class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def presenca(self):
        return f"O aluno {self.nome} está presente."

class Aula:
    def __init__(self, professor, assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_presenca(self):
        presenca_aula = f"Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:"
        for aluno in self.alunos:
            presenca_aula += f"\n{aluno.presenca()}"
        return presenca_aula

professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
print(aula.listar_presenca())

# exemplos mongodb:
#db.paises.find({},{ "name.official": 1, "_id": 0 }).filter({ "region": "Americas", "area": { $lt: 100 } }) Mostrar apenas o nome oficial dos países que são da região "Americas" e possuem área menor que 100:
#db.paises.find({},{ "name.common": 1, "_id": 0 }).filter({ "name.common": { $regex: "^B", $options: "i" } }).sort({ "area": 1 })Mostrar apenas o nome comum dos países que começam com "B" e ordenar os resultados por ordem crescente de área:
#db.paises.find({},{ "name.common": 1, "latlng": 1, "_id": 0 }).filter({ "languages": "por" }) Mostrar apenas o nome comum dos países que começam com "B" e ordenar os resultados por ordem crescente de área:
#db.paises.find({},{ "name.common": 1, "borders": 1, "_id": 0 }).filter({ "borders": { $size: 0 } }) Mostrar apenas o nome comum dos países que não possuem fronteiras:
#db.paises.find({},{ "name.common": 1, "borders": 1, "_id": 0 }).filter({ "borders": { $size: 1 } }) Mostrar apenas o nome comum dos países que possuem apenas uma fronteira:

#exemplos neo4j:
#MATCH (p:Person) WHERE p.name = 'Tom Hanks' RETURN p
#MATCH (m:Movie) WHERE m.title = 'The Matrix' RETURN m
#MATCH (p:Person)-[:ACTED_IN]->(m:Movie) WHERE m.title = 'The Matrix' RETURN p




