from unittest import TestCase
import unittest
import json
from .redis_connect import redis_instance
from .views import UploadLinks
import requests


class TestRedisCache(TestCase):

    def test_upload_links(self):
        data = {
            "links": [
                "https://www.youtube.com/watch?app=desktop&v=qizLT_p6z4g",
                "https://drive.google.com/file/d/1DU2-MSCNN-FzCa8ksB3rx2GQy23LSt5T/view",
                "https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/"
            ]
        }
        data_json = json.dumps(data)
        response = requests.post(url='http://127.0.0.1:8000/api/v1/visited_links',
                                 data=data_json)
        keys = redis_instance.scan()[1]
        print(redis_instance.mget(*keys))
        self.assertEqual(response.json(), {'status': 'ok'})


if __name__ == '__main__':
    unittest.main()
# Create your tests here.
