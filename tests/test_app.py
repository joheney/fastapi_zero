from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_restorna_html_deve_retornar_html():

    client = TestClient(app)
    response = client.get("/ola_mundo")

    status_da_response_e_OK = response.status_code == HTTPStatus.OK

    html_para_test = """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""

    html_da_response_e_igual_a_html_para_test = response.text == html_para_test

    assert status_da_response_e_OK
    assert html_da_response_e_igual_a_html_para_test
