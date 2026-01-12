# Exercise 1: Create a basic BaseModel

from pydantic import BaseModel, ValidationError, Field, ConfigDict
from datetime import datetime
import json

# Solution 1: Create a basic BaseModel
class User(BaseModel):
    id: int
    name: str
    email: str | None = None
user = User(
    id=1,
    name="John Doe",
    email="john.doe@example.com"
)
print("Exercise 1: User model instance:")
print(user)
# Solution 2: Validate data with model_validate()


class Product(BaseModel):
    name: str
    price: float
    

valid_data = {
    "name": "Laptop",
    "price": 1000.00
}
try:
    print("Exercise 2: Validating data with model_validate()...")
    product_a = Product.model_validate(valid_data)
    print(product_a)
except ValidationError as e:
    print(e)

# Solution 3: Validate data from JSON with model_validate_json()


class Event(BaseModel):
    title: str
    date: datetime
    

json_data = """{
    "title": "PyCon",
    "date": "2026-01-11"
}"""

try:
    print("Exercise 3: Validating JSON data with model_validate_json()...")
    event = Event.model_validate_json(json_data)
    print(event)
except ValidationError as e:
    print(e)

# Solution 4: Serialize model to dictionary with model_dump()

class Book(BaseModel):
    title: str
    author: str
    publication_year: datetime

book = Book(
    title="The Great Gatsby",
    author="F. Scott Fitzgerald",
    publication_year=datetime(1925, 1, 1)
)
print("Exercise 4: Serializing model to dictionary with model_dump()...")
book_dict = book.model_dump(mode='json')
print(json.dumps(book_dict, indent=4))

# Solution 5: Serialize model to JSON with model_dump_json()

print("Exercise 5: Serializing model to JSON with model_dump_json()...")
json_book = book.model_dump_json(indent=4)
print(json_book)

# Solution 6: Generate JSON Schema with model_json_schema()

class UserConfiguration(BaseModel):
    id: int
    name: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
    is_premium: bool | None = None
    tags: list[str] = []

print("Exercise 6: Generating JSON Schema with model_json_schema()...")
json_schema = UserConfiguration.model_json_schema()
print(json.dumps(json_schema, indent=4))
# TODO: Discover how to use the json schema in python


# Solution 7: Access model fields with model_fields

class Employee(BaseModel):
    id: int = Field(
        description="The id of the employee",
        alias="_id",
        examples=[1, 2, 3],
        default=1,
        
    )
    name: str = Field(
        description="The name of the employee",
        alias="full_name",
        examples=["John Doe", "Jane Smith"],
        validate_default=True,
    )
    age: int = Field(
        description="The age of the employee",
        alias="age",
        examples=[30, 35],
        validate_default=False,
        gt=18,
        lt=65
    )
    email: str = Field(
        description="The email of the employee",
        alias="email",
        examples=["john.doe@example.com", "jane.smith@example.com"],
        validate_default=True
    )


print("Exercise 7: Accessing model fields with model_fields...")

employee = Employee(
    full_name="John Doe",
    age=30,
    email="john.doe@example.com"
)
print(employee)
print(Employee.model_fields)

# Solution 8: Configure model with model_config


class Client(BaseModel):
    name: str = Field(alias="full_name")
    age: int
    email: str
    model_config = ConfigDict(
        extra="allow",
        validate_by_name=True,
        strict=True
    )

print("Exercise 8: Configure model with model_config...")
client = Client(
    full_name="John Doe",
    age=30,
    email="john.doe@example.com"
)
print(client)


# Solution 9: Configure model with model_config

class Order(BaseModel):
    id: int
    items: list[str]
    total_price: float = Field(gt=0)

print("Exercise 9: Configure model with model_config...")

order_a = Order.model_construct(
    id=1,
    items=["Item 1", "Item 2", "Item 3"],
    total_price=100.00
)
order_b = Order.model_construct(
    id=1,
    items=["Item 1", "Item 2", "Item 3"],
    total_price=-100.00,
    send_to="john.doe@example.com"
)
print(order_a)
print(order_b)

# Solution 10: Copy model with model_copy()

class User(BaseModel):
    name: str
    age: int
    email: str

user = User(
    name="John Doe",
    age=30,
    email="john.doe@example.com"
)
print("Exercise 10: Copy model with model_copy()...")
print(user)
copy_user = user.model_copy(update={"age": 31})
print(copy_user)


