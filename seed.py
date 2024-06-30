import json
import connection_to_db
from models import Author, Quote




def load_authors(file):
    with open(f"{file}", "r", encoding="utf-8") as fh:
        data = json.load(fh)
        for author in data:
            aut = Author(fullname=author.get("fullname"),
                         born_date=author.get("born_date"),
                         born_location=author.get("born_location"),
                         description=author.get("description"))
            aut.save()

if __name__ == "__main__":
    file = "authors.json"
    file2 = "qoutes.json"
    load_authors(file)


