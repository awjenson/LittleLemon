from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title="Greek Salad", price=12.99, inventory=50)
        Menu.objects.create(title="Bruschetta", price=8.50, inventory=30)
        Menu.objects.create(title="Lemon Dessert", price=6.75, inventory=20)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)