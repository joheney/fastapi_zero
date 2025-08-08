from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Minha API foda.")

status_200_do_HTTPStatus = HTTPStatus.OK


@app.get(
    "/ola_mundo",
    status_code=status_200_do_HTTPStatus,
    response_class=HTMLResponse,
)
def retorna_html():
    return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""
