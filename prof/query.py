from database import Database

db = Database("bolt://44.192.11.117:7687", "neo4j", "convenience-checkpoint-confidences")

class QueryHandler:
    def __init__(self, db):
        self.db = db

    #1) A
    def getRenzoDetails(self):
        query = "MATCH (t:Teacher {name: 'Renzo'}) RETURN t.ano_nasc, t.cpf"
        return self.db.execute_query(query)

    #B   
    def getTeachersStartingWithM(self):
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name, t.cpf"
        return self.db.execute_query(query)

    #C
    def getAllCities(self):
        query = "MATCH (c:City) RETURN c.name"
        return self.db.execute_query(query)

    #D
    def getSchoolsInRange(self):
        query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address, s.number"
        return self.db.execute_query(query)

    #2) A
    def getYoungestAndOldestTeacher(self):
        query = "MATCH (t:Teacher) RETURN t.name, substring(t.name, 3, 1)"
        return self.db.execute_query(query)
    
    #B
    def getCityPopulations(self):
        query = "MATCH (c:City) RETURN c.name, c.population"
        return self.db.execute_query(query)
    
    #C
    def getCityWithModifiedName(self):
        query = "MATCH (c:City) WHERE c.cep = '37540-000' RETURN replace(c.name, 'a', 'A')"
        return self.db.execute_query(query)
    
    #D
    def getTeachersWithCharAtPosition(self):
        query = "MATCH (t:Teacher) RETURN t.name, substring(t.name, 3, 1)"
        return self.db.execute_query(query)

query_handler = QueryHandler(db)

print("1) A")
result = query_handler.getRenzoDetails()
print(f'Ano de nascimento: {result[0]["t.ano_nasc"]}, CPF: {result[0]["t.cpf"]}')

print("\n1) B")
result = query_handler.getTeachersStartingWithM()
for item in result:
    print(f'Nome: {item["t.name"]}, CPF: {item["t.cpf"]}')

print("\n1) C")
result = query_handler.getAllCities()
for item in result:
    print(f'Cidade: {item["c.name"]}')

print("\n1) D")
result = query_handler.getSchoolsInRange()
for item in result:
    print(f'Nome: {item["s.name"]}, Endereço: {item["s.address"]}, Número: {item["s.number"]}')

print("\n2) A")
result = query_handler.getYoungestAndOldestTeacher()
for item in result:
    print(f'Nome: {item["t.name"]}, Terceira letra: {item["substring(t.name, 3, 1)"]}')

print("\n2) B")
result = query_handler.getCityPopulations()
for item in result:
    print(f'Cidade: {item["c.name"]}, População: {item["c.population"]}')

print("\n2) C")
result = query_handler.getCityWithModifiedName()
for item in result:
    print('Cidade: {}'.format(item["replace(c.name, 'a', 'A')"]))

print("\n2) D")
result = query_handler.getTeachersWithCharAtPosition()
for item in result:
    print(f'Char 3: {item["substring(t.name, 3, 1)"]}')
