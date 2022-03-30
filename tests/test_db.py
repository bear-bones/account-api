from pprint import pprint

from app import db
from pymongo.errors import InvalidOperation
import pytest

def test_db_connect(app):
    with app.app_context():
        client = db.connect()
        assert client.server_info() is not None
        assert client is db.connect()

    with pytest.raises(InvalidOperation) as error:
        _uid = client.user_accounts.users.insert_one({'account_num': 48229381, 'first_name': 'Rudy', 'last_name': 'Tomjanovich'}).inserted_id

    assert str(error.value) == 'Cannot use MongoClient after close'
