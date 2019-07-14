from django.test import TestCase

# Create your tests here.

class HomepageViewTests(TestCase):
    def test_homepage_view(self):
        """
        homepage view
        Hello, world. You're at home.
        """
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "at home")
