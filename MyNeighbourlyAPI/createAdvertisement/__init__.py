import azure.functions as func
import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = os.environ["bamfa_cosmosdb_connection_string"]
            # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['bam-mongo-db']
            collection = database['advertisements']

            result = collection.insert_one(eval(request))
            print(result)

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )