from fastapi import FastAPI
from models import Product

app=FastAPI()

@app.get("/")
def greet():
    return "Hello, World!"

products=[
    Product(id=1,name="Phone",description="budget phone ",price=99,quantity=10),
    Product(id=2,name="laptop",description="gaming laptop",price=999,quantity=6),
    Product(id=3,name="chai",description="Comfortable chair",price=1299,quantity=10),
    Product(id=4,name="car",description="Racing car",price=100000,quantity=2),
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product")
def get_product_by_id():
    return products[0]
    
@app.get("/about")
def about():
    return "This is about us page"

@app.get("/contact")
def contact():
    return "This is contact us page"
