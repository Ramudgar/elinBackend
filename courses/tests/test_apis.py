from django.test import TestCase, Client
from rest_framework import status


class APITests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_course_list_api(self):
        response = self.client.get('/api/v1/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_category_api(self):
        response = self.client.get('/api/v1/courses_category/Reading/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_detail_api(self):
        response = self.client.get('/api/v1/course/test-course/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # Add more tests for other API endpoints
