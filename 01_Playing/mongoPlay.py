from datetime import datetime

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pandas import DataFrame
from dateutil import parser

import os
import datetime

from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("MONGO_USER")
db_pass = os.getenv("MONGO_PASS")
db_name = os.getenv("MONGO_NAME")


def get_database():
    uri = f"mongodb+srv://{db_user}:{db_pass}@cluster0.3n74soi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['user_shopping_list']


def get_id(collection):
    try:
        return get_database()[collection].find().sort("_id", -1).limit(1)[0]['_id'] + 1
    except IndexError:
        return 0


def get_orga_id(organame):
    return get_database()['orgas'].find({"name": organame.lower()})[0]['_id']


def get_date():
    return datetime.datetime.now().strftime("%c")


def insert_person(vorname, nachname, member_of=None, status=0):
    person = {
        "_id": get_id("persons"),
        "vorname": vorname,
        "nachname": nachname,
        "member_of": get_orga_id(member_of),
        "status": status,
        "date": get_date()
    }
    dbname = get_database()
    collection_name = dbname["persons"]
    collection_name.insert_one(person)


def insert_orga(name, locaton=0, status=0):
    orga = {
        "_id": get_id("orgas"),
        "name": name.lower(),
        "location": locaton,
        "status": status,
        "date": get_date()
    }
    dbname = get_database()
    collection_name = dbname["orgas"]
    collection_name.insert_one(orga)


def display_person_data(vorname=None):
    dbname = get_database()
    persons_collection = dbname["persons"]

    pipeline = [
        {
            "$lookup": {
                "from": "orgas",
                "localField": "member_of",
                "foreignField": "_id",
                "as": "orga_info"
            }
        },
        {
            "$match": {
                "vorname": "Aares",
                "nachname": None
            }
        },
        {
            "$project": {
                "_id": 1,
                "vorname": 1,
                "nachname": 1,
                "status": 1,
                "orga_name": {"$arrayElemAt": ["$orga_info.name", 0]}
            }
        }
    ]

    result = persons_collection.aggregate(pipeline)

    # Display the results
    for doc in result:
        print(
            f"Person ID: {doc['_id']}, Vorname: {doc['vorname']}, Name: {doc['nachname']}, Status: {doc['status']}, Orga Name: {doc['orga_name'].strip("[]'")}")


if __name__ == "__main__":
    # insert_orga("PD", 1291, 0)
    # insert_person("Hen", "dings", "fib", 0)
    # insert_person("Hen", "bums", "fib", 0)
    # print(get_orga_id("FIB"))

    # print(get_id("persons"))

    display_person_data()
