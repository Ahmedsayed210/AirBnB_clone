import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_user_creation(self):
        user = User()
        self.assertIsInstance(user, User)

    def test_user_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_attributes_assignment(self):
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_user_to_dict(self):
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(user_dict['email'], "")
        self.assertEqual(user_dict['password'], "")
        self.assertEqual(user_dict['first_name'], "")
        self.assertEqual(user_dict['last_name'], "")
        self.assertEqual(user_dict['__class__'], 'User')
