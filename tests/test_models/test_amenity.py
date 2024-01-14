import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_default_values(self):
        amenity_instance = Amenity()
        self.assertEqual(amenity_instance.name, "")
        self.assertIsNone(amenity_instance.created_at)
        self.assertIsNone(amenity_instance.updated_at)

    def test_attributes(self):
        amenity_instance = Amenity()
        amenity_instance.name = "Swimming Pool"
        self.assertEqual(amenity_instance.name, "Swimming Pool")

    def test_to_dict(self):
        amenity_instance = Amenity()
        amenity_dict = amenity_instance.to_dict()
        self.assertIn("id", amenity_dict)
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)
        self.assertIn("name", amenity_dict)

    def test_str_representation(self):
        amenity_instance = Amenity(name="Gym")
        expected_str = "[Amenity] ({}) {}"\
            .format(amenity_instance.id, amenity_instance.__dict__)
        self.assertEqual(str(amenity_instance), expected_str)


if __name__ == '__main__':
    unittest.main()
