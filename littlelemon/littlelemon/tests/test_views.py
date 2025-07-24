from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer  # Adjust name if needed

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create some test Menu objects
        self.item1 = Menu.objects.create(title="Burger", price=5.99, inventory=10)
        self.item2 = Menu.objects.create(title="Pizza", price=7.99, inventory=15)
        self.item3 = Menu.objects.create(title="Salad", price=4.99, inventory=8)

    def test_getall(self):
        # Hit the API endpoint for menu items
        response = self.client.get(reverse('menu-list'))  # Adjust name if needed

        # Get all Menu items and serialize them
        menu_items = Menu.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)

        # Assert response status and data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    