from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from pereval.models import *


# Create your tests here.
class PostAPITestCase(APITestCase):
    def setUp(self):
        self.user = Users.objects.create(
            email="qwerty@mail.ru",
            fam="Пупкин",
            name="Василий",
            otc="Иванович",
            phone="+7 555 55 55")
        self.coords = Coords.objects.create(
            latitude="45.3842",
            longitude="7.1525",
            height="1200")
        self.level = Level.objects.create(
            winter="1А",
            summer="1А",
            autumn="1А",
            spring="1А")
        self.pereval = Pereval.objects.create(
            beauty_title="пер.",
            title="Пхия",
            other_titles="Триев",
            connect="connect",
            user=self.user,
            coords=self.coords,
            level=self.level
        )
        Image.objects.create(data="<картинка1>", title="Седловина", pereval=self.pereval)
        Image.objects.create(data="<картинка>", title="Подъём", pereval=self.pereval)

    def test_submitData(self):
        url = reverse('submitData-list')
        data = {
            "beauty_title": "пер.",
            "title": "Пхия",
            "other_titles": "Триев",
            "connect": "connect",
            "add_time": "2021-09-22 13:18:13",
            "user": {"email": "qwerty@mail.ru",
                     "fam": "Иванов",
                     "name": "Иван",
                     "otc": "Иванович",
                     "phone": "+7 800 555 3535"},
            "coords": {
                "latitude": "45.3842",
                "longitude": "7.1525",
                "height": "1200"},
            "level": {"winter": "1А",
                      "summer": "1А",
                      "autumn": "1А",
                      "spring": "1А"},
            "images": [{"data": "<картинка1>", "title": "Седловина"}, {"data": "<картинка>", "title": "Подъём"}]
        }
        #проверка, что запрос отправлен
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #проверка, что объект сохранён в бд и не None
        new_pereval = Pereval.objects.filter(beauty_title="пер.", title="Пхия")
        self.assertIsNotNone(new_pereval)

        self.assertIn('status', response.data)
        self.assertIn('message', response.data)
        self.assertIn('id', response.data)
