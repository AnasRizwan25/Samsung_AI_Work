products = [
    {
        "name": "electronic",
        "price": 300
    },
    {
        "name": "clothing",
        "price": 500
    },
    {
        "name": "grocery",
        "price": 200
    }
]
def ratio_of_sale(product):
    total = 0
    new_product = []
    for i in product:
        total += i["price"]
    new_product = []
    for i in product:
        new_product.append({
            "name": i["name"],
            "price": i["price"] / total
        })
    return new_product

a = ratio_of_sale(products)

def ratio_percent(a):
    new_product = []
    for i in a:
        new_product.append({
            "name": i["name"],
            "price": i["price"] * 100
        })
    return new_product

b = ratio_percent(a)
print(b)