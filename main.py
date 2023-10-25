import requests

r = requests.post(
    url="https://restful-booker.herokuapp.com/auth",
    json={
        "username": "username",
        "password": "password123"
    }
)

print(r.status_code)
