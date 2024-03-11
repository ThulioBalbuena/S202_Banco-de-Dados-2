from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
# db.resetDatabase()

def getPokemonByName(name: str):
    return db.collection.find({"name": name})

pikachu = getPokemonByName("Pikachu")
writeAJson(pikachu, "pikachu")

def getPokemonByType(type: str):
    return db.collection.find({"type": type})

pokemonsFire = getPokemonByType("Fire")
writeAJson(pokemonsFire, "pokemonsfire")

def getPokemonByNextEvolution(next_evolution: list):
    return db.collection.find({"next_evolution": next_evolution})

pokemonsNextEvolution = db.collection.find({"next_evolution": {"$exists": True}})
writeAJson(pokemonsNextEvolution, "pokemonsnextevolution")

def getPokemonBySpawnChance(spawn_chance: float):
    return db.collection.find({"spawn_chance": spawn_chance})

pokemonsSpawnChance = db.collection.find({"spawn_chance": {"$gt": 0.3, "$lt": 0.6}})
writeAJson(pokemonsSpawnChance, "pokemonsSpawnChance")

def getPokemonByWeaknesses(weaknesses: list):
    return db.collection.find({"weaknesses": weaknesses})

pokemonsWeaknesses = db.collection.find({"weaknesses": {"$in": ["Ground"]}})
writeAJson(pokemonsWeaknesses, "pokemonsWeaknesses")
