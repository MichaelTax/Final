import pymongo
from pymongo import MongoClient
                                               #| DB Password   |
cluster = MongoClient("mongodb+srv://MichaelTax:2MrwXOs87ivaXfat@cluster0.n7gitx4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = cluster["Michael_Notes"]
collection = db["Michael_Notes"]

post1 ={"_id": 0, "name": "Michael"}
post2 ={"_id": 1, "name": "bill"}

results = collection.update_one({"_id":0}, {"$set":{"LastName":"Chad"}})
