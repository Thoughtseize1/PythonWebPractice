from models import User, TextPost, ImagePost, Post, LinkPost

if __name__ == "__main__":
    all_posts = Post.objects
    print("---------ALL POST INFORMATION:-------------")
    for post in all_posts:
        print(post.to_mongo().to_dict())
    print("---------AUTHORS:-------------")
    for post in all_posts:
        print(post.author.first_name)
