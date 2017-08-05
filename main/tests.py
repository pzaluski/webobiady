from django.test import TestCase
from django.urls import reverse
from orders.models import OrderSettings
from restaurants.models import Restaurant
from django.contrib.auth.models import User


def create_user(name, password, email=None):
    return User.objects.create_user(username=name, email=email, password=password)


def create_restaurant(name, url=None, delivery_price=0):
    return Restaurant.objects.create(name=name, menu_url=url, delivery_price=delivery_price)


def create_order_settings(restaurant, deadline, purchaser, active):
    return OrderSettings.objects.create(restaurant=restaurant, order_deadline=deadline, purchaser=purchaser, active=active)


class HomeViewTests(TestCase):

    def setUp(self):
        restaurant = create_restaurant('AktywnaRestauracja', 'webobiady.pl', 1)
        purchaser = create_user('purchaser', 'tester', 'tester@tester.pl')
        create_order_settings(restaurant, '10:10', purchaser, True)
        restaurant2 = create_restaurant('NieaktywnaRestauracja', 'http://webobiady.pl', 2)
        create_order_settings(restaurant2, '10:20', purchaser, False)

    def test_home_view_no_user(self):

        response = self.client.get(reverse('webobiady_home'))
        self.assertEqual(response.status_code, 200)

        self.assertNotContains(response, 'Twoje zamówienie')
        self.assertNotContains(response, 'Historia zamówień')
        self.assertNotContains(response, 'Import menu')
        self.assertContains(response, 'Logowanie')

        os = OrderSettings.objects.get(active=True)
        restaurant = os.restaurant
        purchaser = os.purchaser

        self.assertEqual(response.context['os'], os)
        self.assertContains(response, restaurant.name)
        self.assertContains(response, purchaser.username)

