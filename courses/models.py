from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    """
    Model representing a tag.
    """
    name = models.CharField(max_length=50)
    tag_slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        """
        Save method to automatically generate a slug based on the name.
        """
        if not self.tag_slug:
            self.tag_slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ('-name',)


class Course(models.Model):
    """
    Model representing a course.
    """
    title = models.CharField(max_length=100)
    content = RichTextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    thumbnail = models.ImageField(upload_to='courses/media/thumbnails')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Save method to automatically generate a slug based on the title.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ('-created_at',)


class Category(models.Model):
    """
    Model representing a category.
    """
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """
        Save method to automatically generate a slug based on the title.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('-title',)


class Subscriber(models.Model):
    """
    Model representing a subscriber.
    """
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'
        ordering = ('-email',)


class Contact(models.Model):
    """
    Model representing a contact.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ('-name',)


class About(models.Model):
    """
    Model representing profile information.
    """
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='courses/media/Profile_pic')
    address = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    email = models.EmailField()
    facebook = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()
    instagram = models.URLField()
    tiktok = models.URLField()
    message = RichTextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'
        ordering = ('-name',)


class Gallery(models.Model):
    """
    Model representing a gallery.
    """
    title = models.CharField(max_length=100)


class File(models.Model):
    """
    Model representing a file associated with a gallery.
    """
    gallery = models.ForeignKey(
        Gallery, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='courses/media/gallery_files')


class Testimonials(models.Model):
    """
    Model representing testimonials.
    """
    name = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    profile_pic = models.ImageField(upload_to='courses/media/testimonials')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ('-name', )
