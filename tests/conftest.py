from contextlib import contextmanager
from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session
<<<<<<< HEAD
from sqlalchemy.pool import StaticPool

from fast_zero.app import app
from fast_zero.database import get_session
from fast_zero.models import User, table_registry


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()
=======

from fastapi_zero.app import app
from fastapi_zero.models import table_registry


@pytest.fixture
def client():
    return TestClient(app)
>>>>>>> 916b82829813a56b53efc07a2fbca561446ec169


@pytest.fixture
def session():
<<<<<<< HEAD
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
=======
    engine = create_engine("sqlite:///:memory:")
>>>>>>> 916b82829813a56b53efc07a2fbca561446ec169
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)


@contextmanager
def _mock_db_time(*, model, time=datetime(2024, 1, 1)):
<<<<<<< HEAD
    def fake_time_handler(mapper, connection, target):
=======
    def fake_time_hook(mapper, connection, target):
>>>>>>> 916b82829813a56b53efc07a2fbca561446ec169
        if hasattr(target, "created_at"):
            target.created_at = time
        if hasattr(target, "updated_at"):
            target.updated_at = time

<<<<<<< HEAD
    event.listen(model, "before_insert", fake_time_handler)

    yield time

    event.remove(model, "before_insert", fake_time_handler)
=======
    event.listen(model, "before_insert", fake_time_hook)

    yield time

    event.remove(model, "before_insert", fake_time_hook)
>>>>>>> 916b82829813a56b53efc07a2fbca561446ec169


@pytest.fixture
def mock_db_time():
    return _mock_db_time
<<<<<<< HEAD


@pytest.fixture
def user(session: Session):
    user = User(username="Teste", email="teste@test.com", password="testtest")
    session.add(user)
    session.commit()
    session.refresh(user)

    return user
=======
>>>>>>> 916b82829813a56b53efc07a2fbca561446ec169
