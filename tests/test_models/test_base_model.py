#!/usr/bin/python3
from models.base_model import BaseModel
import unittest

class Test_BaseModel(unittest.TestCase):

    def test_init(self):
        modelly = BaseModel()
        self.assertIsNotNone(modelly.id)
        self.assertIsNotNone(modelly.created_at)
        self.assertIsNotNone(modelly.updated_at)


    def test_save(self):
        modelly = BaseModel()
        initiali_up_at = modelly.updated_at
        current_up_at = modelly.save()

        self.assertNotEqual(initiali_up_at, current_up_at)


    def test_to_dict(self):
        modelly = BaseModel()
        modelly_to_dict = modelly.to_dict()
        self.assertIsInstance(modelly_to_dict, dict)

        self.assertEqual(modelly_to_dict["__class__"], "BaseModel")
        self.assertEqual(modelly_to_dict["id"], modelly.id)
        self.assertEqual(modelly_to_dict["created_at"], modelly.created_at.isoformat())
        self.assertEqual(modelly_to_dict["updated_at"], modelly.created_at.isoformat())



    def test_str(self):
        modelly = BaseModel()
        self.assertTrue(str(modelly).startswith('[BaseModel]'))

        self.assertIn(modelly.id, str(modelly))

        self.assertIn(str(modelly.__dict__), str(modelly))

if __name__ == "__main__":
    unittest.main()