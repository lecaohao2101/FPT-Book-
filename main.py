from fastapi import FastAPI
import enum
from sqlalchemy import create_engine

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Double, Numeric, Enum
from sqlalchemy.orm import sessionmaker, declarative_base

# connection db
SQLALCHEMY_DATABASE_URL = "sqlite:///app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# open data
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Create table
class CategoryModel(Base):
    __tablename__ = "Category"

    id = Column(Integer, primary_key=True, autoincrement=True, )
    name = Column(String, nullable=False)


class AuthorModel(Base):
    __tablename__ = "Author"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)


class RoleEnum(enum.Enum):
    ADMIN = 'ADMIN'
    CUSTOMER = 'CUSTOMER'
    OWNER = 'OWNER'


class RoleModel(Base):
    __tablename__ = "Role"

    id = Column(Integer, primary_key=True, autoincrement=True)
    # name = Column(String, nullable=False)
    name = Column(Enum(RoleEnum), nullable=False)


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String(length=8), nullable=False)
    role_id = Column(Integer, ForeignKey("Role.id"), nullable=False)


class AddressModel(Base):
    __tablename__ = "Address"
    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String(length=56), nullable=False)
    city = Column(String(length=21), nullable=False)
    district = Column(String(length=15), nullable=False)
    ward = Column(String(length=15) , nullable=False)
    street = Column(String(length=15) , nullable=False)
    numbers_home = Column(String(length=15), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)


class OrderModel(Base):
    __tablename__ = "Order"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    create_date = Column(DateTime, nullable=False)
    Total = Column(Double ,nullable=False)


class StoreModel(Base):
    __tablename__ = "Store"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    name = Column(String, nullable=False)


class BookModel(Base):
    __tablename__ = "Book"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50), nullable=False)
    description = Column(String(length=300), nullable=False)
    price = Column(Numeric, nullable=False)
    stock = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey("Category.id"), nullable=False)
    store_id = Column(Integer, ForeignKey("Store.id"), nullable=False)
    author_id = Column(Integer, ForeignKey("Author.id"), nullable=False)


class OrderItemModel(Base):
    __tablename__ = "Order_Item"
    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey("Book.id"), nullable=False)
    order_id = Column(Integer, ForeignKey("Order.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    subtotal = Column(Double, nullable=False)





app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
