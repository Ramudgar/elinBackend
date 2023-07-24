from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import RedirectView

from .views import (AboutView, AdminPasswordResetDoneView,
                    AdminPasswordResetView, Contact, CourseCategoryListView,
                    CourseDetailView, CourseListView, GalleryListAPIView,
                    Subscribe, TestimonialListAPIView)

urlpatterns = [



    path('admin/password_reset/',  AdminPasswordResetView.as_view(),
         name='admin_password_reset'),

    path('password_reset/done/', AdminPasswordResetDoneView.as_view(
    ), name='password_reset_done'),

    path('password_reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
         ), name='password_reset_confirm'),

    path('reset_complete/', RedirectView.as_view(url='/admin/'),
         name='password_reset_complete'),

    path('courses/', CourseListView.as_view(), name='course-list'),

    path('courses_category/<str:category_name>/',
         CourseCategoryListView.as_view(), name='course-category-list'),

    path('course/<slug:slug>/', CourseDetailView.as_view(), name='course-detail'),

    path('subscribe/', Subscribe.as_view(), name='subscribe'),

    path('contact/', Contact.as_view(), name='contact'),

    path('about/', AboutView.as_view(), name='about'),

    path('galleries/', GalleryListAPIView.as_view(), name='gallery-list'),

    path('testimonials/', TestimonialListAPIView.as_view(), name='testimonial-list'),
]
