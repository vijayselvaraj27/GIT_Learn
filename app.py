def hello():
    return "Hello E-Commerce"


def get_product():
    return {
        "id": 1,
        "name": "Laptop",
        "price": 50000
    }


if __name__ == "__main__":
    print(hello())
    print(get_product())