books = [
    {
        "name": "Lord of the rings",
        'price': 700
    },
    {
        'name': 'Fluent Python',
        'price': 650
    },
    {
        'name': 'Harry Potter',
        'price': 1300
    },
]
book = min(books, key=lambda x: x['price'])

print("The cheapest book is '%s'. It costs %d grn" % (book['name'], book['price']))
