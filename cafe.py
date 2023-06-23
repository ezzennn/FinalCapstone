# Define menu items and their respective stock and price
menu = {'coffee': {'stock': 10, 'price': 2},
        'tea': {'stock': 5, 'price': 1.5},
        'sandwich': {'stock': 3, 'price': 5.5},
        'cake': {'stock': 6, 'price': 4}}

# Calculate the total stock worth in the cafe
total_stock_worth = 0
for item in menu:
    total_stock_worth += menu[item]['stock'] * menu[item]['price']

print(f"Total stock worth in the cafe: ${total_stock_worth:.2f}")