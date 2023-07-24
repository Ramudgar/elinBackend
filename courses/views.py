from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.views import PasswordResetDoneView

from .models import About, Category, Course, Gallery, Subscriber, Testimonials
from .serializer import (AboutSerializer, AllCourseSerializer,
                         ContactSerializer, CourseSerializer,
                         GallerySerializer, SubscriberSerializer, TestimonialSerializer)


class CourseListView(APIView):
    """
    API view for retrieving a list of courses.
    """

    def get(self, request):
        courses = Course.objects.order_by('-created_at')[:5]
        serializer = AllCourseSerializer(
            courses, many=True, context={'request': request})
        return Response(serializer.data)


class CourseCategoryListView(APIView):
    """
    API view for retrieving a list of courses by category.
    """
    serializer_class = CourseSerializer

    def get(self, request, category_name):
        try:
            category = Category.objects.get(title=category_name)
            courses = Course.objects.filter(category=category)
            serializer = self.serializer_class(
                courses, many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"message": "Category not found"}, status=status.HTTP_404_NOT_FOUND)


class CourseDetailView(APIView):
    """
    API view for retrieving course details.
    """

    def get(self, request, slug):
        try:
            course = Course.objects.get(slug=slug)
            serializer = CourseSerializer(course, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response({"message": "Course not found"}, status=status.HTTP_404_NOT_FOUND)


class CourseSearchView(APIView):
    """
    API view for searching courses.
    """

    def get(self, request):
        query = request.GET.get('q')
        if query is not None:
            courses = Course.objects.filter(title__icontains=query)
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "No query found"}, status=status.HTTP_400_BAD_REQUEST)


class Subscribe(APIView):
    """
    API view for subscribing to the newsletter.
    """

    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if Subscriber.objects.filter(email=email).exists():
                return Response({"message": "Email already subscribed"}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({"message": "You are subscribed"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Contact(APIView):
    """
    API view for submitting a contact form.
    """

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Your message has been sent"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AboutView(APIView):
    """
    API view for retrieving the about information.
    """

    def get(self, request):
        about = About.objects.first()
        serializer = AboutSerializer(about, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class GalleryListAPIView(APIView):
    """
    API view for retrieving a list of galleries.
    """

    def get(self, request):
        galleries = Gallery.objects.all()
        serializer = GallerySerializer(
            galleries, many=True, context={'request': request})
        return Response(serializer.data)
    

class TestimonialListAPIView(APIView):
    """
    API view for retrieving a list of testimonials.
    """

    def get(self, request):
        testimonials = Testimonials.objects.all()
        serializer = TestimonialSerializer(
            testimonials, many=True, context={'request': request})
        return Response(serializer.data)


class AdminPasswordResetView(PasswordResetView):
    """
    Password reset view for the admin.
    """
    from_email = 'ymilan361@gmail.com'  # Set your desired sender email address

 


class AdminPasswordResetDoneView(PasswordResetDoneView):
    def get(self, request, *args, **kwargs):
        # Add any additional context data you want to pass to the template
        context = {
            'message': 'Password reset email has been sent. Please check your email.',
        }
        return render(request, 'registration/password_reset_done.html', context)

    def get_success_url(self):
        return '/admin/'