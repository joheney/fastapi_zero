from contextlib import contextmanager
from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session

from fastapi_zero.app import app
from fastapi_zero.models import table_registry


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)


@contextmanager
def _mock_db_time(*, model, time=datetime(2024, 1, 1), updated_at=datetime(2024, 1, 2)):
    def fake_time_hook(mapper, connection, target):
        if hasattr(target, 'created_at') and hasattr(target, 'updated_at'):
            target.created_at = time
            target.updated_at = updated_at

    event.listen(model, 'before_insert', fake_time_hook)

    yield time, updated_at

    event.remove(model, 'before_insert', fake_time_hook)


@pytest.fixture
def mock_db_time():
    return _mock_db_time
