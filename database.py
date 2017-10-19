from pymongo import MongoClient


def create_database(name):
    """
    If the database does not already exist
    this function will create it. If it does
    the function will simply return the database
    :param name: database name obviously.
    :return:
    """
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
