import os
import random
from faker import Faker

fake = Faker("uk-ua")
from models import User, TextPost, ImagePost, Post, LinkPost

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LINKS_FILE = os.path.join(BASE_DIR, "links.txt")

# Open the file for reading
with open(LINKS_FILE, "r") as f:
    lines = f.readlines()

# Choose 5 random lines


# Generate fake posts with links
posts = []
for _ in range(User.objects().count() + 1):
    post = TextPost(
        title=fake.sentence(),
        content=random.choice(lines),
        author=random.choice(User.objects()),
        tags=[fake.word() for _ in range(3)],
    )
    posts.append(post)

# Save posts to the database
TextPost.objects.insert(posts)
