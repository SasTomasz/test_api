import requests
import pytest

base_url = "http://localhost:3000/"
r = requests.get(base_url)
status_code = r.status_code
print(r.status_code)


def test_correct_status_code():
    posts = base_url + "posts"
    get_posts = requests.get(posts)
    print(get_posts.text)
    assert get_posts.status_code == 200


def test_correct_add_post():
    pass
