from database import Database
from helper.writeAJson import writeAJson

db = Database(database="mercado", collection="produtos")

class ProductAnalyzer:
    result = db.collection.aggregate([
         {
        "$group": {
            "_id": "$data_compra",
            "total_sales": {"$sum": 1}
        }
    }
    ])
    writeAJson(result, "Total de vendas por dia")


    result = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
        {"$sort": {"total": -1}},
        {"$limit": 1}
    ])
    writeAJson(result, "Produto mais vendido")


    result = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
        {"$sort": {"total": -1}},
        {"$limit": 1}
    ])
    writeAJson(result, "Cliente que mais gastou")

    result = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$match": {"produtos.quantidade": {"$gt": 1}}}, 
        {"$group": {"_id": "$produtos.descricao"}}
    ])

    writeAJson(result, "Produtos que venderam mais de 1 unidade")


