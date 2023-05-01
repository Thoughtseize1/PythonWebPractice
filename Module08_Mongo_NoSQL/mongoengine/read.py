from models import User, TextPost, ImagePost, Post, LinkPost
from bson.objectid import ObjectId
from colors import *


def find_post_by_id(_id):
    try:
        post = Post.objects.get(id=ObjectId(_id))
        print(f"{CYAN_COLOR} FOUND POST BY ID: {RESET_COLOR}")
        print(post.to_mongo().to_dict())
        return post
    except Post.DoesNotExist:
        print(f"No post with _id={_id} found.")
        return None


def find_user_by_id(_id):
    try:
        user = User.objects.get(id=ObjectId(_id))
        print(f"{CYAN_COLOR}FOUND USER BY ID:{RESET_COLOR}")
        print(user.to_mongo().to_dict())
        return user
    except User.DoesNotExist:
        print(f"No user with _id={_id} found.")
        return None


if __name__ == "__main__":
    all_posts = Post.objects()
    print("---------ALL POST INFORMATION:-------------")
    for post in all_posts:
        print(post.to_mongo().to_dict())
    print("---------AUTHORS:-------------")
    for post in all_posts:
        print(post.author.first_name)

    # ?GETTING ALL USERS
    print("---------ALL USERS:-------------")
    all_users = User.objects()
    for user in all_users:
        print(f"{user.first_name} {user.last_name}. Email: {user.email}")

    print(f"{GREEN_COLOR}---------WORK WITH Specific user:-------------{RESET_COLOR}")
    find_post_by_id("644ec8fbcb81357d2551576c")
    find_user_by_id("644ec8facb81357d2551576a")
