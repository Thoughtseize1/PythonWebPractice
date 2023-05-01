from faker import Faker
from mongoengine import connect
from models import User, Post

# Connect to MongoDB

# Create a Faker instance
fake = Faker("uk-ua")

# Generate fake users
users = []
for _ in range(10):
    user = User(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
    )
    users.append(user)

# Save users to the database
User.objects.insert(users)
