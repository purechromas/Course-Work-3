import pytest

import utils


def test_get_post_all():
    """content type should be a list with JSON"""
    assert type(utils.get_posts_all()) == list, 'Type content is not list'


def test_get_comments_all():
    """content type should be a list with JSON"""
    assert type(utils.get_comments_all()) == list, 'Type content is not list'


def test_get_post_by_pk():
    """testing does function is returning write content"""
    assert utils.get_post_by_pk(1)['poster_name'] == "leo", "wrong content loaded"
    with pytest.raises(ValueError):
        utils.get_post_by_pk(10000)


def test_get_posts_by_user():
    """testing does function is returning write content"""
    with pytest.raises(ValueError):
        utils.get_posts_by_user('None_existed_name')
    assert len(utils.get_posts_by_user('larry')) == 2, "Returning not correct len"
    assert len(utils.get_posts_by_user('jlia')) == 0, "Returning not correct len"


def test_get_comments_by_post_id():
    """testing does function is returning write content"""
    with pytest.raises(ValueError):
        utils.get_comments_by_post_id(100)
    assert len(utils.get_comments_by_post_id(4)) == 4, "Retuning not correct len posts"
    assert len(utils.get_comments_by_post_id(8)) == 0, "Retuning not correct len posts"


def test_search_for_posts():
    """testing does function is returning write content"""
    assert len(utils.search_for_posts('кот')) == 4, "Retuning not correct len posts"
    assert len(utils.search_for_posts('Благовест')) == 0, "Retuning not correct len posts"
