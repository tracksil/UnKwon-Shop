from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase
from apps.users.models import User
from apps.products.models import Product
from apps.wish_list.models import WishList, WishListProducts
from rest_framework import status


class WishListViewSetTest(APITestCase):
    fixtures = [
        "apps/fixtures/users.json",
        "apps/fixtures/products.json",
        "apps/fixtures/wish_list.json",
    ]

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get(pk=1)
        self.wishlist_1 = WishList.objects.get(pk=1)
        self.wishlist_2 = WishList.objects.get(pk=2)

    def test_list_wishlists_authenticated(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(reverse("wish_list-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json().get("results")), 1)

    def test_list_wishlists_unauthenticated(self):
        response = self.client.get(reverse("wish_list-list"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_wishlist_authenticated(self):
        self.client.force_authenticate(self.user)
        data = {"name": "New Wishlist"}
        response = self.client.post(reverse("wish_list-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(WishList.objects.count(), 3)
        self.assertEqual(response.json()["user"], self.user.id)

    def test_create_wishlist_unauthenticated(self):
        data = {"name": "New Wishlist"}
        response = self.client.post(reverse("wish_list-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class WishListProductsViewSetTest(APITestCase):
    fixtures = [
        "apps/fixtures/users.json",
        "apps/fixtures/products.json",
        "apps/fixtures/wish_list.json",
    ]

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get(pk=1)
        self.wishlist_1 = WishList.objects.get(pk=1)
        self.wishlist_2 = WishList.objects.get(pk=2)
        self.product_1 = Product.objects.get(pk=1)
        self.product_2 = Product.objects.get(pk=2)
        self.wishlist_product_1 = WishListProducts.objects.create(
            wish_list=self.wishlist_1, product=self.product_1
        )
        self.wishlist_product_2 = WishListProducts.objects.create(
            wish_list=self.wishlist_2, product=self.product_2
        )

    def test_list_wishlist_products_authenticated(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(reverse("wish_list_products-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json().get("results")), 3)

    def test_list_wishlist_products_unauthenticated(self):
        response = self.client.get(reverse("wish_list_products-list"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_wishlist_product_authenticated(self):
        self.client.force_authenticate(self.user)
        data = {"wish_list": self.wishlist_1.id, "product": self.product_1.id}
        response = self.client.post(reverse("wish_list_products-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(WishListProducts.objects.filter(wish_list__user=self.user).count(), 4)

    def test_create_wishlist_product_unauthenticated(self):
        data = {"wish_list": self.wishlist_1.id, "product": self.product_1.id}
        response = self.client.post(reverse("wish_list_products-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class WishListProductsListViewTest(APITestCase):
    fixtures = [
        "apps/fixtures/users.json",
        "apps/fixtures/products.json",
        "apps/fixtures/wish_list.json",
    ]

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get(pk=1)
        self.wishlist_1 = WishList.objects.get(pk=1)
        self.wishlist_2 = WishList.objects.get(pk=2)
        self.product_1 = Product.objects.get(pk=1)
        self.product_2 = Product.objects.get(pk=2)
        self.wishlist_product_1 = WishListProducts.objects.create(
            wish_list=self.wishlist_1, product=self.product_1
        )
        self.wishlist_product_2 = WishListProducts.objects.create(
            wish_list=self.wishlist_2, product=self.product_2
        )

    def test_list_wishlist_products_list_view_authenticated(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(reverse("wishlist-products-list", args=[self.wishlist_1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json().get("results")), 3)
        self.assertEqual(response.json().get("results")[0]["id"], self.product_1.id)

    def test_list_wishlist_products_list_view_unauthenticated(self):
        response = self.client.get(reverse("wishlist-products-list", args=[self.wishlist_1.id]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
