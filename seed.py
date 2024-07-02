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

def load_quotes(file, author):
    with open(f"{file}", "r", encoding="utf-8") as fh:
        data = json.load(fh)
        for quote in data:
            if quote["author"] == f"{author.fullname}":
                quo = Quote(tags=quote.get("tags"),
                            author=author._id,
                            quote=quote.get("quote"))
                quo.save()
if __name__ == "__main__":
    quotes = Quote.objects()
    authors = Author.objects()
    for quote in quotes:
        quote.delete()
    for author in authors:
        author.delete()

    file = "authors.json"
    file2 = "qoutes.json"
    load_authors(file)
    authors = Author.objects()
    for author in authors:
        load_quotes(file2, author)


