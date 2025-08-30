from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env
# Connect to MongoDB
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["fastapi"]         # Database name
collection = db["products"]       # Collection name

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","https://fast-api-learning.vercel.app"],  # Correct key!
    allow_methods=["*"],
    allow_headers=["*"],                      # Also important
)



def product_helper(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "description": product["description"],
        "price": product["price"],
        "quantity": product["quantity"]
    }

# products=[
#     Product(id=1,name="Phone",description="budget phone ",price=99,quantity=10),
#     Product(id=2,name="laptop",description="gaming laptop",price=999,quantity=6),
#     Product(id=3,name="chai",description="Comfortable chair",price=1299,quantity=10),
#     Product(id=4,name="car",description="Racing car",price=100000,quantity=2),
# ]

# @app.get("/products")
# def get_all_products():
#     return products
@app.get("/")
def home():
    return "Hello JI"

    
@app.get("/products")
def get_all_products():
    products = []
    for product in collection.find():
        products.append(product_helper(product))
    return products



# @app.get("/product")
# def get_product_by_id():
#     return products[0]

#dynamic route
# @app.get("/product/{id}")
# def get_product_by_id(id:int):
#     for product in products:
#         if product.id==id:
#             return product
#     return "Product not found"
@app.get("/product/{id}")
def get_product_by_id(id: str):
    product = collection.find_one({"_id": ObjectId(id)})
    if product:
        return product_helper(product)
    raise HTTPException(status_code=404, detail="Product not found")


#post
# @app.post("/product")
# def add_product(product:Product):
#     products.append(product)
#     return product
@app.post("/products")
def add_product(product: Product):
    result = collection.insert_one(product.dict())
    new_product = collection.find_one({"_id": result.inserted_id})
    return product_helper(new_product)


#update
# @app.put("/product/{id}")
# def update_product(id: int, product: Product):
#     for i in range(len(products)):
#         if products[i].id == id:
#             products[i] = product
#             return {"message": "Product updated successfully"}
#     return {"message": "Product not found"}
@app.put("/products/{id}")
def update_product(id: str, product: Product):
    result = collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": product.dict()}
    )
    if result.modified_count == 1:
        return {"message": "Product updated successfully"}
    raise HTTPException(status_code=404, detail="Product not found")



#delete
# @app.delete("/product")
# def delete_product(id:int):
#     for i in range(len(products)):
#         if products[i].id==id:
#             del products[i]
#             return "Products deleted"
#     return "Product not found"
@app.delete("/products/{id}")
def delete_product(id: str):
    result = collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": "Product deleted successfully"}
    raise HTTPException(status_code=404, detail="Product not found")




@app.get("/about")
def about():
    return "This is about us page"

@app.get("/contact")
def contact():
    return "This is contact us page"


