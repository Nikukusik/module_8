from mongoengine import connect
import configparser
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')

connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@cluster0.1ld4axf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0""", ssl=True)

if __name__ == "__main__":
    uri = f"mongodb+srv://{mongo_user}:{mongodb_pass}@cluster0.1ld4axf.mongodb.net/?appName=Cluster0"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)