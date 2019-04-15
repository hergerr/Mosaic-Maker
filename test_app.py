import unittest
import requests
from app import make_mosaic


class TestMakeMosaic(unittest.TestCase):
    def test_resolution_values(self):
        # Test negative resolution
        self.assertRaises(ValueError, make_mosaic, [], -100, -100)

    def test_wrong_image_url(self):
        # Test not existing or not available image
        self.assertRaises(requests.exceptions.ConnectionError, make_mosaic, ['http://dasdas.jpg'], 500, 500)

    def test_too_many_urls(self):
        # Test too large image list
        self.assertRaises(ValueError, make_mosaic, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 100, 100)
