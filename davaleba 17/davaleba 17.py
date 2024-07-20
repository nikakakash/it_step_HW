class User:
    def __init__(self, username):
        self.username = username
        self.posts = []
        self.friends = set()

    def create_post(self, content):
        post = Post(content, self)
        self.posts.append(post)
        return post

    def add_friend(self, friend):
        self.friends.add(friend)
        friend.friends.add(self)

    def comment_on_post(self, post, content):
        comment = Comment(content, self)
        post.add_comment(comment)
        return comment

    def like_post(self, post):
        post.add_like(self)

    def __repr__(self):
        return f"User({self.username})"


class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.comments = []
        self.likes = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def add_like(self, user):
        self.likes.append(user)

    def __repr__(self):
        return f"Post(content={self.content}, author={self.author.username}, comments={self.comments}, likes={len(self.likes)})"


class Comment:
    def __init__(self, content, author):
        self.content = content
        self.author = author

    def __repr__(self):
        return f"Comment(content={self.content}, author={self.author.username})"

# Create users
user1 = User("User1")
user2 = User("User2")

# Make them friends
user1.add_friend(user2)

# User1 creates a post
post1 = user1.create_post("This is User1's first post.")

# User2 comments on User1's post
comment1 = user2.comment_on_post(post1, "Nice post, User1!")

# User1 likes User2's comment (assuming likes are on posts)
user1.like_post(post1)

# User1 creates another post
post2 = user1.create_post("This is User1's second post.")

# User2 likes User1's second post
user2.like_post(post2)

# Display the posts and interactions
print(post1)
print(post2)