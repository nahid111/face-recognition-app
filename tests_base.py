from init import app, db
from models import User
from flask_testing import TestCase


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User("admin", "admin"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()