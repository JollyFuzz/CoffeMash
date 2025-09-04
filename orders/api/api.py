
from datetime import datetime

from http import HTTPStatus
from uuid import UUID
from starlette import status
from starlette.responses import Response
from random import randint

from orders.app import app 
from orders.api.schemas import CreateOrderSchema

orders = []

order = {
    "id": "ff0f1355-e821-4178-9567-550dec27a373",
    "status": "delivered",
    'created': datetime.now(), 
    'order': [
        {
            "product": "cappuccino",
            "size": "medium",
            "quantity": 1
        }
    ]
}

@app.get("/orders")
def get_orders():
    return {'orders': orders}

@app.post("/orders", status_code=status.HTTP_201_CREATED)
def create_orders(order_details: CreateOrderSchema):
    return order

@app.put("/orders/{order_id}")
def update_order(order_id: UUID, order_details: CreateOrderSchema):
    order["order"][0]["quantity"] = randint(1,5)
    return order

@app.delete("/orders/{order_id}")
def delete_order(order_id: UUID):
    return Response(status_code=HTTPStatus.NO_CONTENT.value)

@app.post("orders/{order_id}/cancel")
def cancel_order(order_id: UUID):
    return order

@app.post("orders/{order_id}/pay")
def pay_order(order_id: UUID):
    return order