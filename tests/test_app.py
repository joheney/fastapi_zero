def test_create_user(client, codigo_201_dado_enviado_e_criado_com_sucesso):
    response = client.post(
        '/users/',
        json={'username': 'jhon', 'email': 'jhon@gmail.com', 'password': '123'},
    )

    json_da_response = response.json()

    status_code_da_response = response.status_code

    assert status_code_da_response == codigo_201_dado_enviado_e_criado_com_sucesso
    assert json_da_response == {'username': 'jhon', 'email': 'jhon@gmail.com', 'id': 1}


def test_read_users(client, codigo_200_dado_solicitado_e_retornado_com_sucesso):
    response = client.get('/users/')

    status_code_da_response = response.status_code
    json_da_response = response.json()

    assert status_code_da_response == codigo_200_dado_solicitado_e_retornado_com_sucesso
    assert json_da_response == {
        'users': [{'username': 'jhon', 'email': 'jhon@gmail.com', 'id': 1}]
    }


def test_update_user(client, codigo_200_dado_atualizado_com_sucesso):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    status_code_da_response = response.status_code
    json_da_response = response.json()

    assert status_code_da_response == codigo_200_dado_atualizado_com_sucesso
    assert json_da_response == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_delete_user(client, codigo_200_dado_excluido_com_sucesso):
    response = client.delete('/users/1')

    status_code_da_response = response.status_code
    json_da_response = response.json()

    assert json_da_response == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }
    assert status_code_da_response == codigo_200_dado_excluido_com_sucesso
    