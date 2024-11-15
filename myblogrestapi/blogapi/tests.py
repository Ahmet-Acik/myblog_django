from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import BlogPost

class BlogPostTests(APITestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_post(self):
        url = reverse('create_post')  # Ensure this matches the name of your URL pattern
        data = {
            "title": "Avoid Your Phone First Thing",
            "body": "Reaching for your phone as soon as you wake up can lead to mindless scrolling and information overload. Instead, resist the urge to check emails or social media right away. Giving yourself at least 15-30 minutes before diving into digital distractions allows your mind to ease into the day naturally. Use this time to focus on yourself, set intentions, and enjoy a peaceful start."
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlogPost.objects.count(), 1)
        self.assertEqual(BlogPost.objects.get().title, data['title'])