from http import HTTPStatus


def test_create_user(client, codigo_201_dado_enviado_e_criado_com_sucesso):
    response = client.post(
        "/users/",
        json={"username": "bob", "email": "bob@example.com", "password": "123"},
    )

    json_da_response = response.json()

    status_code_da_response = response.status_code

    assert status_code_da_response == codigo_201_dado_enviado_e_criado_com_sucesso
    assert json_da_response == {"username": "bob", "email": "bob@example.com", "id": 1}


def test_read_users(client, codigo_200_dado_solicitado_e_retornado_com_sucesso):
    response = client.get("/users/")

    status_code_da_response = response.status_code
    json_da_response = response.json()

    assert status_code_da_response == codigo_200_dado_solicitado_e_retornado_com_sucesso
    assert json_da_response == {
        "users": [{"username": "bob", "email": "bob@example.com", "id": 1}]
    }


def test_update_user(client, codigo_200_dado_atualizado_com_sucesso):
    response = client.put(
        "/users/666",
        json={
            "username": "bob",
            "email": "bob@example.com",
            "password": "mynewpassword",
        },
    )

    status_code_da_response = response.status_code
    json_da_response = response.json()

    assert status_code_da_response == HTTPStatus.NOT_FOUND
    assert json_da_response == {"detail": "User not found"}


def test_delete_user(client, codigo_200_dado_excluido_com_sucesso):
    response = client.delete("/users/111")

    status_code_da_response = response.status_code
    json_da_response = response.json()

    assert status_code_da_response == HTTPStatus.NOT_FOUND
    assert json_da_response == {"detail": "User not found"}


def test_get_user_should_return_not_found__exercicio(client):
    response = client.get("/users/666")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_get_user__exercicio(client):
    response = client.get("/users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "bob",
        "email": "bob@example.com",
        "id": 1,
    }
