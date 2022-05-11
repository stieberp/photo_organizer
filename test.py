import unittest

from main import get_date


class TestPhotoDate(unittest.TestCase):
    def test_date_jpg(self):
        path = "test_photos/image_with_date.jpg"
        result = get_date(path)
        self.assertEqual("2022-05", result)

    def test_no_date_jpg(self):
        path = "test_photos/image.jpg"
        result = get_date(path)
        self.assertEqual(None, result)


if __name__ == "__main__":
    unittest.main()
