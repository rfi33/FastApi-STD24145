from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
app = FastAPI()

reservation = []

class Reservation(BaseModel):
    customer_name : str
    customer_phone : str
    customer_email : str
    room_number : str
    reservation_description : str
    reservation_date : date

@app.get("/booking")
def get_reservation():
    return {
        "message": "List of reservation",
        "data": reservation
    }

