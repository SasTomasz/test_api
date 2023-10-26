from http import HTTPStatus
import requests


# json_auth = admin_auth.model_dump_json()


# def test_auth(admin_auth, env_settings):
def test_auth(admin_auth, env_settings):
    r = requests.post(
        url=f"{env_settings.base_url}auth",
        json={
            "username": admin_auth.username,
            "password": admin_auth.password
        }
    )

    print(f"username from admin_auth: {admin_auth.username}")
    print(f"password from admin_auth: {admin_auth.password}")
    print(f"content = {r.content}")
    print(f"json = {r.json()}")

    assert HTTPStatus.OK == r.status_code
    # assert "token" in r.json()
    # r = requests.post('https://restful-booker.herokuapp.com/auth')
    # print(r.status_code)

# def test_auth_2(admin_auth):
#     r = requests.post(
#         "https://restful-booker.herokuapp.com/auth",
#         json=admin_auth
#     )
#
#     print(f"content = {r.content}")
#     print(f"json = {r.json()}")
