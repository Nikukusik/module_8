import connection_to_db
from models import Author, Quote

def find_name(name):
    list_of_quotes = []
    author = Author.objects(fullname=name).first()
    quotes = Quote.objects(author=author._id)
    for quote in quotes:
        list_of_quotes.append(quote.quote)
    return list_of_quotes

def find_tag(tag):
    list_of_quotes = []
    quotes = Quote.objects(tags=tag)
    for quote in quotes:
        list_of_quotes.append(quote.quote)
    return list_of_quotes

def find_tags(tags):
    list_of_quotes = []
    tags = tags.split(',')
    quotes = Quote.objects(tags__in=tags)
    for quote in quotes:
        list_of_quotes.append(quote.quote)
    return list_of_quotes



if __name__ == "__main__":
    while(True):
        text = input().split(":")
        if text[0] == "name":
            print(find_name(text[1]))
        elif text[0] == "tag":
            print(find_tag(text[1]))
        elif text[0] == "tags":
            print(find_tags(text[1]))
        elif text[0] == "close":
            break

