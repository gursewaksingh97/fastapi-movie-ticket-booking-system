from pydantic import BaseModel

class BookingSystemSchema(BaseModel):
    booking_id:int
    customer_name:str
    movie_name:str
    seat_no:str

class UpdateBookings(BaseModel):
    customer_name:str
    movie_name:str
    seat_no:str

# response 
class BookingResponse(BaseModel):
    customer_name:str
    movie_name:str
    seat_no:str
    # this schema defines : what API should return to user