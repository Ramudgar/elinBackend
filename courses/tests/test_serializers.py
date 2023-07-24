from django.test import TestCase
from ..models import Course, Category
from ..serializer import CourseSerializer, CategorySerializer


class CourseSerializerTest(TestCase):
    def test_course_serializer(self):
        category = Category.objects.create(title='Test Category')
        course = Course.objects.create(title='Test Course', category=category)
        serializer = CourseSerializer(course)
        expected_data = {
            'id': course.id,
            'title': 'Test Course',
            'content': '',
            'thumbnail': None,
            'created_at': course.created_at,
            'updated_at': course.updated_at,
            'slug': 'test-course',
            'category': {
                'id': category.id,
                'title': 'Test Category'
            },
            'tags': []
        }
        self.assertEqual(serializer.data, expected_data)


class CategorySerializerTest(TestCase):
    def test_category_serializer(self):
        category = Category.objects.create(title='Test Category')
        serializer = CategorySerializer(category)
        expected_data = {
            'id': category.id,
            'title': 'Test Category'
        }
        self.assertEqual(serializer.data, expected_data)
