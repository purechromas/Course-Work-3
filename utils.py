import json


def get_posts_all():
    """Loading all posts"""
    try:
        with open('./data/posts.json', 'r', encoding='utf-8') as file:
            all_post = json.load(file)
        return all_post
    except OSError:
        print('File is not found or load')


def get_comments_all():
    """Loading all comments"""
    try:
        with open('./data/comments.json', 'r', encoding='utf-8') as file:
            all_comments = json.load(file)
        return all_comments
    except OSError:
        print('File is not found or load')


def get_post_by_pk(pk):
    """Return post by PK."""
    posts = get_posts_all()

    for post in posts:
        if post['pk'] == pk:
            return post
    raise ValueError('There is not that kind of post')


def get_posts_by_user(user_name):
    """Returns posts by USERNAME"""
    posts = get_posts_all()
    comments = get_comments_all()
    exist_user = []

    for comment in comments:
        if user_name.lower() == comment['commenter_name'].lower():
            exist_user.append(user_name)

    for post in posts:
        if user_name.lower() == post['poster_name'].lower():
            exist_user.append(user_name)

    if len(exist_user) == 0:
        raise ValueError("That kind of user doesn't exist")
    else:
        user_posts = []

        for user_post in posts:
            if user_name.lower() == user_post['poster_name'].lower():
                user_posts.append(user_post)
        return user_posts


def get_comments_by_post_id(post_id):
    """Returns all comments by POST ID."""
    posts = get_posts_all()
    comments = get_comments_all()
    post_comments = []
    check_post = []

    for post in posts:
        if post_id == post['pk']:
            check_post.append(post)

    for comment in comments:
        if post_id == comment['post_id']:
            post_comments.append(comment)

    if not len(check_post) == 1:
        raise ValueError("That kind of post doesn't exist")
    else:
        return post_comments


def search_for_posts(query):
    """Returns list of post with key word in CONTENT."""
    posts = get_posts_all()
    current_posts = []

    for post in posts:
        if query.lower() in post['content'].lower():
            current_posts.append(post)

    return current_posts


def get_posts_by_hashtag(hashtag):
    """Return list of posts with HASHTAGS"""
    posts = get_posts_all()
    hashtag_word = '#' + hashtag
    hashtag_posts = []

    for post in posts:
        if hashtag_word in post['content']:
            hashtag_posts.append(post)

    return hashtag_posts

