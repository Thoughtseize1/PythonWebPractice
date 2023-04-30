from models import User, TextPost, ImagePost, Post, LinkPost

if __name__ == "__main__":
    ross = User(email="ross@example.com", first_name="Ross", last_name="Lawley").save()
    john = User(email="john@example.com", first_name="John", last_name="Lawley").save()
    nikita = User(email="nikita@example.com").save()
    post1 = TextPost(title="Fun with MongoEngine", author=john)
    post1.content = "Took a look at MongoEngine today, looks pretty cool."
    post1.tags = ["mongodb", "mongoengine"]
    post1.save()

    post2 = LinkPost(title="MongoEngine Documentation", author=ross)
    post2.link_url = "http://docs.mongoengine.com/"
    post2.tags = ["mongoengine"]
    post2.save()
