import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_default_values(self):
        review_instance = Review()
        self.assertEqual(review_instance.place_id, "")
        self.assertEqual(review_instance.user_id, "")
        self.assertEqual(review_instance.text, "")
        self.assertIsNone(review_instance.created_at)
        self.assertIsNone(review_instance.updated_at)

    def test_attributes(self):
        review_instance = Review()
        review_instance.place_id = "12345"
        review_instance.user_id = "user_123"
        review_instance.text = "This is a great place!"
        self.assertEqual(review_instance.place_id, "12345")
        self.assertEqual(review_instance.user_id, "user_123")
        self.assertEqual(review_instance.text, "This is a great place!")

    def test_to_dict(self):
        review_instance = Review()
        review_dict = review_instance.to_dict()
        self.assertIn("id", review_dict)
        self.assertIn("created_at", review_dict)
        self.assertIn("updated_at", review_dict)
        self.assertIn("place_id", review_dict)
        self.assertIn("user_id", review_dict)
        self.assertIn("text", review_dict)

    def test_str_representation(self):
        review_instance = Review(place_id="98765",
                                 user_id="user_456", text="Nice experience!")
        expected_str = "[Review] ({}) {}"\
            .format(review_instance.id, review_instance.__dict__)
        self.assertEqual(str(review_instance), expected_str)


if __name__ == '__main__':
    unittest.main()
