from mongoengine import connect
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')

connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@cluster0.1ld4axf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0""", ssl=True)

if __name__ == "__main__":

    try:
        connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@cluster0.1ld4axf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0""", ssl=True)
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)