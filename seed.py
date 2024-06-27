import json
import connection_to_db
from models import Author, Quote




def seed_file(file):
    with open(f"{file}", "r", encoding="utf-8") as fh:
        res = json.load(fh)
    return res

if __name__ == "__main__":
    file = "authors.json"
    file2 = "qoutes.json"
    author = Author()
    quote = Quote()
    for data in seed_file(file):
        author = Author(fullname=data.get("fullname"), born_date=data.get("born_date"), born_location=data.get("born_location"), description=data.get("description"))
        author.save()
        for data2 in seed_file(file2):
            quote = Quote(tags=data2.get("tags"), quote=data2.get("quote"), author=author)
            quote.save()
            continue

