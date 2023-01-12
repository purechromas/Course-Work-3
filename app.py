from flask import Flask, render_template, request, jsonify, redirect
import utils
import logging

app = Flask(__name__, static_url_path='/static')

# We are making new logger.
logger = logging.getLogger('one')
# Level = INFO
logger.setLevel(logging.INFO)
# Setting format of the logger.
logger_format = "%(asctime)s :: %(levelname)s :: %(message)s"
# Making a file handler(fh) and showing the way(file) where logger have to save all the info we need.
fh = logging.FileHandler(filename='logs/api.log')
# Adding format exactly on the file handler logger.
fh.setFormatter(logging.Formatter(logger_format))
# Adding file handler logger
logger.addHandler(fh)


# Return all post (Home Page)
@app.route('/')
def home_page():
    posts = utils.get_posts_all()
    return render_template('index.html', posts=posts)


# Return post by ID.
@app.route('/posts/<int:post_id>')
def post_page(post_id):
    post = utils.get_post_by_pk(post_id)
    comments = utils.get_comments_by_post_id(post_id)
    len_comments = len(comments)
    return render_template('post.html', post=post, comments=comments, len_comments=len_comments)


# Return all post with that kind of 'Search Content'.
@app.route('/search', methods=['GET', 'POST'])
def search_page():
    word = request.values.get('search')
    posts = utils.search_for_posts(f"{word}")
    return render_template('search.html', posts=posts)


# Return all user posts.
@app.route('/users/<username>')
def users_page(username):
    posts = utils.get_posts_by_user(f"{username}")
    return render_template('user-feed.html', posts=posts)


# Return all tags posts.
@app.route('/tag/<tagname>')
def tag_page(tagname):
    hashtag_posts = utils.get_posts_by_hashtag(tagname)
    return render_template('tag.html', hashtag_posts=hashtag_posts, tagname=tagname)


# Return all posts in JSON-DATA.
@app.route('/api/posts')
def api_posts():
    posts = utils.get_posts_all()
    logger.info('logger worked successfully - all posts')
    return jsonify(posts)


# Return post by ID in JSON-DATA.
@app.route('/api/posts/<int:post_id>')
def api_post(post_id):
    post = utils.get_post_by_pk(post_id)
    logger.info(f'logger worked successfully - post_id: {post_id}')
    return jsonify(post)


# If page is not found raise 404 errorhandler.
@app.errorhandler(404)
def error_404(error):
    return f"<h3>{error}</h3>"


# Uncovered errors will raise errorhandler.
@app.errorhandler(500)
def error_500(error):
    return f"<h3>{error}</h3>"


# ValueError will come if there is not that kind of user or post.
@app.errorhandler(ValueError)
def value_error(error):
    return f"<h3>({error})<h3>"


if __name__ == "__main__":
    app.run(debug=True)
