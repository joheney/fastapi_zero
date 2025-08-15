from dataclasses import asdict

<<<<<<< HEAD
from sqlalchemy import select

from fast_zero.models import User
=======
from sqlalchemy import Select

from fastapi_zero.models import User
>>>>>>> 916b82829813a56b53efc07a2fbca561446ec169


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(username='alice', password='secret', email='teste@test')
        session.add(new_user)
        session.commit()

<<<<<<< HEAD
    user = session.scalar(select(User).where(User.username == 'alice'))
=======
    user = session.scalar(Select(User).where(User.username == 'alice'))
>>>>>>> 916b82829813a56b53efc07a2fbca561446ec169

    assert asdict(user) == {
        'id': 1,
        'username': 'alice',
        'password': 'secret',
        'email': 'teste@test',
        'created_at': time,
<<<<<<< HEAD
        'updated_at': time,  # Exercício
=======
        'updated_at': time,
>>>>>>> 916b82829813a56b53efc07a2fbca561446ec169
    }
