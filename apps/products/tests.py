from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase

from apps.products.models import Product
from apps.users.models import User


class ProductViewSetTest(APITestCase):
    fixtures = [
        "apps/fixtures/users.json",
        "apps/fixtures/products.json",
        "apps/fixtures/wish_list.json",
    ]

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get(pk=1)
        self.superuser = User.objects.get(pk=2)
        self.product_1 = Product.objects.get(pk=1)
        self.product_2 = Product.objects.get(pk=2)

    def test_list_products_authenticated(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(reverse("products-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("results")[0].get("added_to_wish_list"), 1)
        self.assertEqual(len(response.json().get("results")), 2)

    def test_list_products_unauthenticated(self):
        response = self.client.get(reverse("products-list"))
        self.assertEqual(response.status_code, 401)

    def test_retrieve_product(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(reverse("products-detail", args=(1,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], self.product_1.name)

    def test_superuser_create_product(self):
        data = {"name": "New Product", "price": "25.00", "description": "New Description"}
        self.client.force_authenticate(self.superuser)
        response = self.client.post(reverse("products-list"), data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Product.objects.count(), 3)

    def test_user_create_product(self):
        data = {"name": "New Product", "price": "25.00", "description": "New Description"}
        self.client.force_authenticate(self.user)
        response = self.client.post(reverse("products-list"), data=data)
        self.assertEqual(response.status_code, 403)
