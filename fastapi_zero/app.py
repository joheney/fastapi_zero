from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from fastapi_zero.shcemas import UserDb, UserList, UserPublic, UserSchema

status_created_201 = HTTPStatus.CREATED
status_200_ok = HTTPStatus.OK
status_404_NOT_FOUND = HTTPStatus.NOT_FOUND


app = FastAPI(title='Minha API foda')

database = []


def gen_next_id():
    return len(database) + 1


@app.post('/users/', status_code=status_created_201, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDb(id=gen_next_id(), **user.model_dump())
    database.append(user_with_id)
    return user_with_id


@app.get('/users/', status_code=status_200_ok, response_model=UserList)
def read_users():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=status_404_NOT_FOUND, detail='User not found')
    user_with_id = UserDb(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id
    return user_with_id


@app.delete('/users/{user_id}', status_code=status_200_ok, response_model=UserPublic)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=status_404_NOT_FOUND, detail='User not found')

    return database.pop(user_id - 1)


@app.get('/users/{user_id}', response_model=UserPublic)
def read_user__exercicio(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='User not found')
    return database[user_id - 1]
