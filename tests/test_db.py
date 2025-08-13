from dataclasses import asdict

from sqlalchemy import Select

from fastapi_zero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as (time, updated_at):
        new_user = User(username='alice', password='secret', email='teste@test')
        session.add(new_user)
        session.commit()

    user = session.scalar(Select(User).where(User.username == 'alice'))

    assert asdict(user) == {
        'id': 1,
        'username': 'alice',
        'password': 'secret',
        'email': 'teste@test',
        'created_at': time,
        'updated_at': updated_at,
    }
