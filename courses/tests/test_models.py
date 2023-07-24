from django.test import TestCase
from ..models import Course, Category


class CourseModelTest(TestCase):
    def test_course_creation(self):
        category = Category.objects.create(title='Test Category')
        course = Course.objects.create(title='Test Course', category=category)
        self.assertEqual(course.title, 'Test Course')
        self.assertEqual(course.category, category)

    def test_course_slug(self):
        category = Category.objects.create(title='Test Category')
        course = Course.objects.create(title='Test Course', category=category)
        self.assertEqual(course.slug, 'test-course')


class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(title='Test Category')
        self.assertEqual(category.title, 'Test Category')
