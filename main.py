import requests
import pytest

base_url = "http://localhost:3000/"
r = requests.get(base_url)
status_code = r.status_code
print(r.status_code)


def test_correct_status_code():
    assert status_code == 200
