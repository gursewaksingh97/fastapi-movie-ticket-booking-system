from sqlalchemy import Column, Integer, String

from database import Base

class BookingSystem(Base):
    __tablename__="moviebooking"
    booking_id=Column(Integer,primary_key=True)
    customer_name=Column(String)
    movie_name=Column(String)
    seat_no=Column(String)
    