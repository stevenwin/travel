from django.test import TestCase, Client
from django.urls import reverse
from .models import UserInput

class AstroTravelTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.itinerary_url = reverse('itinerary')
        self.user_input = UserInput.objects.create(
            astro_sun='Aries',
            astro_moon='Taurus',
            country='USA'
        )

    def test_home_view_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'astro_travel/home.html')

    def test_itinerary_view_GET(self):
        response = self.client.get(self.itinerary_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'astro_travel/itinerary.html')

    def test_user_input_model(self):
        self.assertEquals(self.user_input.astro_sun, 'Aries')
        self.assertEquals(self.user_input.astro_moon, 'Taurus')
        self.assertEquals(self.user_input.country, 'USA')