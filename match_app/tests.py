import json

from django.test import tag
from rest_framework.test import APITestCase

from test_task.settings import BASE_DIR


class HumanTestCase(APITestCase):
    BASE_URL = '/api/match/'
    HUMAN_URL = '/api/human/'
    DEFAULT_DATA = {
            "first_name": "default_first_name",
            "second_name": "default_second_name",
            "age": "10",
            "gender": "M"
    }

    def post_default(self, avatar=None, **kwargs):
        with open(BASE_DIR + '/static/avatar_sample.jpg', 'rb') as f:
            data = self.DEFAULT_DATA.copy()
            data.update(kwargs)
            payload = {
                'avatar':  avatar or f,
                'data': json.dumps(data)
            }
            response = self.client.post(
                self.HUMAN_URL,
                data=payload,
                format='multipart'
            )
            return response

    def setUp(self):
        self.first = self.post_default(first_name='first').data
        self.second = self.post_default(first_name='second').data

    @tag('skip_setup')
    def test_post(self):
        resp = self.post_default()
        self.assertEqual(resp.status_code, 201)
        resp = self.client.post(self.BASE_URL, data=self.DEFAULT_DATA)
        self.assertEqual(resp.status_code, 405)

    def test_get(self):
        resp = self.client.get(self.BASE_URL + '{}/'.format(self.first['id']))
        self.assertEqual(resp.status_code, 200)
        expected = {
            "first_name": "first",
            "second_name": "default_second_name",
            "age": "10",
            "gender": "Male",
            "human": self.first
        }
        self.assertEqual(resp.json(), expected)

    def test_put(self):
        data = self.DEFAULT_DATA.copy()
        data.update({
            "first_name": 'Non_Default_fn',
            "age": '1235',
            "gender": 'F'
        })
        with open(BASE_DIR + '/static/avatar_sample.jpg', 'rb') as avatar:
            payload = {
                'avatar': avatar,
                'data': json.dumps(
                    data
                )
            }
            resp = self.client.put(
                self.HUMAN_URL + '{}/'.format(self.first['id']),
                data=payload,
                format='multipart'
            )
        self.first.update({
            "first_name": 'Non_Default_fn',
            "age": '1235',
            "gender": 'Female',
        })
        self.first.pop('avatar')
        expected = {
            "first_name": "first",
            "second_name": "default_second_name",
            "age": "10",
            "gender": "Male",
            "human": self.first
        }
        expected.update({
            "first_name": 'Non_Default_fn',
            "age": '1235',
            "gender": 'Female',
        })
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(self.BASE_URL + '{}/'.format(self.first['id']))
        json_ = resp.json()
        json_['human'].pop('avatar')
        self.assertEqual(expected, json_)

    def test_delete(self):
        resp = self.client.delete(self.HUMAN_URL + '{}/'.format(self.first['id']))
        self.assertEqual(resp.status_code, 204)
        resp = self.client.get(self.BASE_URL + '{}/'.format(self.first['id']))
        self.assertEqual(resp.status_code, 404)
        resp = self.client.delete(self.BASE_URL + '{}/'.format(self.first['id']))
        self.assertEqual(resp.status_code, 405)

    def test_list(self):
        resp = self.client.get(self.BASE_URL)
        self.assertEqual(resp.status_code, 200)
        f_resp = self.client.get(self.BASE_URL+ '{}/'.format(self.first['id']))
        s_resp = self.client.get(self.BASE_URL+ '{}/'.format(self.second['id']))
        expected = [f_resp.json(), s_resp.json()]
        self.assertEqual(resp.data['results'], expected)