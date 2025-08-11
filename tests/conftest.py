from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from fastapi_zero.app import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def codigo_200_dado_solicitado_e_retornado_com_sucesso():
    return HTTPStatus.OK


@pytest.fixture
def codigo_200_dado_atualizado_com_sucesso():
    return HTTPStatus.OK


@pytest.fixture
def codigo_200_dado_excluido_com_sucesso():
    return HTTPStatus.OK


@pytest.fixture
def codigo_201_dado_enviado_e_criado_com_sucesso():
    return HTTPStatus.CREATED
