from sqlalchemy import create_engine
#create_engine - responsible -establishing connection b/w Python-database
from sqlalchemy.orm import sessionmaker
# is used to create sessions that helps us talk to the database and perform CRUD operations
from sqlalchemy.ext.declarative import declarative_base 
#helps create database tables using Python Classes instead of Writing SQL manually

DATABSE_URL="postgresql://postgres:1234@localhost/Booking System"
# it is a connection string used to conect Python and PostgreSQL Database
# databse rtype://postgreSQL username:password@local machine/database name

engine =create_engine(DATABSE_URL)
SessionLocal=sessionmaker(bind=engine)

Base = declarative_base()