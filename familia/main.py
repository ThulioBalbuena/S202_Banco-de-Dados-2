from neo4j import GraphDatabase

##codigos usados para criar os nos e relacoes no neo4j
#Criar nodes
# CREATE (:Pessoa:Engenheiro {nome: "Thiago", sexo: "Masculino", idade: 50}) 
# CREATE (:Pessoa:Advogado {nome: "Roberta", sexo: "Feminino", idade: 48})
# CREATE (:Pessoa:Pintor {nome: "Paulo", sexo: "Masculino", idade: 18})
# CREATE (:Pessoa:Atriz {nome: "Júlia", sexo: "Feminino", idade: 17})
# CREATE (:Pessoa:Cantora {nome: "Fernanda", sexo: "Feminino", idade: 35})
# CREATE (:Pessoa:Jogador {nome: "Lucas", sexo: "Masculino", idade: 32})
# CREATE (:Pessoa:Modelo {nome: "Amanda", sexo: "Feminino", idade: 40})
# CREATE (:Pet:Gato {nome: "Tigre", especie: "Felina", cor: "Branco"})
# CREATE (:Pet:Cachorro {nome: "Leao", especie: "Canina", cor: "Marrom"})
# CREATE (:Pet:Peixe {nome: "Baiacu", especie: "Aquatica", cor: "Cinza"})
#Criar relacoes
# MATCH (thiago:Pessoa {nome: "Thiago"}), (paulo:Pessoa {nome: "Paulo"}), (julia:Pessoa {nome: "Júlia"})
# CREATE (thiago)-[:PAI_DE]->(paulo), (thiago)-[:PAI_DE]->(julia)

# MATCH (roberta:Pessoa {nome: "Roberta"}), (paulo:Pessoa {nome: "Paulo"}), (julia:Pessoa {nome: "Júlia"})
# CREATE (roberta)-[:ESPOSO_DE]->(thiago), (thiago)-[:ESPOSO_DE]->(roberta), (roberta)-[:PAI_DE]->(paulo), (roberta)-[:PAI_DE]->(julia)

# MATCH (thiago:Pessoa {nome: "Thiago"}), (roberta:Pessoa {nome: "Roberta"}), (paulo:Pessoa {nome: "Paulo"})
# CREATE (paulo)-[:FILHO_DE]->(thiago), (paulo)-[:FILHO_DE]->(roberta)

# MATCH (thiago:Pessoa {nome: "Thiago"}), (roberta:Pessoa {nome: "Roberta"}), (julia:Pessoa {nome: "Júlia"})
# CREATE (julia)-[:FILHO_DE]->(thiago), (julia)-[:FILHO_DE]->(roberta)

# MATCH (roberta:Pessoa {nome: "Roberta"}), (fernanda:Pessoa {nome: "Fernanda"}), (lucas:Pessoa {nome: "Lucas"})
# CREATE (fernanda)-[:ESPOSO_DE]->(lucas),(lucas)-[:ESPOSO_DE]->(fernanda), (fernanda)-[:IRMAO_DE]->(roberta), (roberta)-[:IRMAO_DE]->(fernanda)

# MATCH (lucas:Pessoa {nome: "Lucas"}), (leao:Pet {nome: "Leao"}), (amanda:Pessoa {nome: "Amanda"})
# CREATE (lucas)-[:DONO_DE]->(leao) , (amanda)-[:IRMAO_DE]->(lucas)

# MATCH (fernanda:Pessoa {nome: "Fernanda"}), (tigre:Pet {nome: "Tigre"})
# CREATE (fernanda)-[:DONO_DE]->(tigre)

# MATCH (lucas:Pessoa {nome: "Lucas"}), (leao:Pet {nome: "Leao"})
# CREATE (leao)-[:TEM_DONO]->(lucas)

# MATCH (amanda:Pessoa {nome: "Amanda"}), (tigre:Pet {nome: "Tigre"})
# CREATE (amanda)-[:TEM_DONO]->(tigre)

#Criando o aquario do THiago
# MATCH (pessoa:Pessoa {nome: "Thiago"})
# SET pessoa.temAquario = true

# MATCH (baiacu:Pet {nome: "Baiacu"}), (pessoa:Pessoa {nome: "Thiago"})
# CREATE (baiacu)-[:PERTENCE_AO {tipo: "Aquário"}]->(pessoa) #baiacu pertence ao aquario do thiago


class FamilyQueryClient:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def who_is_professional(self, profession):
        with self._driver.session() as session:
            result = session.run(
                "MATCH (p:Pessoa:{}) RETURN p.nome AS name".format(profession))
            return [record["name"] for record in result]

    def find_siblings_of(self, person_name):
        with self._driver.session() as session:
            result = session.run(
                "MATCH (sibling:Pessoa {nome: $name})-[:IRMAO_DE]-(other_sibling) RETURN other_sibling.nome AS name",
                name=person_name)
            return [record["name"] for record in result]

    def find_owner_of_pet(self, pet_name):
        with self._driver.session() as session:
            result = session.run(
                "MATCH (:Pet {nome: $pet_name})<-[:DONO_DE]-(dono:Pessoa) RETURN dono.nome AS owner",
                pet_name=pet_name)
            return [record["owner"] for record in result]
        
    def who_is_parent_of(self, person_name):
        with self._driver.session() as session:
            result = session.run(
                "MATCH (parent:Pessoa)-[:PAI_DE]->(child:Pessoa {nome: $name}) RETURN parent.nome AS name",
                name=person_name)
            return [record["name"] for record in result]

    def find_partner_of(self, person_name):
        with self._driver.session() as session:
            result = session.run(
                "MATCH (person1:Pessoa {nome: $name})-[:ESPOSO_DE]->(partner:Pessoa) RETURN partner.nome AS name",
                name=person_name)
            return [record["name"] for record in result]

    def find_pet_species(self, pet_name):
        with self._driver.session() as session:
            result = session.run(
                "MATCH (pet:Pet {nome: $pet_name}) RETURN labels(pet)[1] AS species",
                pet_name=pet_name)
            return [record["species"] for record in result]



uri = "neo4j+ssc://3e3118a6.databases.neo4j.io"
user = "neo4j"
password = "dYUdax8W0Wx7Eq7n2TqbBvdMIoXd6U6zKVkFZ0QEDHI"

client = FamilyQueryClient(uri, user, password)

print("1. Quem na família é Engenheiro?")
engineers = client.who_is_professional("Engenheiro")
print(engineers)

print("2. Paulo é irmão de quem?")
siblings = client.find_siblings_of("Paulo")
print(siblings)

print("3. Quem é a dona do Tigre?")
owners = client.find_owner_of_pet("Tigre")
print(owners)

print("4. Quem é o pai e mãe de Julia?")
parents = client.who_is_parent_of("Júlia")
print(parents)

print("5. Quem é a esposa de Lucas?")
partner = client.find_partner_of("Lucas")
print(partner)

print("6. Qual é a espécie do Baiacu?")
species = client.find_pet_species("Baiacu")
print(species)


client.close()
