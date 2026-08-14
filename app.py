def hello():
    return "Hello E-Commerce"


def get_product():
    return {
        "id": 1,
        "name": "Laptop",
        "price": 55000
    }

def login(username, password):
    if username == "admin" and password == "1234":
        return "Login successful"

    return "Invalid username or password"

def search_product(name):
      # Search product by name.
    return f"Searching for {name}"

def get_customer():
    return {
        "id": 1,
        "name": "Vijay"
    }

def process_payment(amount):
    return f"Payment of {amount} processed"

if __name__ == "__main__":
    print(hello())
    print(get_product())