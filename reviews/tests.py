from django.contrib.auth.models import User
from .models import Review
from rest_framework import status
from rest_framework.test import APITestCase

# Define a test case for the Review model
class ReviewTests(APITestCase):
    # Set up a user for the test
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
    # Test that a user can list reviews
    def test_can_list_reivews(self):
        # Get the test user
        test = User.objects.get(username='testuser')
        # Create a review for the test user
        Review.objects.create(owner=test, title='Test Review')
        # Send a GET request to the reviews endpoint
        response = self.client.get('/reviews/')
        # Check that the response status code is 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    # Test that a log in user can create a review
    def test_logged_in_user_can_create_review(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(
            '/reviews/',
            {'title': 'Logged In USER Review title', 'content': 'Logged In USER Review content'}
        )
        print(response.data)
        print(response.status_code)
        count = Review.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test that a logged out user cannot create a review
    def test_logged_out_user_cannot_create_review(self):
        response = self.client.post(
            '/reviews/',
            {'title': 'Logged Out USER Review title', 'content': 'Logged Out USER Review content'}
        )
        print(response.data)
        print(response.status_code)
        count = Review.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
