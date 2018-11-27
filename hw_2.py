"""
Find the cheapest book

books = [
{
‘name’: ‘Lord of the rings’,
‘price’: 700
},
{
‘name’: ‘Harry Potter’,
‘price’: 1300
},
{
‘name’: ‘Fluent Python’,
‘price’: 650
}
]

Your script should return: The cheapest book is ‘Fluent Python’. It costs 650 grn.
"""

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
print("The cheapest book is {name}. It costs {price} grn".format(name=book['name'], price=book['price']))
