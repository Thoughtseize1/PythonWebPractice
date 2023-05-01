from models import User, TextPost, ImagePost, Post, LinkPost


if __name__ == "__main__":
    # ! Got ALL users with name Ross
    all_rosses = User.objects(first_name="Ross")
    # ! We know that we have only 1 Ross!
    print(all_rosses[0].email)
    # ? Changing last name:
    all_rosses.update(last_name="Lawley")
    # ? Print new last name WITH NEW DATA
    for user in all_rosses:
        print(user.last_name)

    # ! Get only one User object by using the first() method on the queryset. This will return the first matching user object."""
    new_one_ross = User.objects(first_name="Ross").first()

    if new_one_ross:
        # Assign a new lastname BUT without saving in database!
        new_one_ross.last_name = "Barashek"
        # Now, we save new last_name in database!
        new_one_ross.save()
        print(new_one_ross.last_name)
    else:
        print("No users found.")
