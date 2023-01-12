from app import app


def test_api_post():
    """testing the content"""
    response = app.test_client().get('/api/posts/1')
    assert response.json.get('poster_name') == "leo", "Wrong name"


def test_api_posts():
    """testing the status code"""
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200, 'Wrong status'
