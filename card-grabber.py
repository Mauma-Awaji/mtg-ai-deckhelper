import scrython

results = scrython.cards.Search(q="id:golgari otag:sacrifice-outlet game:paper")

for card in results.data:
    print(f"{card.name} - {card.set_name} - {card.prices}")