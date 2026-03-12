from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, Json
from datetime import date

from starlette.responses import JSONResponse

app = FastAPI()

bookings = []

class Booking(BaseModel):
    customer_name : str
    customer_phone : str
    customer_email : str
    room_number : int
    reservation_description : str
    reservation_date : date

@app.get("/booking",response_model=List[Booking],status_code=200)
def get_reservation():
    return bookings

@app.post("/booking",response_model=List[Booking],status_code=200)
def create_reservation(booking: Booking):

    if booking.room_number < 1 or booking.room_number > 9 :
        return JSONResponse(
            status_code=400,
            content={"message": "Room number must be between 1 and 9"}
        )

    for existing_booking in bookings:
        if(
            existing_booking.room_number == booking.room_number
            and existing_booking.reservation_date == booking.reservation_date
        ):
            return JSONResponse(
                status_code=409,
                content={"message": "This room is not available for this date"}
            )
    bookings.append(booking)
    return bookings

