from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
# db.resetDatabase()

def getPokemonByName(name: str):
    return db.collection.find({"name": name})

pikachu = getPokemonByName("Pikachu")
writeAJson(pikachu, "pikachu")

pokemonsBL = db.collection.find({"next_evolution.1.num": {"$lte": "020"}})
writeAJson(pokemonsBL, "pokemonsbelow020")

pokemonsBT = db.collection.find({"spawn_chance": {"$gt": 0.3, "$lt": 0.6}})
writeAJson(pokemonsBT, "pokemonsbetween03and06")

fraquezas = ["Psychic", "Ice"]
pokemonsF = db.collection.find({"weaknesses": {"$all": fraquezas}})
writeAJson(pokemonsF, "pokemonsweaknesses")

pokemonsG = db.collection.find({"type": "Grass"})
writeAJson(pokemonsG, "pokemonsgrass")

