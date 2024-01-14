import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_default_values(self):
        city_instance = City()
        self.assertEqual(city_instance.state_id, "")
        self.assertEqual(city_instance.name, "")
        self.assertIsNone(city_instance.created_at)
        self.assertIsNone(city_instance.updated_at)

    def test_attributes(self):
        city_instance = City()
        city_instance.state_id = "CA"
        city_instance.name = "San Francisco"
        self.assertEqual(city_instance.state_id, "CA")
        self.assertEqual(city_instance.name, "San Francisco")

    def test_to_dict(self):
        city_instance = City()
        city_dict = city_instance.to_dict()
        self.assertIn("id", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertIn("state_id", city_dict)
        self.assertIn("name", city_dict)

    def test_str_representation(self):
        city_instance = City(state_id="NY", name="New York")
        expected_str = "[City] ({}) {}"\
            .format(city_instance.id, city_instance.__dict__)
        self.assertEqual(str(city_instance), expected_str)


if __name__ == '__main__':
    unittest.main()
