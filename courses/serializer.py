from bs4 import BeautifulSoup
from django.conf import settings
from rest_framework import serializers

from .models import (About, Category, Contact, Course, File, Gallery,
                     Subscriber, Tag, Testimonials)


class AllCourseSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving a subset of course fields.
    """
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('thumbnail', 'title', 'created_at', 'slug')

    def get_thumbnail(self, instance):
        """
        Get the absolute URL of the thumbnail.
        """
        request = self.context.get('request')
        if request and instance.thumbnail:
            thumbnail_url = request.build_absolute_uri(instance.thumbnail.url)
            return thumbnail_url
        return None

    def to_representation(self, instance):
        """
        Override the to_representation method to modify the serialized data.
        """
        data = super().to_representation(instance)

        # Format the created_at date as "YYYY-MM-DD"
        data['created_at'] = instance.created_at.strftime('%Y-%m-%d')
        return data


class TagSerializer(serializers.ModelSerializer):
    """
    Serializer for the Tag model.
    """
    class Meta:
        model = Tag
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    """
    class Meta:
        model = Category
        fields = ('id', 'title')


class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer for the Course model.
    """
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'content', 'thumbnail', 'created_at',
                  'updated_at', 'slug', 'category', 'tags')

    def get_thumbnail_url(self, obj):
        """
        Get the absolute URL of the thumbnail.
        """
        request = self.context.get('request')
        if obj.thumbnail:
            return request.build_absolute_uri(obj.thumbnail.url)
        return None

    def to_representation(self, instance):
        """
        Override the to_representation method to modify the serialized data.
        """
        data = super().to_representation(instance)
        data['thumbnail'] = self.get_thumbnail_url(instance)

        # Format the created_at date as "YYYY-MM-DD"
        data['created_at'] = instance.created_at.strftime('%Y-%m-%d')
        return data


class SubscriberSerializer(serializers.ModelSerializer):
    """
    Serializer for the Subscriber model.
    """
    class Meta:
        model = Subscriber
        fields = ['email']


class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contact model.
    """
    class Meta:
        model = Contact
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new Contact instance.
        """
        return Contact.objects.create(**validated_data)


class AboutSerializer(serializers.ModelSerializer):
    """
    Serializer for the About model.
    """
    profile_pic = serializers.SerializerMethodField()

    class Meta:
        model = About
        fields = ('id', 'name', 'profile_pic', 'address', 'qualification', 'email',
                  'facebook', 'twitter', 'linkedin', 'instagram', 'tiktok', 'message', 'updated_at')

    def get_profile_pic(self, obj):
        """
        Get the absolute URL of the profile picture.
        """
        request = self.context.get('request')
        if obj.profile_pic:
            return request.build_absolute_uri(obj.profile_pic.url)
        return None

    def to_representation(self, instance):
        """
        Override the to_representation method to modify the serialized data.
        """
        data = super().to_representation(instance)
        data['profile_pic'] = self.get_profile_pic(instance)
        return data


class FileSerializer(serializers.ModelSerializer):
    """
    Serializer for the File model.
    """
    class Meta:
        model = File
        fields = ('file',)


class GallerySerializer(serializers.ModelSerializer):
    """
    Serializer for the Gallery model.
    """
    files = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = ('files',)

    def get_files(self, obj):
        """
        Get the absolute URLs of all the files in the gallery.
        """
        request = self.context.get('request')
        return [request.build_absolute_uri(file.file.url) for file in obj.files.all()]


class TestimonialSerializer(serializers.ModelSerializer):
    """
    Serializer for the Testimonial model.
    """
    class Meta:
        model = Testimonials
        fields = ('name', 'message', 'profile_pic', 'created_at')

    def get_profile_pic(self, obj):
        """
        Get the absolute URL of the profile picture.
        """
        request = self.context.get('request')
        if obj.profile_pic:
            return request.build_absolute_uri(obj.profile_pic.url)
        return None

    def to_representation(self, instance):
        """
        Override the to_representation method to modify the serialized data.
        """
        data = super().to_representation(instance)
        data['profile_pic'] = self.get_profile_pic(instance)

        # Format the created_at date as "YYYY-MM-DD"
        data['created_at'] = instance.created_at.strftime('%Y-%m-%d')

        return data
