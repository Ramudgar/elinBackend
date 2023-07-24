from django.test import TestCase, RequestFactory
from rest_framework import status
from ..views import CourseListView
from ..models import Course, Category


class CourseListViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_course_list_view(self):
        request = self.factory.get('/courses/')
        response = CourseListView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
