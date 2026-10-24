# Exercise 7: Shopping Cart

products = [
    {"name": "Notebook", "price": 120, "quantity": 3},
    {"name": "Pen", "price": 20, "quantity": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Mouse", "price": 650, "quantity": 1}
]

total = 0

for product in products:
    total = total + product["price"] * product["quantity"]

def apply_discount(total):
    if total >= 2000:
        return total * 0.90
    else:
        return total

print("Total:", total)
print("Final Price:", apply_discount(total))