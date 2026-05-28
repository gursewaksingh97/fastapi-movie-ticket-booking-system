from fastapi import FastAPI,status
from database import engine,SessionLocal
from models import BookingSystem,Base
from schemas import BookingSystemSchema,UpdateBookings,BookingResponse
app=FastAPI()

Base.metadata.create_all(bind=engine)
session = SessionLocal()

@app.get("/")
def home():
    return {'message': "Welcome To Movie Booking Management System"} 

@app.get("/bookings",response_model=list[BookingResponse])
def get_booking():
    bookings=session.query(BookingSystem).all()
    return bookings


@app.post("/add_booking",status_code=status.HTTP_201_CREATED)
def add_booking(book:BookingSystemSchema):
    booking=BookingSystem(booking_id=book.booking_id,customer_name=book.customer_name,movie_name=book.movie_name,seat_no=book.seat_no)
    session.add(booking)
    session.commit()
    return {"Message":"Booking Placed...."}
    
@app.put("/bookings/update/{booking_id}",status_code=status.HTTP_200_OK)
def update_booking(booking_id:int, book:UpdateBookings):
    booking=session.query(BookingSystem).filter(BookingSystem.booking_id==booking_id).first()
    
    booking.customer_name= book.customer_name
    # changes old name
    booking.movie_name= book.movie_name
    session.commit()
    return {'message':"Booking Details Updated Successful...."}


@app.delete("/bookings/delete/{booking_id}",status_code=status.HTTP_200_OK)
def delete_booking(booking_id:int):
    booking=session.query(BookingSystem).filter(BookingSystem.booking_id==booking_id).first()
    session.delete(booking)
    session.commit()
    return{'Message':"Booking Deleted Successfully"}