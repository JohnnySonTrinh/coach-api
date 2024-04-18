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
        # print(response.data)
        # print(len(response.data))

    # Test that a log in user can create a review
    def test_logged_in_user_can_create_review(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(
            '/reviews/',
            {'title': 'Logged In USER Review title', 'content': 'Logged In USER Review content'}
        )
        # print(response.data)
        # print(response.status_code)
        count = Review.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test that a logged out user cannot create a reviewc
    def test_logged_out_user_cannot_create_review(self):
        response = self.client.post(
            '/reviews/',
            {'title': 'Logged Out USER Review title', 'content': 'Logged Out USER Review content'}
        )
        # print(response.data)
        # print(response.status_code)
        count = Review.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

# Define a test case for the ReviewDetail view
class ReviewDetailViewTests(APITestCase):
    def setUp(self):
        testuser1 = User.objects.create_user(
            username='testuser1',
            password='testpassword'
        )
        testuser2 = User.objects.create_user(
            username='testuser2',
            password='testpassword'
        )
        Review.objects.create(
            owner=testuser1,
            title='Test Review 1',
            content='Test Review 1 content',
        )
        Review.objects.create(
            owner=testuser2,
            title='Test Review 2',
            content='Test Review 2 content',
        )

    def test_can_retrieve_review_using_valid_id(self):
        response = self.client.get('/reviews/1/')
        self.assertEqual(response.data['title'], 'Test Review 1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.data)
        # print(len(response.data))

    def test_cannot_retrieve_review_using_invalid_id(self):
        response = self.client.get('/reviews/823/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # print(response.data)
        # print(len(response.data))

    def test_can_update_review_using_valid_id(self):
        self.client.login(username='testuser1', password='testpassword')
        response = self.client.put(
            '/reviews/1/',
            {'title': 'Updated Review 1', 'content': 'Updated Review 1 content'}
        )
        self.assertEqual(response.data['title'], 'Updated Review 1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.data)
        # print(len(response.data))

    def test_cannot_update_review_using_invalid_id(self):
        self.client.login(username='testuser1', password='testpassword')
        response = self.client.put(
            '/reviews/2/',
            {'title': 'Updated Review 1', 'content': 'Updated Review 1 content'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        print(response.data)
        print(len(response.data))