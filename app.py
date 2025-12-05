from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

#Category Endpoints
@app.post ("/categories")
def create_category():
    return {"message": "Category created successfully"}

@app.get("/categories")
def get_categories():
    return []

@app.get("/categories/{category_id}")
def get_category(category_id):
    return {"id": category_id}

@app.patch("/categories/{category_id}")
def update_category(category_id):
    return {"message": "Category updated successfully"}

@app.delete("/categories/{category_id}")
def delete_category(category_id):
    return {"message": "Category deleted successfully"}

#Product Endpoints
@app.post("/products")
def create_product():
    return {"message": "Product created successfully"}

@app.get("/products")
def get_products():
    return []

@app.get("/products/{product_id}")
def get_product(product_id):
    return {"id": product_id}

@app.patch("/products/{product_id}")
def update_product(product_id):
    return {"message": "Product updated successfully"}

@app.delete("/products/{product_id}")
def delete_product(product_id):
    return {"message": "Product deleted successfully"}


#Order Endpoints
@app.post("/orders")
def create_order():
    return {"message": "Order created successfully"}

@app.get("/orders")
def get_orders():
    return []

@app.get("/orders/{order_id}")
def get_order(order_id):
    return {"id": order_id}

@app.patch("/orders/{order_id}")
def update_order(order_id):
    return {"message": "Order updated successfully"}

@app.delete("/orders/{order_id}")
def delete_order(order_id):
    return {"message": "Order deleted successfully"}