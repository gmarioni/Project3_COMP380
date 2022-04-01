import db

def test_connection():
    db_test = db.Database()
    db_test.create_connection()
    assert db_test.is_connected() is True
