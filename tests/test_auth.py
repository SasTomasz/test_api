from http import HTTPStatus
import requests


# json_auth = admin_auth.model_dump_json()


def test_auth(admin_auth):
    r = requests.post(
        url="https://restful-booker.herokuapp.com/auth",
        json={
            "username": admin_auth.password,
            "password": admin_auth.password
        }
    )

    print(f"content = {r.content}")
    print(f"json = {r.json()}")

    assert HTTPStatus.OK == r.status_code

# def test_auth_2(admin_auth):
#     r = requests.post(
#         "https://restful-booker.herokuapp.com/auth",
#         json=admin_auth
#     )
#
#     print(f"content = {r.content}")
#     print(f"json = {r.json()}")
