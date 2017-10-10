from pymongo import MongoClient


def create_database(name):
    client = MongoClient()
    db = client[name]
    return db


def create_collection(db, name):
    collection = db[name]
    return collection


def insert_document(collection, doc):
    doc_id = collection.insert_one(doc).inserted_id
    return doc_id


if __name__ == '__main__':
    user_example = {
        'username': 'kurtprice',
        'password': 'password',
        'cards': ['CSR', 'CFU', 'CF'],
    }
    db = create_database("finance")
    coll = create_collection(db, "users")
    doc_id = insert_document(coll, user_example)
    print(doc_id)
