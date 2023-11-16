import datetime as dt
import json
import connect
from models import Author,Tag,Qouts

with open('authors.json', 'r',encoding='utf-8') as authors_file:
    authors_data = json.load(authors_file)

with open('qoutes.json', 'r',encoding='utf-8') as quotes_file:
    quotes_data = json.load(quotes_file)

for author_data in authors_data:
    author = Author(fullname=author_data["fullname"],
                    born_date=dt.datetime.strptime(author_data["born_date"], "%B %d, %Y"),
                    born_location=author_data["born_location"],
                    description=author_data["description"])
    author.save()


tags = []

for quote_data in quotes_data:
    author_name = quote_data["author"]
    author = Author.objects(fullname=author_name).first()

    quote = Qouts(
        tags=[Tag(name=tag) for tag in quote_data["tags"]],
        author=author,
        qout=quote_data["quote"],
    )

    quote.save()
