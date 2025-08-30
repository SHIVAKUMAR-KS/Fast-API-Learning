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

# @app.get("/product")
# def get_product_by_id():
#     return products[0]

#dynamic route
@app.get("/product/{id}")
def get_product_by_id(id:int):
    for product in products:
        if product.id==id:
            return product
    return "Product not found"

#post
@app.post("/product")
def add_product(product:Product):
    products.append(product)
    return product

#update
@app.put("/product/{id}")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return {"message": "Product updated successfully"}
    return {"message": "Product not found"}


#delete
@app.delete("/product")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id==id:
            del products[i]
            return "Products deleted"
    return "Product not found"



@app.get("/about")
def about():
    return "This is about us page"

@app.get("/contact")
def contact():
    return "This is contact us page"


